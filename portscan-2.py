#!usr/bin/python3
from socket import *
from termcolor import colored
import optparse
from threading import *
from time import *

def retbanner(ip,port):
   try:
      sock=socket(AF_INET,SOCK_STREAM)
      b=sock.connect((ip,int(port)))
      banner=sock.recv(1024)
      return banner
   except:
      print("not")
      return

def ascending(port):
   #for arranging in ascending order:
    for i in range(len(port)):
       port[i]=int(port[i])
    port.sort()

    for i in range(len(port)):
       port[i]=str(port[i])

def main():
    #for arguments:

    parser=optparse.OptionParser("usage of program: -H <target host> -P <target ports seprated with comma> -A <to scan all ports> ")
    parser.add_option("-H", dest='host',type='string',help='specify host to scan')
    parser.add_option('-P', dest='port',type='string',help='specify port seprated with ,')
    parser.add_option('-A', dest='', help='to scan all ports')
    (options,args)= parser.parse_args()
    host=options.host
    port=str(options.port).split(',')
    
    # print usage:
    if (host==None)|(port==None):
        print(colored(parser.usage,'red'))
        exit(0)
    ascending(port)
    scanner(host,port)
    

def scanner(host,port):

     try:
        ip=gethostbyname(host)
     except:
        print(colored("host not found","red"))
    
     try:
        hostname=gethostbyaddr(ip)
        print(colored("[+]scanning result for "+ip+" ["+hostname[0]+"]",'blue'))
        
     except:
        pass

     #For Threading: 
     for i in port:
        
        t=Thread(target=conn,args=(host,i))
        t.start()
        sleep(0.00001)

     
def conn(host,port):
    try:
         sock=socket(AF_INET,SOCK_STREAM)
         #sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
         #socket.setdefaulttimeout(2
         result=sock.connect((host,int(port)))
         ban = retbanner(host,port).decode("utf-8")
         print(colored("\n[+]port "+port+" is open"+"\t"+ban+"\n",'green'))
         
    except:     
         print(colored("[-]tcp port "+port+" is not open",'red'))
    
    finally:
       sock.close()


if __name__ == "__main__":
    main()
