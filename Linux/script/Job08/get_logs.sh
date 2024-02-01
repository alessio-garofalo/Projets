#!/bin/bash
date=$(date +"%d-%m-%Y-%H-%M")

last -5 alessio | wc -l > backup/number_connection-$date.txt
last -5 alessio >> backup/number_connection-$date.txt
tar -cf backup/number_connection-$date.tar number_connection-$date.txt

rm number_connection-$date.txt
