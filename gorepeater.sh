prefix="https://"
if [ "$#" -lt 2 ]; then
    echo "need file, wordlist and (optional) prefix" 
    exit 1
fi

if [ "$#" -eq 2 ]; then
    prefix=$3
fi

mkdir ~/gobusterout
while read in; do ./gobuster -w $2 -u $prefix$in -k > ~/gobusterout/$in ; done < $1
