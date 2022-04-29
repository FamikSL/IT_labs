while true
do
    read string
    all_strings+=" ${string}"
    if [[ $string = 'Guzaerov' ]];
    
    then
        echo $all_strings
        break;
    fi
done