#!/bin/bash

star() {
        for((i=1; i<=rows; i+=2))
        do
                for((j=rows-i; j>=0; j--))
                do
                         echo -n "* "
                done
        echo
        done
        }

read -p "Insert Odd number " rows
if [ $((rows%2)) -eq 0 ]
then
  echo "This is even number, please insert Odd number for star output."
else
  star
fi