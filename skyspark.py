print "hello sujil ";
import os
import subprocess
currentDir= os.getcwd();
fileDir=currentDir+"\s.bat";

os.system(fileDir + ' >> 123.txt | tail -l ');
import subprocess
p = subprocess.Popen("cat file.log | tail -1", shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#Try shell=True if the above doesn't work with shell=False
p_stdout = p.stdout.read()
p_stderr = p.stderr.read()
print p_stdout
