#!/bin/sh
sudo ansible-galaxy install -r requirements.txt --force
vagrant destroy -f 
vagrant up
python createAnsibleStaticInventory.py
ansible-playbook --inventory-file=./ansible_static_inventory site.yml --vvvv
