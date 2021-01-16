import socket
import sys
import threading
import time

from random import randint

# Definizione del lock
threadLock = threading.Lock()
class IlMioThread (threading.Thread):
   def __init__(self, nome, durata):
      threading.Thread.__init__(self)
      self.nome = nome
      self.durata = durata
   def run(self):
     #  print ("Thread '" + self.name + "' avviato")
      # Acquisizione del lock
      time.sleep(5)
      while True:
        sock.sendall('SUB TSLA\r\n'.encode())
        #time.sleep(1)
        sock.sendall('UNS TSLA\r\n'.encode())
       # time.sleep(1)
      #   print ("Thread '" + self.name + "' terminato")
      # Rilascio del lock
      #  threadLock.release()

# Creazione dei thread
thread1 = IlMioThread("Thread#1", randint(1,5))


# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10001))
amount_received = 0;

while True:
    data = sock.recv(1000)
    if data:
        pippo=data.decode('utf-8')
        pippo.replace('\r\n','')
        pluto=pippo.split(';')
         # Avvio dei thread
        if pluto[0]=='DARWIN_STATUS':
            print(pluto[0],pluto[1],pluto[2])
            thread1.start()
        if pluto[0]=='ANAG':
            dollari=str(float(pluto[5])*1.21)
            print(pluto[2],'   Titolo =',pluto[1],'   Valore EUR',pluto[5], 'Valore USD',dollari)
# Join
thread1.join()


