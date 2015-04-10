#!/bin/bash
cd ~/Works/mgl/bastly/infra/DevOps/
vagrant up consul1 chaski1 webdev1 atahualpa1 
gnome-terminal -x sh -c "vagrant ssh chaski1" -t chaski1
gnome-terminal -x sh -c "vagrant ssh chaski1" -t chaski1
gnome-terminal -x sh -c "vagrant ssh chaski1" -t chaski1

gnome-terminal -x sh -c "vagrant ssh atahualpa1" -t atahualpa1
gnome-terminal -x sh -c "vagrant ssh atahualpa1" -t atahualpa1
gnome-terminal -x sh -c "vagrant ssh atahualpa1" -t atahualpa1

gnome-terminal -x sh -c "vagrant ssh webdev1" -t webdev1
gnome-terminal -x sh -c "vagrant ssh webdev1" -t webdev1
gnome-terminal -x sh -c "vagrant ssh webdev1" -t webdev1
cd -
