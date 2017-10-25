vagrant up --provider=aws

fab -i FINAL_KEY.pem -H ubuntu@DNS instalar_bot
fab -i FINAL_KEY.pem -H ubuntu@DNS bot_up

#Cambiar FINAL_KEY.pem por el archivo correspondiente de AWS
#Cambiar DNS por el correspondiente del a instancia creada con Vagrant
