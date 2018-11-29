import sys

if len(sys.argv) != 3:
	print "need a hash file and a key file"
	exit()

hash = open(sys.argv[1])
key = open(sys.argv[2])
result = open("result.txt","w")
keysreplaced = 0

keys = {}
for line in key:
	colin=line.find(':')
	if colin == -1:
		print "key file not formatted correctly"
		exit()
	keys[line[:colin]] = line[colin+1:]

for line in hash:
	replaced = False
	for elem,val in keys.items():
		if not replaced and line.find(elem) != -1:
			replaced = True
			result.write(line[:-1]+":"+val)
			keysreplaced = keysreplaced + 1
	if not replaced:
		result.write(line)

print "completed.",keysreplaced," values replaced"
