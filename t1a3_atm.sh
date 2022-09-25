#!/bin/bash
# if [ -x "$(command -v reuqirements.txt)" ]; then
#   echo 'Will install requirements.txt.' >&2
#   pip install -r requirements.txt
# fi

# if [[ -x "$(command -v python)" ]]
# then
#     pyv="$(python -V 2>&1)"
#     if [[ $pyv == "Python 3"* ]]
#     then
#         python3 main.py $1
#     else
#         echo "You don't have Python 3.x version of python, please, sort it out!" >&2
#     fi 
# else
#     echo "You don't have python! please, install if first!" >&2
# fi

printf 'Authorisation required for activating virtual environment and download: \n'
cat requirements.txt
echo "Do you authorise to proceed? [Y,n]"
read input
if [[ $input == "Y" || $input == "y" ]]; then
    echo "Creaing & Activaing Virtual Environment..."
    python3 -m venv .venv 
    source .venv/bin/activate
    echo "Installing packages..."
    pip install -r requirements.txt
    python3 main.py $1
    exit 0
else
    echo "Program terminating"
    exit 1
fi
