from jinja2 import Template
import yaml

templateVirtualBox = Template(open('templates/ansible_static_inventory.j2').read())
datavars = yaml.load(open("vagrantConfig.yml").read())

output =  templateVirtualBox.render(datavars)

with open("ansible_static_inventory", "wb") as fh:
    fh.write(output)
