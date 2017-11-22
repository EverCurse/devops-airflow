#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from protobufs import airflow_pb2, airflow_pb2_grpc

_HOST = 'localhost'
_PORT = '9999'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = airflow_pb2_grpc.PingStub(channel=conn)
    response = client.Ping(airflow_pb2.ReqPingData(health_url=''))
    print response.status

    client2 = airflow_pb2_grpc.DeployStub(channel=conn)
    response2 = client2.Deploy(airflow_pb2.ReqDeployData(version='v1.2', type='jar', service='haixue_demo', port=9500))
    print response2.ret


if __name__ == '__main__':
    run()
