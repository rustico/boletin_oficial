# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise64"
  config.vm.synced_folder ".", "/code"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y \ 
         python-dev \
         default-jre \
         git 
         
    cd /code
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python get-pip.py
    rm get-pip.py
    sudo pip install virtualenv
    virtualenv .venv

    source .env/bin/activate
    pip install -r requirements.txt

    echo "cd /code" >> /home/vagrant/.bashrc
    echo "source .venv/bin/activate" >> /home/vagrant/.bashrc
  SHELL

end
