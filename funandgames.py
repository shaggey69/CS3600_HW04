import crypt

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

boss_password = getHahsedPW("yourboss",my_input)
sys_admin_password = getHahsedPW("sysadmin",my_input)
your_buddy_password = getHahsedPW("yourbuddy",my_input)

print(findWord(my_dict.split(),boss_password))
print(findWord(my_dict.split(),sys_admin_password))




'''
subprocess.run(args, *, stdin=None, input=None, stdout=None,
stderr=None, shell=False, timeout=None, check=False)
'''