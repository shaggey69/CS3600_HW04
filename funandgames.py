with open ("/etc/shadow") as f:
	my_input = f.readlines()

for line in my_input:
	word = line.spit(":")
	if word[0] == "yourboss":
		boss_info  = word

print(word)

