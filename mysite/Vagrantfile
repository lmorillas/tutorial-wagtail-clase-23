# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-22.04"
    # puertos host y máquina virtualizada
    config.vm.network :forwarded_port, host: 8080, guest: 80
    config.vm.network :forwarded_port, host: 5432, guest: 5432
    # config.vm.synced_folder './', '/vagrant', SharedFoldersEnableSymlinksCreate: false
    # require plugin https://github.com/leighmcculloch/vagrant-docker-compose
    config.vagrant.plugins = "vagrant-docker-compose"
    
    # copiamos la carpeta de los estáticos dentro de la máquina. 
    # Para usar rsync, tiene que estar instalado en el host
    # https://learn.microsoft.com/en-us/windows/wsl/install

    # config.vm.provision "file", source: "./web", destination: "/home/vagrant/web"
    # config.vm.synced_folder "./web", "/home/vagrant/web", type: "rsync"  #, rsync__exclude: ".git/"
    # install docker and docker-compose
    config.vm.provision :docker
    config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", rebuild: true, run: "always"
    # config.vm.provision :shell, path: "provision.sh"  
  end
  