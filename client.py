
#!/usr/bin/env python3
import socket
import datetime
def openClientTunnel(host,port,buffer=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connexion au serveur de M1ISI – M1SSI")
    print(f'Connexion faite à: {datetime.datetime.now()}')
    print(f'Connexion faite via le port: {port} à l\'adresse: {host}')
    # Customer send message to server
    client.send("Bonjour, je suis le client".encode("utf-8"))
    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    print("Connexion fermée")
    client.close()
if __name__ == '__main__':
    openClientTunnel("127.0.0.1", 50000)
