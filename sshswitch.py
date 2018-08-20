mport paramiko
import time

def MAIN(ip):

    host = ip
    port = 22
    user = 'user'
    pswd = 'password'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, user, pswd,)

    chan= ssh.invoke_shell()
    chan.send('enable\n')
    time.sleep(0.5)

    chan.send('password'+'\n')
    time.sleep(0.5)

    chan.send('conf t'+'\n')
    time.sleep(0.5)

    chan.send('interface fast 0/2'+'\n')
    time.sleep(0.5)

    chan.send('shut'+'\n')
    time.sleep(0.5)

    chan.send('end'+'\n')
    time.sleep(0.5)

    #chan.send('show run'+'\n')
    #time.sleep(3)

    result = chan.recv(100000).decode()
    
    chan.close()
    ssh.close()
    print(result)
    Wr(result, host)

def Wr(info, ip):
    print('saving file, wait a moment... ')
    t = time.strftime('%Y%m%d')
    with open('/home/liang/Desktop/' + t + '.txt', 'w') as f:
        f.write('ip:%s' %(ip) + info )

def Loop():
    hosts = ['10.0.0.55',]
    for i in hosts:
        MAIN(i)

if __name__=='__main__':
    try:
        #a = input('>>>')
        MAIN(a)
		
    except Exception as e:
        print(e)

