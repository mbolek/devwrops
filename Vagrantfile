# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.boot_timeout = 300
  config.vm.provision :shell do |s|
    s.inline = "apt-get install -y python"
  end

   config.vm.network "forwarded_port", guest: 9090, host: 9090 #prometheus port
   config.vm.network "forwarded_port", guest: 9093, host: 9093 #alertmanager port
   config.vm.network "forwarded_port", guest: 9100, host: 9100 #node_exporter port
   config.vm.network "forwarded_port", guest: 3000, host: 3000 #grafana port
   config.vm.network "forwarded_port", guest: 8081, host: 8081 #cAdvisor port
   config.vm.network "forwarded_port", guest: 9101, host: 9101 #haproxy_exporter port
   config.vm.network "forwarded_port", guest: 9121, host: 9121 #redis_exporter port
   config.vm.network "forwarded_port", guest: 9115, host: 9115 #blackbox_exporter port

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    #ansible.verbose = "vvv"
    ansible.limit = 'all' #very important for multimachine tests
  end
end
