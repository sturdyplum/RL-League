"""
Initial file where entering
"""
import uuid

from . import server
from proto_api.shared.games_pb2 import Agent 

if __name__ == '__main__':
    agents = []
    for i in range(10):
        agent = Agent()
        agent.uuid = uuid.uuid4().hex
        agent.elo = 1500
        agents.append(agent)

    server.serve(agents)
