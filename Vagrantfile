# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.define "elk1" do |elk1|
    elk1.vm.box = "ubuntu/trusty64"
    elk1.vm.network "private_network", type: "dhcp"
  end

  config.vm.define "dev1" do |dev1|
    dev1.vm.box = "ubuntu/trusty64"
    dev1.vm.network "private_network", type: "dhcp"
  end


  config.vm.provision :ansible do |ansible|
    ansible.groups = {
        "elk" => ["elk1"],
        "dev" => ["dev1"]
    }
    ansible.playbook = "site.yml"
  end

end
