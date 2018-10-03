import sys
if len(sys.argv) != 3:
	print "need file and port"
else:
	r = open(sys.argv[1])
	w = open("result"+sys.argv[1],"w")
	for line in r:
		towrite = ""
		if int(sys.argv[2]) == 80:
			towrite = "http://"
		else:
			towrite = "https://"
		towrite += line[:-1]
		if int(sys.argv[2]) != 80 and int(sys.argv[2]) != 443:
			towrite += ":"+str(sys.argv[2])
		w.write(towrite+"\n")
