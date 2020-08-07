# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from rlleague.league_runner import runner_service_pb2 as rlleague_dot_league__runner_dot_runner__service__pb2


class LeagueRunnerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestAgents = channel.unary_unary(
                '/LeagueRunner/RequestAgents',
                request_serializer=rlleague_dot_league__runner_dot_runner__service__pb2.AgentRequest.SerializeToString,
                response_deserializer=rlleague_dot_league__runner_dot_runner__service__pb2.AgentResponse.FromString,
                )
        self.RequestGames = channel.unary_unary(
                '/LeagueRunner/RequestGames',
                request_serializer=rlleague_dot_league__runner_dot_runner__service__pb2.GameRequest.SerializeToString,
                response_deserializer=rlleague_dot_league__runner_dot_runner__service__pb2.GameResponse.FromString,
                )
        self.ReportResults = channel.unary_unary(
                '/LeagueRunner/ReportResults',
                request_serializer=rlleague_dot_league__runner_dot_runner__service__pb2.ReportRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LeagueRunnerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RequestAgents(self, request, context):
        """Will rqeuest a set of agents to run games for. Any given main agent 
        should only belong to one `GameRunner` at a time to prevent multiple 
        people from training the same agents at once.

        TODO(sturdyplum) Maybe the best idea would be to let multiple people 
        train a main agent at once but only keep the best as the main agent and 
        make the rest copies. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestGames(self, request, context):
        """Will return a list of games to play. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportResults(self, request, context):
        """Used to report the results of playing all the games in a GameReponse 
        (along with any updated network for main agents).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LeagueRunnerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestAgents': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestAgents,
                    request_deserializer=rlleague_dot_league__runner_dot_runner__service__pb2.AgentRequest.FromString,
                    response_serializer=rlleague_dot_league__runner_dot_runner__service__pb2.AgentResponse.SerializeToString,
            ),
            'RequestGames': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestGames,
                    request_deserializer=rlleague_dot_league__runner_dot_runner__service__pb2.GameRequest.FromString,
                    response_serializer=rlleague_dot_league__runner_dot_runner__service__pb2.GameResponse.SerializeToString,
            ),
            'ReportResults': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportResults,
                    request_deserializer=rlleague_dot_league__runner_dot_runner__service__pb2.ReportRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LeagueRunner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LeagueRunner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RequestAgents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LeagueRunner/RequestAgents',
            rlleague_dot_league__runner_dot_runner__service__pb2.AgentRequest.SerializeToString,
            rlleague_dot_league__runner_dot_runner__service__pb2.AgentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LeagueRunner/RequestGames',
            rlleague_dot_league__runner_dot_runner__service__pb2.GameRequest.SerializeToString,
            rlleague_dot_league__runner_dot_runner__service__pb2.GameResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LeagueRunner/ReportResults',
            rlleague_dot_league__runner_dot_runner__service__pb2.ReportRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)