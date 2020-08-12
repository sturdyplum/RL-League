"""
Initial file where entering
"""
import logging
from . import server
from .league_runner.agent_manager.agent_manager import InMemoryAgentManager
from .league_runner.elo_manager.elo_manager import WinRateEloManager
from proto_api.shared.games_pb2 import Agent 

if __name__ == '__main__':
    logging.basicConfig()
    agents = []
    for i in range(10):
        agent = Agent()
        agent.id = i + 1
        agent.elo = 1500
        agents.append(agent)

    elo_manager = WinRateEloManager()
    agent_manager = InMemoryAgentManager(agents, elo_manager)
    server.serve(agent_manager)
