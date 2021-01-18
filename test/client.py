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
      time.sleep(5)
      while True:
        sock.sendall('SUBPRZ SFER\r\n'.encode())
        sock.sendall('UNS SFER\r\n'.encode())

# Creazione dei thread
thread1 = IlMioThread("Thread#1", randint(1,5))

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10001))


while True:
    data = sock.recv(1000)
    if data:
        dataString=data.decode('utf-8').replace('\r\n','').split(';')
         # Avvio dei thread
        if dataString[0]=='DARWIN_STATUS':
            print(dataString[0],dataString[1],dataString[2])
            thread1.start()
        if dataString[0]=='ANAG':
            dollari=str(float(dataString[5])*1.21)
            print(dataString[2],'   Titolo =',dataString[1],'   Valore EUR',dataString[5], 'Valore USD',dollari)
# Join
thread1.join()


