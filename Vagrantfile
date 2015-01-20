# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.define "pub1" do |pub1|
    pub1.vm.box = "ubuntu/trusty64"
    pub1.vm.network "private_network", type: "dhcp"
  end

  config.vm.define "sub1" do |sub1|
    sub1.vm.box = "ubuntu/trusty64"
    sub1.vm.network "private_network", type: "dhcp"
  end

  config.vm.define "elk1" do |elk1|
    elk1.vm.box = "ubuntu/trusty64"
    elk1.vm.network "private_network", type: "dhcp"
  end

  config.vm.provision :ansible do |ansible|
    ansible.groups = {
        "elk" => ["elk1"],
        "pub" => ["pub1"],
        "sub" => ["sub1"]
    }
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    config.ssh.forward_agent = true
  end

end
