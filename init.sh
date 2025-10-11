#!/usr/bin/bash

if [ ! -d 'ven' ]; then

    virtualenv ven
fi
source ven/bin/activate
pip install -r requirements.txt
python3 main.py

  git config --global user.email "begreat5333@gmail.com"
  git config --global user.name "be-great"