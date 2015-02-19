# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "elk1" do |elk1|
    elk1.vm.box = "ubuntu/trusty64"
    elk1.vm.network "public_network", ip: "192.168.1.111", bridge:"eth0"
    config.vm.synced_folder "sharedKeys", "/vagrant/sharedKeys"
    config.vm.synced_folder "sharedFolder/elk/", "/vagrant"
  end
  
  config.vm.define "bastly1" do |atahualpa1|
    bastly1.vm.box = "ubuntu/trusty64"
    bastly1.vm.network "public_network", ip: "192.168.1.112", bridge:"eth0"
    config.vm.synced_folder "sharedKeys", "/vagrant/sharedKeys"
    config.vm.synced_folder "sharedFolder/atahualpa/", "/vagrant"
    bastly1.vm.provider "virtualbox" do |v|
        v.memory = 1024 
    end
  end

  config.vm.define "chaski1" do |chaski1|
    chaski1.vm.box = "ubuntu/trusty64"
    chaski1.vm.network "public_network", ip: "192.168.1.113", bridge:"eth0"
    config.vm.synced_folder "sharedKeys", "/vagrant/sharedKeys"
    config.vm.synced_folder "sharedFolder/chaski/", "/vagrant"
  end

  config.vm.provision :ansible do |ansible|
#    ansible.groups = {
#        "elk" => ["elk1"],
#        "pub" => ["pub1"],
#        "sub" => ["sub1"],
#        "log_gather" => ["pub1", "sub1"]
#    }
    ansible.verbose = "vvvv"
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    ansible.inventory_path = "ansible_static_inventory"
    config.ssh.forward_agent = true
  end

end
