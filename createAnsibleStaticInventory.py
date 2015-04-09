from jinja2 import Template
import yaml

templateVirtualBox = Template(open('templates/ansible_static_inventory_virtualbox.j2').read())
templateOpenStack = Template(open('templates/ansible_static_inventory_openstack.j2').read())
datavars = yaml.load(open("vagrantConfig.yml").read())

if datavars['provider'] == 'openstack' :
    print 'openstack template loaded'
    output =  templateOpenStack.render(datavars)
else :
    print 'virtualbox template loaded'
    output =  templateVirtualBox.render(datavars)

with open("ansible_static_inventory", "wb") as fh:
    fh.write(output)
