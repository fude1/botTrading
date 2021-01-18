import socket
import time
import threading
import queue as Queue


def worker(socket, stopper, rx_queue):
 """thread worker function"""
 message = ""

 # while not rx_queue.empty():
  # message = rx_queue.get()
 # f.write(message.decode('utf-8'))
pippo=1
 while True:
  data = client_socket.recv(512)

  print(data.decode('utf-8').replace('\r\n','\r'))
  f = open("storico.txt", 'a')
  pippo=data.decode('utf-8').replace('\r\n','\r')

  f.write(pippo)
  f.close()
  # message = message + (data.decode('utf-8')
  if "END " in data.decode('utf-8'):
    print("Message Received");
    rx_queue.put(message)
    message = ""

  #f = open("book.txt", 'a')
  #f.write(data.decode('utf-8'))
  #f.close()
 # if b'\r\n' in data:
   # message=message.replace('\r\n',',')
   # message=message.replace(', ',',')
   # print(message.split(','))
  
    #message = "" 
  # pippo=dataString.split(',')
  # pluto=dataString.split(';')
 
  #print(pluto)
 #   print(data.decode('utf-8').split(';'))
 #   dataString=data.decode('utf-8').replace('\r\n',';').split(';')
  #  if dataString[0]=='BOOK_15':
  #    print(dataString[2],'Book   Titolo =',dataString[1],' ',dataString[3],dataString[4],dataString[5],dataString[6],dataString[7],dataString[8],dataString[9],dataString[10],dataString[11],dataString[12])
  #  if dataString[0]=='BOOK_20':
  #    print(dataString[2],'Book   Titolo =',dataString[1],' ',dataString[3],dataString[4],dataString[5],dataString[6],dataString[7],dataString[8],dataString[9],dataString[10],dataString[11],dataString[12])
  #  if dataString[0]=='PRICE':
  #    dollari=str(float(dataString[5])*1.21)
  #  #    if dataString[1]=='ITW':
   #    print(dataString[2],'   Titolo =',dataString[1],'   Valore EUR',dataString[5], '   Target EUR 0,850')
  #    if dataString[1]=='SFER':
   #     print(dataString[2],'   Titolo =',dataString[1],'   Valore EUR',dataString[5], '   Target EUR 15,50')
  #else:
  # message = message + (data)

  #if "END " in data:
  #  print("Message Received");
  #  rx_queue.put(message)
  #  message = ""

   # return

###########################################
###########################################

if __name__ == "__main__":
  rx_queue =Queue.Queue() # create a Thread Safe Queue
  stopper = threading.Event() # create a Thread Safe Event

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(('localhost', 10003)) # connect to HISTORICAL DATA socket

  t = threading.Thread(target=worker, args=(client_socket, stopper, rx_queue ) )
  t.start()
  time.sleep( 10 )
 
   #print("Extract 1 hour candles")
   #print("Extract TSLA pricesfor last 5 years")
  client_socket.send('CANDLE PDD 1250 86400\r\n'.encode())
  while True:
   # client_socket.send('SUB SFER\r\n'.encode())
   # client_socket.sendall('UNS SFER\r\n'.encode())
    time.sleep( 60 )
    
   


  #print("Wait for 15 seconds")
  #time.sleep( 5 )
  #cmd=('UNS SFER\r\n'.encode())
  #client_socket.send(cmd)

  #stopper.set() # force thread stop
  #t.join();
 # client_socket.close()

  #f = open("MSE.txt", 'w')
 # while not rx_queue.empty():
  # message = rx_queue.get()
  # f.write(message.decode('utf-8'))

  #f.close()
  print("Done!")