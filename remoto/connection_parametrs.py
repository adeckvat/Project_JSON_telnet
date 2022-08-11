from pydoc import cli
from sqlite3 import connect
import paramiko
import subprocces
#paramiko
client = paramiko.SSHClient()

client.connect(
hostname="10.16.135.2", 
port=22, 
username="apc", 
passphrase="MasterApc",
timeout=5, # sec
banner_timeout=5,
auth_timeout=5
)

#sub