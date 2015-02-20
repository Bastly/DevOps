sudo ansible-galaxy install -r requirements.txt --force
sudo apt-get install redis-server
sudo service redis-server stop
sudo service redis-server start
wget https://bootstrap.pypa.io/get-pip.py 
sudo python get-pip.py
sudo pip install redis

TO CREATE A NEW ROLE (RECIPE) FOR ANSIBLE GALAXY
ansible-galaxy init rolename