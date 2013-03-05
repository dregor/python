import subprocess
pipe = subprocess.Popen('python echoenv.py',shell=True,stdout = subprocess.PIPE)
print( pipe.stdout.read() )
pipe.returncode

