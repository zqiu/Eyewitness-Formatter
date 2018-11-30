import sys

def parsekeyfile(tomodify,f):
	for line in f:
        	colin=line.find(':')
        	if colin == -1:
                	print f.name + "file not formatted correctly"
               		exit()
       		tomodify[line[:colin]] = line[colin+1:]


if len(sys.argv) != 3 and len(sys.argv) != 4:
	print "need a hash file and a key file (optionally LMkey file)"
	exit()

hash = open(sys.argv[1])
key = open(sys.argv[2])
result = open("result.txt","w")
keysreplaced = 0

keys = {}
parsekeyfile(keys,key)

lm = {}
if len(sys.argv) == 4:
	lmfile = open(sys.argv[3])
	parsekeyfile(lm,lmfile)

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
