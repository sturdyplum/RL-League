"""
Initial file where entering
"""

from . import server
from proto_api.shared.games_pb2 import Agent 

if __name__ == '__main__':
    agents = []
    for i in range(10):
        agent = Agent()
        agent.id = i + 1
        agent.elo = 1500
        agents.append(agent)

    server.serve(agents)
