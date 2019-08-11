import socket
from Printer import dictPrinter
mealDict = {1:"Breakfast", 2:"Lunch", 3:"Dinner"}
cuisineDict = {1:"African", 2:"British", 3:"Chinese", 4:"French", 5:"Fast Food", 6:"Indian", 7:"Italian", 8:"Japanese", 9:"Korean", 10:"Lebanese", 11:"Mexican", 12:"Turkish"}
def Main():
    #connection to ChatBot 
    host = '127.0.0.1'
    port = 50091
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
    #Reading first message to ChatBot
    nameIntro = thisSocket.recv(1024).decode()
    print('Message Received from ChatBot: '+ str(nameIntro))
    #client name
    message = raw_input("Message to  ChatBot: ")
    #Continue conversation with ChatBot until end is types
    while message != "end":
    #send message to Chatbot
                        thisSocket.send(message.encode())
                        #Receive Message from ChatBot
                        RMess = thisSocket.recv(1024).decode()
                        #Print message from ChatBot
                        print("Message Received from ChatBot: "+ str(RMess) + "\n")
                        #print mealDict
                        dictPrinter(mealDict)
                        #choose meal
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        #choose cuisine
                        cuisineChoice = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(cuisineChoice))
                        dictPrinter(cuisineDict)
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        #does price matter?
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(message))
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(message))
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        #does rating matter
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(message))
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(message))
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        #recieve list of final restaurants
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: "+ str(message))
                        #End or repeat
                        message = thisSocket.recv(1024).decode()
                        print("Message Received from ChatBot: " + str(message))
                        message = raw_input("Message to  ChatBot: ")
                        thisSocket.send(message.encode())
                        message = thisSocket.recv(1024).decode()
                        if message == "end":
                            break
                        elif message == "repeat":
                            continue
                            
    #Close Socket
    thisSocket.close()
    #Display conversation is over
    print("Conversation between user and ChatBot Ended")
#Check if running directly from this file
if __name__ == '__main__':
    Main()
    

