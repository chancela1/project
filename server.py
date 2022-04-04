#!/usr/bin/env python3
import socket

def openServer(host,port,buffer=1024):
	serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serveur.bind(('', port)) # Écoute sur le port 50000
	serveur.listen(5)
	while True:
		client, infosClient = serveur.accept()
		print("Client connecté. Adresse " + infosClient[0])
		# Reçoit 1024 octets. Vous pouvez changer pour recevoir plus de données
		requete = client.recv(buffer)
		# decoder la reponse du client en utf-8
		print(requete.decode("utf-8"))
		reponse = "Connexion établie avec le serveur"
		client.send(reponse.encode("utf-8"))
		client.close()
		serveur.close()
if __name__ == "__main__":
	openServer('127.0.0.1', 50000)


