#!/bin/sh
sudo ansible-galaxy install -r requirements.txt --force
vagrant destroy -f 
python createAnsibleStaticInventory.py
vagrant up
