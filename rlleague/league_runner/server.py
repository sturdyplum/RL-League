import grpc
import rlleague.league_runner.runner_service_pb2 as RunnerProtos
import rlleague.league_runner.runner_service_pb2_grpc as RunnerService
from concurrent import futures

class LeagueRunner(RunnerService.LeagueRunnerServicer):
    num_agents = 10

    def RequestAgents(
            self, request: RunnerProtos.AgentRequest, context):
        if self.num_agents < request.number_of_agents:
            return grpc.Status(grpc.StatusCode.FAILED_PRECONDITION,
                               "Requested more agents than are available.")
        response = RunnerProtos.AgentResponse()
        response.uuid = 7
        return response 

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    RunnerService.add_LeagueRunnerServicer_to_server(LeagueRunner(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
