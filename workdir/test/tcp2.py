#! /usr/bin/env python
# coding=utf-8

from SocketServer import TCPServer, BaseRequestHandler
import traceback

class MyBaseRequestsHandlerr(BaseRequestHandler):
    '''
    # 从BaseRequestHandler继承，并重写handle方法
    '''

    def handle(self):
        # 循环监听（读取）来自客户端的数据
        while True:
            # 当客户端主动断开连接时，self.recv(1024)会抛出异常
            try:
                # 一次读取1024字节，并去除两端的空白字符（包括空格，TAB,\r,\n）
                data = self.request.recv(1024).strip()
                # self.client_address是客户端的连接（host，port）的元组
                print "receive from (%r):%r"%(self.client_address, data)
                # 转换成大写后写回（发生到）客户端
                self.request.sendall(data.upper())
            except:
                traceback.print_exc()
                break
if __name__ == '__main__':
    # telnet 127.0.01 9999
    host = "" #主机名，可以是ip,像localhost的主机名，或""
    port = 8080 #端口
    addr = (host, port)
    # 购置TCPServer对象
    server = TCPServer(addr, MyBaseRequestsHandlerr)

    #启动服务监听
    server.serve_forever()
