import sys

def parsekeyfile(tomodify,f):
	for line in f:
        	colin=line.strip().find(':')
        	if colin == -1:
                	print f.name + "file not formatted correctly"
               		exit()
       		tomodify[line.strip()[:colin]] = line.strip()[colin+1:]

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
	cracked = ""
	data = line.strip().split(':')
	hashes = []
	for a in data:
		if len(a) == 32: #hashes are of len 32
			hashes.append(a)
	for a in hashes:
		if a in keys:
			cracked = keys[a]+":(NTLM):"
		lmdata1 = a[:16] #LM hashes are broken up in 16 length
		lmdata2 = a[16:]
		if cracked == "" and lmdata1 in lm and lmdata2 in lm:
			cracked = lm[lmdata1] + lm[lmdata2] + ":(LM):" 
	if cracked != "":
		keysreplaced = keysreplaced + 1
	result.write(cracked+line)

print "completed.",keysreplaced," values replaced"
