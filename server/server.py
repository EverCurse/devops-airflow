#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
from protobufs import airflow_pb2_grpc, airflow_pb2
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import ConnectTimeout

_ONE_DAY_IN_SECONDS = 24*60*60
_HOST = 'localhost'
_PORT = '9999'


class Ping(airflow_pb2_grpc.PingServicer):
    """
    部署前的agent存活检测
    """
    def Ping(self, request, context):
        status = 'Pong'
        return airflow_pb2.RespPingData(status=status)


class Deploy(airflow_pb2_grpc.DeployServicer):
    """
    正式部署
    """
    def Deploy(self, request, context):
        status = 'Pong'
        return airflow_pb2.RespDeployData(status=status)


class ServiceCheck(airflow_pb2_grpc.ServiceCheckServicer):
    """
    服务部署后 检测服务暴露的check status url
    """
    def ServiceCheck(self, request, context):
        print 'welcome client...'
        check_url = request.health_url
        try:
            r = requests.get(check_url, timeout=10)
        except ConnectionError, _:
            return airflow_pb2.RespCheckSvcData(status='could not connet url {0}'.format(check_url))
        except ConnectTimeout, _:
            return airflow_pb2.RespCheckSvcData(status='{0} connect timeout'.format(check_url))
        ret = r.status_code
        if ret == 200:
            status = 200
        else:
            status = ret
        return airflow_pb2.RespCheckSvcData(status=u'{0}'.format(status))


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    airflow_pb2_grpc.add_PingServicer_to_server(Ping(), grpcServer)
    airflow_pb2_grpc.add_ServiceCheckServicer_to_server(ServiceCheck(), grpcServer)
    airflow_pb2_grpc.add_DeployServicer_to_server(Deploy(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
