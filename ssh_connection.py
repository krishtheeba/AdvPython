import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
try:
	client.connect('127.0.0.1')
except Exception as eobj:
	print(eobj)

stdin, stdout, stderr = client.exec_command('ls -l')

for var in stdout:
	print(var)
