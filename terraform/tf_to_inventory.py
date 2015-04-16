#!/usr/bin/env python
import json

hosts = {}
groups = {}

with open("terraform.tfstate") as fp:
    state = json.load(fp)

for module in state["modules"]:
    for key, resource in module["resources"].iteritems():
        print key.split(".")
        resource_type, group_name = key.split(".")
        
        print resource
        #index = int(index)
        attributes = resource["primary"]["attributes"]
        print attributes
        for key2, res in attributes.iteritems():
            print key2, res
        name = attributes["name"]

        if attributes["status"] == "active":
            hosts[name] = attributes["ipv4_address"]
            #groups.setdefault(group_name, {})[name] = { "index": index, "nz_index": index + 1, }

with open("hosts", "w") as fp:
    for host, ip_address in hosts.iteritems():
        fp.write("{} ansible_ssh_host={} ansible_ssh_user=root\n".format(host, ip_address))

    for group, hosts in groups.iteritems():
        fp.write("[{}]\n".format(group))
        for host, variables in hosts.iteritems():
            fp.write(host)
            for k, v in variables.iteritems():
                fp.write(" {}={}".format(k, v))
            fp.write("\n")
