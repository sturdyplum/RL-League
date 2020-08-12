import abc
import asyncio
import random
import uuid

from proto_api.shared.games_pb2 import Agent


class AgentManagerInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "reserve_n_agents")
                and callable(subclass.reserve_n_agents)
                and hasattr(subclass, "release_agents")
                and callable(subclass.release_agents)
                and hasattr(subclass, "get_agent")
                and callable(subclass.get_agent)
                and hasattr(subclass, "update_agent")
                and callable(subclass.update_agent)
                and hasattr(subclass, "report_result")
                and callable(subclass.report_result))

    @abc.abstractclassmethod
    def reserve_n_agents(self, n: int):
        """ Reserves N agents and returns the ids of those agents. """
        raise NotImplementedError

    @abc.abstractclassmethod
    def release_agents(self, agents: [Agent]):
        """ Frees all agents in list so they can be reserved again. """
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_agent(self, agent_id: str):
        """ Returns an instance of the agent with id `agent_id`. """
        raise NotImplementedError

    @abc.abstractclassmethod
    def update_agent(self, agent_id: str, new_agent: Agent):
        """ Updates the agent with id `agent_id` to `new_agent` """
        raise NotImplementedError

    @abc.abstractclassmethod
    def report_result(self, agent_ids: [int], result: int):
        """
        Reports the result of a game between agents and the index of
        the winner or -1 if it was a tie.
        """
        raise NotImplementedError


class InMemoryAgentManager(AgentManagerInterface):
    """
    An agent manager class that holds all agents in memory. This is usefull for
    testing.
    """

    def __init__(self, agents: [Agent], elo_manager):
        self.agents = {agent.id: agent for agent in agents}
        self.free_agents = set(agent.id for agent in agents)
        self.lock = asyncio.Lock()
        self.elo_manager = elo_manager

    def reserve_n_agents(self, n: int):
        """
        Since this is a testing class the agents will be randomly picked.
        """
        async with self.lock:
            res = []
            if n > len(self.free_agents):
                return res
            for _ in range(n):
                agent = random.choice(self.free_agents)
                self.free_agents.remove(agent)
                res.append(agent)
            return res

    def release_agents(self, agents: [Agent]):
        async with self.lock:
            for agent in agents:
                self.free_agents.add(agent)

    def get_agent(self, agent_id: str):
        if agent_id not in self.agents:
            raise KeyError
        return self.agents[agent_id]

    def update_agent(self, agent_id: str, agent: Agent):
        if agent_id not in self.agents:
            raise KeyError
        self.agents[agent_id] = agent

    def report_result(self, agent_ids: [int], result: int):
        agent_elos = [self.agents[agent_id].elo for agent_id in agent_ids]
        new_elos = self.elo_manager.get_new_elos(agent_elos, result)
        for new_elo, agent_id in zip(new_elos, agent_ids):
            self.agents[agent_id].elo = new_elo
