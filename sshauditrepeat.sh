prefix="https://"
if [ "$#" -eq 0 ]; then
    echo "need file"
    exit 1
fi

mkdir ~/ssh-audit 
while read in; do proxychains python ~/tools/ssh-audit/ssh-audit.py $in > ~/ssh-audit/$in ; done < $1
