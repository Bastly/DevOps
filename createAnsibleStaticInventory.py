from jinja2 import Template
import yaml

template = Template(open('templates/ansible_static_inventory.j2').read())
datavars = yaml.load(open("vagrantConfig.yml").read())

output =  template.render(datavars)

with open("ansible_static_inventory", "wb") as fh:
    fh.write(output)
