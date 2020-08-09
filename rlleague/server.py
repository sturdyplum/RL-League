import grpc

from concurrent import futures
from .league_runner import league_runner
from proto_api.league_runner import runner_service_pb2_grpc as RunnerService
from proto_api.shared.games_pb2 import Agent


def serve(agents):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    RunnerService.add_LeagueRunnerServicer_to_server(
        league_runner.LeagueRunner(agents), server)
    server.add_insecure_port('[::]:50051')
    print("Starting server")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    agents = []
    for i in range(10):
        agent = Agent()
        agent.id = i
        agent.elo = 1500
        agents.append(agent)
    
    serve(agents)
