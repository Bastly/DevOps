sudo ansible-galaxy install -r requirements.txt --force
sudo apt-get install redis-server
sudo service redis-server stop
sudo service redis-server start
wget https://bootstrap.pypa.io/get-pip.py 
sudo python get-pip.py
sudo pip install redis
sudo pip install Jinja2

TO CREATE A NEW ROLE (RECIPE) FOR ANSIBLE GALAXY
ansible-galaxy init rolename


--- useful commands for chaski1 ----
sudo tail -f /var/log/chaski-socketio.log /var/log/chaski-zeromq.log /var/log/nodejs/chaski.log /var/log/nodejs/chaskiSocketio.log | sed 's/\\n/\n/g'


--- useful commands for atahualpa1 ----
sudo tail -f /var/log/nodejs/atahualpa.log /var/log/nodejs/connector-rest.log /var/log/atahualpa.log | sed 's/\\n/\n/g'
