# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import analyze_pb2 as analyze__pb2


class AnalyzeServiceStub(object):
  """The Analyze Service is a service that analyze a given the text using predefined analyzers fields to identify patterns, 
  formats, and checksums with relevant context.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Apply = channel.unary_unary(
        '/types.AnalyzeService/Apply',
        request_serializer=analyze__pb2.AnalyzeRequest.SerializeToString,
        response_deserializer=analyze__pb2.AnalyzeResponse.FromString,
        )
    self.GetAllRecognizers = channel.unary_unary(
        '/types.AnalyzeService/GetAllRecognizers',
        request_serializer=analyze__pb2.RecognizersAllRequest.SerializeToString,
        response_deserializer=analyze__pb2.RecognizersAllResponse.FromString,
        )


class AnalyzeServiceServicer(object):
  """The Analyze Service is a service that analyze a given the text using predefined analyzers fields to identify patterns, 
  formats, and checksums with relevant context.
  """

  def Apply(self, request, context):
    """Apply method will execute on the given request and return the analyze response with the sensitive text findings
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllRecognizers(self, request, context):
    """Gets the list of known recognizers.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AnalyzeServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Apply': grpc.unary_unary_rpc_method_handler(
          servicer.Apply,
          request_deserializer=analyze__pb2.AnalyzeRequest.FromString,
          response_serializer=analyze__pb2.AnalyzeResponse.SerializeToString,
      ),
      'GetAllRecognizers': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllRecognizers,
          request_deserializer=analyze__pb2.RecognizersAllRequest.FromString,
          response_serializer=analyze__pb2.RecognizersAllResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'types.AnalyzeService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
