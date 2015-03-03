#!/bin/sh
sudo ansible-galaxy install -r requirements.txt --force
vagrant destroy -f 
vagrant up
