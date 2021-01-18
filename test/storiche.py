import socket
import time
import threading
import queue as Queue


def worker(socket, stopper, rx_queue):
 """thread worker function"""
 message = ""
 while not stopper.is_set():

  data = client_socket.recv(512)


  if data == "":
   time.sleep(1)
  else:
   message = message + (data)

  if "END " in data:
    print("Message Received");
    rx_queue.put(message)
    message = ""

  return

###########################################
###########################################

if __name__ == "__main__":
  rx_queue =Queue.Queue() # create a Thread Safe Queue
  stopper = threading.Event() # create a Thread Safe Event

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(('localhost', 10003)) # connect to HISTORICAL DATA socket

  t = threading.Thread(target=worker, args=(client_socket, stopper, rx_queue ) )
  t.start()
  time.sleep( 5 )

  print("Wait for 15 seconds")
  time.sleep( 15 )

  #stopper.set() # force thread stop
  #t.join();


  t = threading.Thread(target=worker, args=(client_socket, stopper, rx_queue ) )
  t.start()
  time.sleep( 5 )
  
  print("Extract 1 hour candles")

  print("Extract EOD pricesfor last 5 years")
  cmd='CANDLE MSE 1250 86400\r\n'.encode()
  client_socket.send(cmd)
  time.sleep( 5 )

  print("Wait for 15 seconds")
  time.sleep( 15 )

  stopper.set() # force thread stop
  t.join();
  client_socket.close()

  f = open("MSE.txt", 'w')
  while not rx_queue.empty():
   message = rx_queue.get()
   f.write(message.decode('utf-8'))

  f.close()
  print("Done!")