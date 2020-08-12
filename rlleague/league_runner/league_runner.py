import grpc
import random
import uuid

from proto_api.league_runner import runner_service_pb2 as RunnerProtos
from proto_api.league_runner import runner_service_pb2_grpc as RunnerService


class LeagueRunner(RunnerService.LeagueRunnerServicer):

    """
        intial_agents -
            The list of initial agents to train with.
        game_timeout -
            The amount of time (per game) to wait for a client to repsond with
            the game results before reasigning those agents to another client. 
        client_reset_time -
            The amount of time before a clients uuid will expire and they will 
            need to request new agents. (This is to prevent a slow client from 
            affecting an agent too much)
    """

    def __init__(self, initial_agents, game_timeout = 60):
        self.available_agents = initial_agents
        self.taken_agents = set()
        self.game_timeout = game_timeout
        self.uuid_to_agents = {}

    """ Gets a unique id for an agent and then inserts it into the uuid map. """
    def get_unique_id(self):
        new_uuid = uuid.uuid4().hex
        self.uuid_to_agents[new_uuid] = []
        return new_uuid

    # TODO(sturdyplum) Currently this is random but there should be a smarter 
    # way of doing this to make sure things are balanced.
    def pick_agents(self, num_agents):
        agents = []
        for i in range(num_agents):
            # agent = random.choice(self.available_agents)
            agent = self.available_agents[i]
            # self.available_agents.remove(agent)
            # self.taken_agents.add(agent)
            agents.append(agent)
        return agents

    def RequestAgents(
            self, request: RunnerProtos.AgentRequest, context):
        if len(self.available_agents) < request.number_of_agents:
            return grpc.Status(grpc.StatusCode.FAILED_PRECONDITION,
                               "Requested more agents than are available.")
        response = RunnerProtos.AgentResponse()
        response.uuid = self.get_unique_id()
        for agent in self.pick_agents(request.number_of_agents):
            response.agents.append(agent)
        # response.agents = self.pick_agents(request.number_of_agents)
        return response
