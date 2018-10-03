import sys
import re
if len(sys.argv) != 3:
        print "need in and out file"
else:
        r = open(sys.argv[1])
        w = open(sys.argv[2],"w")
        for line in r:
                if line[:4] == "Nmap":
                        found = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
                        down = re.search("host down",line)
			if found and not down:
                                w.write(line[found.start():found.end()] + "\n")

