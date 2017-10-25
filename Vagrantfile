Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.define "bot-metacritic-aws" do |host|
    host.vm.hostname = "bot-metacritic-aws"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "ASIAIWJETZEM4GOBDK7A"
    aws.secret_access_key = "bu4ccod7eeQaHABs64ZqNPTWZC9AZ7K8eLgm6Qc1"
    aws.session_token = "FQoDYXdzEEsaDMBWtry54BjioOAipyKUAavl6ARVbmENIIUnOIny7g2Oj57m9dhBt85uuVRH7YAmlDdTD5r/wWjUu0/rRsSgaQV1KtsLzM6dPQpPpR9n8S8I0ARluhzA0WhMmi6jZk05JVlxVTIvIulgBGm9o5r4rU82BorImeEDA4k+CFhWK6GjsIG8tpdaodL0WRJy7wQDw+K0UaWMMDXoRIUpAw87RUmY2RUoz6PDzwU="
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
