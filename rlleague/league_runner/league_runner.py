import grpc
import random

from proto_api.league_runner import runner_service_pb2 as RunnerProtos
from proto_api.league_runner import runner_service_pb2_grpc as RunnerService


class LeagueRunner(RunnerService.LeagueRunnerServicer):

    """
        agent_manager -
            Manages the agents. Responsible for selecting which agents to give 
            to a client and maintaining agent elos.
        game_timeout -
            The amount of time (per game) to wait for a client to repsond with
            the game results before reasigning those agents to another client. 
        client_reset_time -
            The amount of time before a clients uuid will expire and they will 
            need to request new agents. (This is to prevent a slow client from 
            affecting an agent too much)
    """
    def __init__(self, agent_manager, game_timeout = 60):
        self.agent_manager = agent_manager
        self.game_timeout = game_timeout
        self.uuid_to_agents = {}

    """ Gets a unique id for an agent and then inserts it into the uuid map. """
    def get_unique_id(self):
        uuid = random.randint(0, 1_000_000_000)
        while uuid in self.uuid_to_agents:
            uuid = random.randint(0, 1_000_000_000)
            self.uuid_to_agents[uuid] = []
        return uuid


    def RequestAgents(
            self, request: RunnerProtos.AgentRequest, context):
        print ("agent requested")
        response = RunnerProtos.AgentResponse()
        response.uuid = self.get_unique_id()
        for agent in self.agent_manager.reserve_n_agents(request.number_of_agents):
            response.agents.append(agent)

        if len(response.agents) < request.number_of_agents:
            return grpc.Status(grpc.StatusCode.FAILED_PRECONDITION,
                               "Requested more agents than are available.")
        return response

