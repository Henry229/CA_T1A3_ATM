#!/bin/bash

printf 'Will show you a package list : \n'
cat requirements.txt
echo "Do you want to proceed? (y,n)"
read input
if [[ $input == "Y" || $input == "y" ]]; then
    echo ">>>>> Creaing  Virtual Environment..."
    python3 -m venv .venv 
    echo "***** Activaing Virtual Environment..."
    source .venv/bin/activate
    echo "Installing packages..."
    pip install -r requirements.txt
    python3 main.py $1
    exit 0
else
    echo "Script will be terminated"
    exit 1
fi
