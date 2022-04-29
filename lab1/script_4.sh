count=0
while true
do
    read number
    let count+=1
    if [ $(($number%2)) = 0 ]
    
    then
        echo $count
        break;
    fi
done