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
	
for line in my_input:
	word = line.split(":")
	if word[0] == "yourboss":
		boss_password  = (word[1])
	exit

print(findWord(my_dict.split(),boss_password))


for line in my_input:
	word = line.split(":")
	if word[0] == "sysadmin":
		sys_admin_password  = (word[1])
	exit

print(findWord(my_dict.split(),sys_admin_password))




'''
subprocess.run(args, *, stdin=None, input=None, stdout=None,
stderr=None, shell=False, timeout=None, check=False)
'''