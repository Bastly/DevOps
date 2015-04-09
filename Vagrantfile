# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

settings = YAML.load_file 'vagrantConfig.yml'

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  if settings['provider'] == 'openstack'
    config.ssh.username       = ''
    config.ssh.forward_agent  = true
    config.ssh.private_key_path = './sshkeys/openstack.key'
  end

  config.vm.define "elk1" do |elk1|
    elk1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
    elk1.vm.synced_folder "sharedFolder/elk/", "/vagrant"
    elk1.ssh.username = 'vagrant'
    if settings['provider'] == 'openstack'
      elk1.ssh.username = 'ubuntu'
      elk1.vm.box = 'boxes/openstack'
      elk1.vm.provider :openstack do |os|
        os.openstack_auth_url = 'http://192.168.1.201:5000/v2.0/tokens'
        os.username           = 'deployer'
        os.password           = 'deployer'
        os.tenant_name        = 'deployment'
        os.flavor             = 'm1.small'
        os.image              = 'ubuntu'
        os.keypair_name       = 'openstack'
        os.public_key_path    = './sshkeys/openstack.key.pub'
        os.floating_ip        = settings['elk1']['ip']
      end
    else
      elk1.vm.box = "ubuntu/trusty64"
      elk1.vm.network "public_network", ip: settings['elk1']['ip'], bridge: settings['bridge']
      elk1.vm.provider "virtualbox" do |v|
        v.memory = 1024 
      end
    end
  end

  # config.vm.define "orion1" do |orion1|
  #   orion1.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
  #   orion1.vm.synced_folder "sharedFolder/orion/", "/vagrant"
  #   orion1.ssh.username = 'centos'
  #   if settings['provider'] == 'openstack'
  #     orion1.vm.box = 'boxes/openstack'
  #     orion1.ssh.pty = true
  #     orion1.vm.provider :openstack do |os|
  #       os.openstack_auth_url = 'http://192.168.1.201:5000/v2.0/tokens'
  #       os.username           = 'deployer'
  #       os.password           = 'deployer'
  #       os.tenant_name        = 'deployment'
  #       os.flavor             = 'm1.small'
  #       os.image              = 'Centos6'
  #       os.keypair_name       = 'openstack'
  #       os.public_key_path    = './sshkeys/openstack.key.pub'
  #       os.floating_ip        = settings['orion1']['ip']
  #     end
  #   else
  #     orion1.vm.box = "nrel/CentOS-6.5-x86_64"
  #     orion1.vm.network "public_network", ip: settings['orion1']['ip'], bridge: settings['bridge']
  #   end
  # end
  
  # config.vm.define "atahualpa1" do |atahualpa1|
  #   # atahualpa1.vm.box = "ubuntu/trusty64"
  #   # atahualpa1.vm.network "public_network", ip: settings['atahualpa1']['ip'], bridge: settings['bridge']
  #   config.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
  #   config.vm.synced_folder "sharedFolder/atahualpa/", "/vagrant"
  #   atahualpa1.vm.provider :openstack do |os|
  #     os.openstack_auth_url = 'http://192.168.1.201:5000/v2.0/tokens'
  #     os.username           = 'deployer'
  #     os.password           = 'deployer'
  #     os.tenant_name        = 'deployment'
  #     os.flavor             = 'm1.small'
  #     os.image              = 'ubuntu'
  #     os.keypair_name       = 'openstack'
  #     os.public_key_path    = './sshkeys/openstack.key.pub'
  #     os.floating_ip        = settings['atahualpa1']['ip']
  #   end
  # end

  # config.vm.define "chaski1" do |chaski1|
  #   # chaski1.vm.box = "ubuntu/trusty64"
  #   # chaski1.vm.network "public_network", ip: settings['chaski1']['ip'], bridge: settings['bridge']
  #   config.vm.synced_folder "sharedKeys", "/vagrant2/sharedKeys"
  #   config.vm.synced_folder "sharedFolder/chaski/", "/vagrant"
  #   chaski1.vm.provider :openstack do |os|
  #     os.openstack_auth_url = 'http://192.168.1.201:5000/v2.0/tokens'
  #     os.username           = 'deployer'
  #     os.password           = 'deployer'
  #     os.tenant_name        = 'deployment'
  #     os.flavor             = 'm1.small'
  #     os.image              = 'ubuntu'
  #     os.keypair_name       = 'openstack'
  #     os.public_key_path    = './sshkeys/openstack.key.pub'
  #     os.floating_ip        = settings['chaski1']['ip']
  #   end
  # end


  # config.vm.define "webdev1" do |webdev1|
  #   # webdev1.vm.box = "ubuntu/trusty64"
  #   # webdev1.vm.network "public_network", ip: settings['webdev1']['ip'], bridge: settings['bridge']
  #   config.vm.synced_folder "sharedFolder/webdev/", "/vagrant"
  #   webdev1.vm.provider :openstack do |os|
  #     os.openstack_auth_url = 'http://192.168.1.201:5000/v2.0/tokens'
  #     os.username           = 'deployer'
  #     os.password           = 'deployer'
  #     os.tenant_name        = 'deployment'
  #     os.flavor             = 'm1.small'
  #     os.image              = 'ubuntu'
  #     os.keypair_name       = 'openstack'
  #     os.public_key_path    = './sshkeys/openstack.key.pub'
  #     os.floating_ip        = settings['webdev1']['ip']
  #   end
  # end

  config.vm.provision :ansible do |ansible|
    ansible.verbose = "vvvv"
    ansible.playbook = "site.yml"
    ansible.host_key_checking = false
    ansible.inventory_path = "ansible_static_inventory"
    config.ssh.forward_agent = true
  end

end
