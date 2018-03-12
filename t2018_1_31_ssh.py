# coding: utf-8

# import paramiko

# paramiko.util.log_to_file('files/paramiko.log')
# s = paramiko.SSHClient()

# s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# s.connect('172.20.40.137', 22, 'zhukb', 'zhukb')
# stdin,stdout,stderr = s.exec_command('ls -lh')
# print stdout.read()
# s.close()


from sshtunnel import SSHTunnelForwarder

server =  SSHTunnelForwarder(
    ssh_address_or_host=('172.20.40.136', 22), # 指定ssh登录的跳转机的address
    ssh_username='scrapyer', # 跳转机的用户
    ssh_password='scrapy', # 跳转机的密码
    local_bind_address=('127.0.0.1', 8882),# 本地绑定的端口
    remote_bind_address=('0.0.0.0', 8882)) # 远程绑定的端口

server.start()

