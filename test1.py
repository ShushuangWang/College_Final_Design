#print(eval(input()) + eval(input()))
#print(eval(input())+eval(input()))
#a = int(input())
#print(a)

# def cost(x):
#   if x<0:
#     print("Invalid Value!")
#     exit()
#   return x*0.53 if x<=50 else 0.53*50+(x-50)*0.58

# print("cost = {:.2f}".format(cost(int(input()))))

import socket
 
target_host = "www.badu.com"
target_port = 80
#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the client
client.connect((target_host, target_port))
#send some data
#client.send("GET / HTTP/1.r\nHost: baidu.com\r\n\r\n")
#receive some data
send_data = "GET / HTTP/1.r\nHost: baidu.com\r\n\r\n"
client.send(send_data.encode("utf-8")) 
response = client.recv(4096)
print(response)
