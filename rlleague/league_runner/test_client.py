import grpc
import rlleague.league_runner.runner_service_pb2_grpc as RunnerService
import rlleague.league_runner.runner_service_pb2 as RunnerProtos


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = RunnerService.LeagueRunnerStub(channel)
        response = stub.RequestAgents(RunnerProtos.AgentRequest(number_of_agents=2))
        print(response)

if __name__ == '__main__':
    run()