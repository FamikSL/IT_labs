#!/bin/bash
if [[ $1 > $2 ]];
then max=$1;
else max=$2;
fi

if [[ $max > $3 ]];
then echo $max
else echo $3
fi