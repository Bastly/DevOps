# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

settings = YAML.load_file 'vagrantConfig.yml'

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "elk1" do |elk1|
    elk1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    elk1.vm.synced_folder "sharedFolder/elk/", "/vagrant"
    elk1.vm.box = "ubuntu/trusty64"
    elk1.vm.network "public_network", ip: settings['elk1']['ip'], bridge: settings['bridge']
    elk1.vm.provider "virtualbox" do |v|
      v.memory = 1024 
    end
  end

  config.vm.define "orion1" do |orion1|
    orion1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    orion1.vm.synced_folder "sharedFolder/orion/", "/vagrant"
    orion1.vm.box = "nrel/CentOS-6.5-x86_64"
    orion1.vm.network "public_network", ip: settings['orion1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "redis1" do |redis1|
    redis1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    redis1.vm.synced_folder "sharedFolder/orion/", "/vagrant"
    redis1.vm.box = "ubuntu/trusty64"
    redis1.vm.network "public_network", ip: settings['redis1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "curaca1" do |curaca1|
    curaca1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    curaca1.vm.synced_folder "sharedFolder/orion/", "/vagrant"
    curaca1.vm.box = "ubuntu/trusty64"
    curaca1.vm.network "public_network", ip: settings['curaca1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "consul1" do |consul1|
    config.vm.synced_folder "sharedFolder/consul/", "/vagrant"
    consul1.vm.box = "ubuntu/trusty64"
    consul1.vm.network "public_network", ip: settings['consul1']['ip'], bridge: settings['bridge']
  end
  
  config.vm.define "atahualpa1" do |atahualpa1|
    atahualpa1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    atahualpa1.vm.synced_folder "sharedFolder/atahualpa/", "/vagrant"
    atahualpa1.vm.box = "ubuntu/trusty64"
    atahualpa1.vm.network "public_network", ip: settings['atahualpa1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "chaski1" do |chaski1|
    config.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    config.vm.synced_folder "sharedFolder/chaski/", "/vagrant"
    chaski1.vm.box = "ubuntu/trusty64"
    chaski1.vm.network "public_network", ip: settings['chaski1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "chaski2" do |chaski2|
    config.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    config.vm.synced_folder "sharedFolder/chaski/", "/vagrant"
    chaski2.vm.box = "ubuntu/trusty64"
    chaski2.vm.network "public_network", ip: settings['chaski2']['ip'], bridge: settings['bridge']
  end


  config.vm.define "consul1" do |consul1|
    config.vm.synced_folder "sharedFolder/consul/", "/vagrant"
    consul1.vm.box = "ubuntu/trusty64"
    consul1.vm.network "public_network", ip: settings['consul1']['ip'], bridge: settings['bridge']
  end

  config.vm.define "connector1" do |connector1|
    config.vm.synced_folder "sharedFolder/connector-rest/", "/vagrant"
    connector1.vm.box = "ubuntu/trusty64"
    connector1.vm.network "public_network", ip: settings['connector1']['ip'], bridge: settings['bridge']
  end

  config.vm.provision :ansible do |ansible|
    ansible.verbose = "vvvv"
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    ansible.inventory_path = "ansible_static_inventory"
    config.ssh.forward_agent = true
  end
end
