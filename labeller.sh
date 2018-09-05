#!/bin/bash
read -p 'What is the 1 class? ' one
mkdir $one
read -p 'What is the 0 class? ' zero
mkdir $zero
counter1=0
counter0=0
for f in *.png
do
if [[ "$f" == "1__"* ]];then
counter1=$((counter1+1))
mv "$f" "$one"
elif [[ "$f" == "0__"* ]];then
counter0=$((counter0+1))
mv "$f" "$zero"
fi
done
echo $counter1 files moved to $one
echo $counter0 files moved to $zero 
