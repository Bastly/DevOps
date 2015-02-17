# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "elk1" do |elk1|
    elk1.vm.box = "ubuntu/trusty64"
    elk1.vm.network "public_network", ip: "192.168.1.111", bridge:"wlan2"
  end
  
  config.vm.define "bastly1" do |bastly1|
    pub1.vm.box = "ubuntu/trusty64"
    pub1.vm.network "public_network", ip: "192.168.1.112", bridge:"wlan2"
    pub1.vm.provider "virtualbox" do |v|
        v.memory = 1024 
    end
  end

  config.vm.define "chaski1" do |chaski1|
    sub1.vm.box = "ubuntu/trusty64"
    sub1.vm.network "public_network", ip: "192.168.1.113", bridge:"wlan2"
  end

  config.vm.provision :ansible do |ansible|
#    ansible.groups = {
#        "elk" => ["elk1"],
#        "pub" => ["pub1"],
#        "sub" => ["sub1"],
#        "log_gather" => ["pub1", "sub1"]
#    }
    ansible.verbose = "vvv"
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    ansible.inventory_path = "ansible_static_inventory"
    config.ssh.forward_agent = true
  end

end
