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

    cli_check = airflow_pb2_grpc.ServiceCheckStub(channel=conn)
    for count in range(3):
        try:
            res_check = cli_check.ServiceCheck(airflow_pb2.ReqCheckSvcData(health_url='http://www.baidu.com/'))
        except Exception, e:
            print '500'
        else:
            print res_check.status
        import time
        time.sleep(10)


if __name__ == '__main__':
    run()
