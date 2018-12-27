#!/bin/bash

declare -a arr=("version" "auth" "list" "post" "clear" )

cmd=./somename.py
flags="-v"

for i in "${arr[@]}"
do
    echo `$cmd $flags $i`
    echo "---------------------"
done


