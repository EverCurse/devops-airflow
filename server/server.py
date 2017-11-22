#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
import sys
sys.path.append('..')
from protobufs import airflow_pb2_grpc, airflow_pb2
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import ConnectTimeout
import subprocess

_ONE_DAY_IN_SECONDS = 24*60*60


def query_address():
    _HOST = ''
    with file('/etc/private.ip') as f:
        for line in f.readlines():
            _HOST = line.strip()
            break
    print 'service register at {0}'.format(_HOST)
    return _HOST


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
        ret_logs = ''

        # step 1, create dir
        p_mkdir = subprocess.Popen('mkdir -p /home/www-data/deploy/{0}/{1}/'.format(request.service,
                                                                                    request.version),
                                   shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if not p_mkdir.stderr.readlines():
            ret_logs += u'创建 /home/www-data/deploy/{0}/{1}/ 成功 \n'.format(request.service, request.version)
        else:
            ret = {
                'status': '500',
                'logs': 'mkdir to save jar file failed',
            }
            return airflow_pb2.RespDeployData(ret=ret)

        # step 2, down jar file
        r = requests.get('http://192.168.15.255:9999/api.jar', stream=True)
        jar_name = request.service+'-'+request.version+'.jar'
        jar_path = "/home/www-data/deploy/{0}/{1}/{2}".format(request.service, request.version, jar_name)
        f = open(jar_path, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
        ret_logs += u'下载文件 {0}-{1}.jar 成功 \n'.format(request.service, request.version)

        # step 3 停止旧代码进程
        p_stop_proc = subprocess.Popen('/usr/bin/supervisorctl stop {0}'.format(request.service),
                                       shell=True, stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not p_stop_proc.stderr.readlines():
            ret_logs += u'service进程成功停止 \n'.format(request.service)
        else:
            ret = {
                'status': '500',
                'logs': 'service {0} stop proccess failed,exception: {1}'.format(request.service,
                                                                                 p_stop_proc.stderr.read()),
            }
            return airflow_pb2.RespDeployData(ret=ret)

        # step 4 替换旧代码
        _ = subprocess.Popen('mkdir -p /data/{0}'.format(request.service),
                             shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p_replace_jar = subprocess.Popen('cp -r -f {0} /data/{1}/'.format(jar_path, request.service),
                                         shell=True, stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not p_replace_jar.stderr.readlines():
            ret_logs += u'{0} 复制到工作目录成功 \n'.format(jar_name)
        else:
            ret = {
                'status': '500',
                'logs': 'file {0} cp  to work dir failed'.format(jar_name),
            }
            return airflow_pb2.RespDeployData(ret=ret)

        # step 5 启动服务
        p_start_service = subprocess.Popen('/usr/bin/supervisorctl start {0}'.format(request.service),
                                     shell=True, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not p_start_service.stderr.readlines():
            ret_logs += u'service {0} 进程启动成功 \n'.format(request.service)
        else:
            ret = {
                'status': '500',
                'logs': 'service {0} start failed,exception: {1}'.format(request.service, p_start_service.stderr.read()),
            }
            return airflow_pb2.RespDeployData(ret=ret)

        # 以上全无异常
        ret = {
            'status': '200',
            'logs': ret_logs,
        }
        return airflow_pb2.RespDeployData(ret=ret)


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
    grpcServer.add_insecure_port(query_address() + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
