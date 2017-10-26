Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.define "bot-metacritic-aws" do |host|
    host.vm.hostname = "bot-metacritic-aws"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "access_key_id"
    aws.secret_access_key = "secret_access_key"
    aws.session_token = "session_token"
    aws.keypair_name = "FINAL_KEY"
    aws.region= "us-west-2"
    aws.security_groups = [ 'botgrupo2' ]
    aws.instance_type= 't2.micro'

    aws.ami = "ami-19e92861"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "FINAL_KEY.pem"
  end

    config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansible_metacritic.yml"
    	ansible.force_remote_user= true
    	ansible.host_key_checking=false
  end


end
