#!/usr/bin/env python
import json

associated_roles = {
    "dev":["node"], 
    "vim":["node"], 
    "webdev":["consulClient"], 
    "connectorrest":["consulClient", "node", "zeromq"], 
    "chaski":["consulClient", "node", "zeromq"], 
    "atahualpa":["consulClient", "node", "zeromq"]
}

groups = {}
ssh_keys_path = "./sshkeys/"
ssh_key_extension = ".key"

with open("terraform.tfstate") as fp:
    state = json.load(fp)

with open("hosts", "w") as inventory:
    for role, extra_roles in associated_roles.iteritems():
        for extra_role in extra_roles:
            groups[extra_role] = []
    for module in state["modules"]:
        for key, resource in module["resources"].iteritems():
            attributes = resource["primary"]["attributes"]
            groups[attributes["metadata.type"]] = []
    for module in state["modules"]:
        for key, resource in module["resources"].iteritems():
            #print key.split(".")
            resource_type, group_name = key.split(".")
            
            #print resource
            #index = int(index)
            attributes = resource["primary"]["attributes"]
            # print attributes
            for key2, res in attributes.iteritems():
                print key2, res
            groups[attributes["metadata.type"]].append(attributes["name"])
            if attributes["metadata.type"] in associated_roles.keys():
                for extra_role in associated_roles[attributes["metadata.type"]]:
                    groups[extra_role].append(attributes["name"])
                
    
           

            inventory.write("{} ansible_ssh_host={} ansible_ssh_user={} ansible_ssh_private_key_file={}{}{}\n".format(attributes["name"], attributes["access_ip_v4"], "root", ssh_keys_path, attributes["key_pair"], ssh_key_extension))

    #apply 
    for role, names in groups.iteritems():
        inventory.write("[{}]\n".format(role))
        for name in names:
            inventory.write("{}\n".format(name))
"""
    for group, hosts in groups.iteritems():
        fp.write("[{}]\n".format(group))
        for host, variables in hosts.iteritems():
            fp.write(host)
            for k, v in variables.iteritems():
                fp.write(" {}={}".format(k, v))
            fp.write("\n")
"""
