if [ $# -ne 2 ]
then 
    exit 1
fi
if [ $1 = 'crypt' ]
then 
    echo $2 | base64 
    exit 0
fi
if [ $1 = 'decrypt' ]
then 
     echo $2 | base64 --decode
    exit 0
else
    exit 2
fi