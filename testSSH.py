import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ssh.arkantus.eu',username='marc',password='tioli13co')
stdin, stdout,stderr = ssh.exec_command("ls")
print type(stdin)
print stdout.readlines()