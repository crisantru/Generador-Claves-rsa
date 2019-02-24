import subprocess

args_values = [' -A', ' -0', ' -y']
args = [0, 0, 1]

longitud = 50

#pwd = check_call("pwgen")
command = 'pwgen ' + str(longitud)

if args[0]:
	command += args_values[0]
if args[1]:
	command += args_values[1]
if args[2]:
	command += args_values[2]

print('command: ' + command)

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output, error = process.communicate()

print(output)
#print(pwd)