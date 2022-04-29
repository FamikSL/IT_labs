if [ $HOME = $(pwd) ]
then 
    echo $HOME
    exit 0
else
    echo 'Ошибка'
    exit 1
fi