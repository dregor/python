import subprocess
pipe = subprocess.Popen('python3 -u ./childproc.py ',shell=True,stdout = subprocess.PIPE)
for line in pipe.stdout:
    print(  line  )
pipe.returncode

