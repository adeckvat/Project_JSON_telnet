import sys, os, time
import telnetlib

HOST = "10.16.135.2"
PORT = "23"
bytes_data = [112, 52, 52]
user = "apc" 
passwd = "MasterApc"

def connectionToServer(HOST, PORT):
  pingStr = "ping " + HOST #Attempt to ping host
  if (os.system(pingStr)==0): #Host able to be pinged
    print ("Robot found...") #Comma prevents printed line from wrapping
    try: #Attempt to connect to remote host
      tn = telnetlib.Telnet(host = HOST, port = PORT)
      print ("Connected!")
    except Exception as E: #Failed connection
      print ("Connection failed!")
      raise E
  else:                       #Host not found
    print ("Host not found")
    raise ValueError('Could not connect to a host')

  tn = telnetlib.Telnet(HOST, PORT, timeout=10)
  tn.expect([b"Login: ", b"User Name: ", b"User Name:", b"Username:"], 5)
  tn.write(user.encode('ascii') + b"\r\n")
  tn.expect([b"Password: ", b"password"], 5)
  tn.write(passwd.encode('ascii') + b"\r\n")
  tn.interact()

print(connectionToServer(HOST, PORT))
