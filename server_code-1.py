def Main():
    
    mealDict = {1:"Breakfast", 2:"Lunch", 3:"Dinner", 4:"Other"}
    cuisineDict = {1:"African", 2:"British", 3:"Chinese", 4:"French", 5:"Fast Food", 6:"Indian", 7:"Italian", 8:"Japanese", 9:"Korean", 10:"Lebanese", 11:"Mexican", 12:"Turkish", 13:"Other"}
    mealList = {"Breakfast":{"The Spon Gate", "Rix's Bombay Cafe Bar", "The Ocean", "Cafe Rouge", "Millie's Kitchen", "Horse and Jockey", "Ristorante Da Vinci", "Cafe Italiano", "Chiquito", "Hummus House", "Mister M's Tradition Fish & Chips", "Ate Til Ate"}, "Lunch":{"A.G.G African Restaurant & Bar", "Anedo Finger Licking Restaurant & Bar", "Chi Bar", "Turmeric Gold", "The Spon Gate", "Nima's", "Rixs Bombay cafe bar", "The Ocean", "Cafe Rouge", "Millie's Kitchen", "Rising Cafe - From the Rubble", "The Old Crown", "Miller and Carter", "Horse and Jockey", "Ristorante Da Vinci", "Cafe Italiano", "Etna", "Las Iguanas", "Selmina's Restaurant and Bar", "Chiquito", "Hummus House UK", "Anatalya Restaurant", "Pasha Turkey Restaurant", "Mister M's Traditional Fish & Chips", "Ate Til Ate", "City Chippy", "Al Bader"}, "Dinner":{"A.G.G African Restaurant & Bar", "Anedo Finger Licking Restaurant & Bar", "Chi Bar", "Turmeric Gold", "The Spon Gate", "Nima's", "Rixs Bombay cafe bar", "The Ocean", "Cafe Rouge", "Millie's Kitchen", "Rising Cafe - From the Rubble", "The Old Crown", "Miller and Carter", "Horse and Jockey", "Ristorante Da Vinci", "Cafe Italiano", "Etna", "Las Iguanas", "Selmina's Restaurant and Bar", "Chiquito", "Hummus House UK", "Anatalya Restaurant", "Pasha Turkey Restaurant", "Mister M's Traditional Fish & Chips", "City Chippy", "My Dhabba", "Aqua", "Al Bader", "Habibi"}}
    priceList = {"cheap eats":{"A.G.G African Restaurant & Bar", "Anedo Finger Licking Restaurant & Bar", "Chi Bar", "The Spon Gate", "Nima's", "Rixs Bombay cafe bar", "Millie's Kitchen", "Rising Cafe - From the Rubble", "Miller and Carter", "Cafe Italiano", "Etna", "Selmina's Restaurant and Bar", "Hummus House UK", "Pasha Turkey Restaurant", "Mister M's Traditional Fish & Chips", "Ate Til Ate", "City Chippy"}, "mid range":{"My Dhabba", "The Old Crown", "Miller and Carter", "Etna", "Las Iguanas", "Selmina's Restaurant and Bar", "Chiquito", "Anatalya Restaurant", "Turmeric Gold", "Aqua", "Al Bader", "Wagamama", "Habibi"}, "fine dining":{"Ristorante Da Vinci", "The Cross at KenilWorth"}}
    cuisineList = {"African":{"A.G.G African Restaurant & Bar", "Anedo Finger Licking Restaurant & Bar"}, "British": {"Rising Cafe - From the Rubble", "The Old Crown", "Miller and Carter", "Horse and Jockey"}, "Chinese":{"Chi Bar"}, "French":{"Cafe Rouge", "Millie's Kitchen"}, "Fast Food":{"Mister M's Traditional Fish & Chips", "Ate Til Ate", "City Chippy"}, "Indian":{"The Spon Gate", "Nima's", "Rixs Bombay Cafe Bar", "The Ocean"}, "Italian":{"Ristorante Da Vinci", "Cafe Italiano", "Etna"}, "Japanese":{"Chi Bar", "Wagamama"}, "Korean":{"Jinseon Korean BBQ Restaurant & Bar"}, "Lebanese":{"Aqua", "Al Bader", "Habibi", "Hummus House UK"}, "Mexican":{"Las Iguanas", "Selmina's Restaurant Bar", "Chiquito"}, "Turkish":{"Hummus House UK", "Anatalya Restaurant", "Pasha Turkish Restaurant"}}
    addressList = {"A.G.G African Restaurant & Bar":"58 Far Gosford Street, CV1 5DZ", "Anedo Finger Licking Restaurant & Bar":"80 Far Gosford Street, CV1 5DZ", "Chi Bar":"13 High Street, Coventry, CV1 5RE", "Turmeric Gold":"166 Spon St, Coventry, CV1 3BB", "The Spon Gate":"The Sky Dome, Coventry CV1 3AZ", "Nima's":"525 Foleshill Road, Coventry CV6 5AU", "Rixs Bombay cafe bar":"5 Priory Place | City Centre,CV1 5SQ", "The Ocean":"46 Jubilee Crescent | Radford, CV6 3ET", "Cafe Rouge":"2 Belgrade Plaza, CV1 4AJ", "Millie's Kitchen":"Market Way, CV1 1DL", "Rising Cafe - From the Rubble":"Priory Street, Coventry CV1 5FB,", "The Old Crown":"466 Aldermans Green Road, Coventry CV2 1NP", "Miller and Carter":"294 Kenpas Highway, Coventry CV3 6PB", "Horse and Jockey":"Tamworth Road | Corley, Coventry CV7 8AA", "Ristorante Da Vinci":"48 Earlsdon Street, Coventry CV5 6EJ", "Cafe Italiano":"2 Trinity Street, Coventry", "Etna":"54-57 Hertford Street, CV1 1LB", "Las Iguanas":"Cathedral Lanes | Broadgate, Coventry CV1 1LL", "Selmina's Restaurant and Bar":"16 Spon Street, Coventry CV1 3BA, England", "Chiquito":"Arena Retail Park Classic Drive, CV6 6AS", "Hummus House UK":"2 Market Way, Coventry CV1 1DY,", "Anatalya Restaurant":"124-126 Walsgrave Road, Coventry CV2 4AX", "Pasha Turkey Restaurant":"136 Far Gosford Street, Coventry CV1 5DY", "Mister M's Traditional Fish & Chips":"164 The Chesils | Cheylesmore, CV3 5BH", "Ate Til Ate":"87 Moseley Avenue | Coundon, CV6 1HR", "City Chippy":"3a Fairfax Street, Coventry CV1 5SR","My Dhabba":"1-3 Lower Holyhead Road, Coventry CV1 3AX", "Al Bader":"31 High Street, Coventry CV1 5RE", "Aqua":"14 Butts, Coventry 3GR", "Habibi":"142 Far Gosford Street, Coventry CV1 5DY"}
    ratingList = {1:{"Rixs Bombay cafe bar", "Chiquito"}, 2:{"A.G.G African Restaurant & Bar", "Anedo Finger Licking Restaurant & Bar", "The Spon Gate", "Nima's", "Cafe Rouge", "The Old Crown", "Miller and Carter", "Horse and Jockey", "Cafe Italiano", "Etna", "Las Iguanas", "Anatalya Restaurant", "Pasha Turkish Restaurant", "Mister M's Traditional Fish & Chips", "Ate Til Ate", "My Dhabba", "Turmeric Gold", "Chi Bar", "Wagamama", "Aqua", "Al Bader", "Habibi"}, 3:{"The Ocean", "Millie's Kitchen", "Rising Cafe - From the Rubble", "Ristorante Da Vinci", "Selmina's Restaurant", "Hummus House UK"}}

    import socket
    import time
    from Printer import dictPrinter 
    from mainCode import mainCode
    import pickle
    #Give ChatBot server an IP address and port
    host = "127.0.0.1"
    port = 50091
    #Create Socket and bind server to socket           
    thisSocket = socket.socket()
    thisSocket.bind((host,port))
    #Listen for clients     
    thisSocket.listen(1)
    #Connect to client
    conn, addr = thisSocket.accept()
    #print Connect ip address
    print ("The Connection ip is : " + str(addr))
    #Introduction for the chatbot
    nameIntro = "Hi. My name is Jess. What is your name? "
    conn.send(nameIntro.encode()) 
    #Repear forever
    while True:
                #Receive info from client
                receiveMess = conn.recv(1024).decode()
                #if no info from client end loop
                if not receiveMess:
                                   break               
                userName = receiveMess
                #message for type of meal
                introMess = ("Hi " + str(userName) + "! I am a Coventry food guide. What would you like to eat? Please choose a number")
                conn.send(introMess.encode())
                #recieve meal choice
                mealChoice = int(conn.recv(1024).decode())
                if mealChoice != 1 or mealChoice != 2 or mealChoice !=3:
                    message = "Please choose from the list. I can only know a number of things."
                    conn.send(introMess.encode())
                #which cuisine
                whichCuisine = ("Which cuisine suits you? Please choose a number")
                conn.send(whichCuisine.encode())
                #recieve cuisine choice
                cuisineChoice = int(conn.recv(1024).decode())
                #ask if price matters
                message = ("Does the price matter? Yes or No")
                conn.send(message.encode())
                priceMatters = conn.recv(1024).decode()
                priceMatters = priceMatters.lower()
                if priceMatters == "yes":
                    message = "Which price range would you prefer? Cheap eats, mid range, or fine dining?"
                    conn.send(message.encode())
                    priceChoice = conn.recv(1024).decode()
                    priceChoice = priceChoice.lower()
                    if "cheap" in priceChoice:
                        priceChoice = "cheap eats"
                    elif "mid" in priceChoice:
                        priceChoice = "mid range"
                    elif "fine" in priceChoice:
                        priceChoice = "fine dining"
                elif priceMatters == "no":
                    priceChoice = 0
                #ask if rating matters
                message = ("Does rating matter? Yes or No")
                conn.send(message.encode())
                ratingMatters = conn.recv(1024).decode()
                ratingMatters = ratingMatters.lower()
                if ratingMatters == "yes":
                    message = "Which rating range would you prefer? 1, 2, or 3 where 3 is the best and 1 is the least best?"
                    conn.send(message.encode())
                    ratingChoice = int(conn.recv(1024).decode())
                elif ratingMatters == "no":
                    ratingChoice = 0
                #send list of final restaurants                
                message = mainCode(mealChoice, cuisineChoice, priceMatters, ratingMatters, priceChoice, ratingChoice)              
                if len(message) == 0:
                    message = "I'm sorry but I don't know any restaurants that fit your needs. You could try changing your choices and maybe I can help you out."
                    conn.send(message.encode())
                elif len(message) > 0:
                    message = str(message)
                    message = ("I would recommend the following restaurant(s): " + "\n" + " " * 31 + message)
                    conn.send(message.encode())
                #End or repeat
                message = ("Do you need to look for any other restaurants in Coventry? Yes or No?")
                conn.send(message.encode())
                message = conn.recv(1024).decode()
                message = message.lower()
                if message == "no":
                    message = "end"
                    conn.send(message.encode())
                    break
                elif message == "yes":
                    message = "repeat"
                    conn.send(message.encode())
                    continue
                    
    conn.close()   
    print("Conversation between user and ChatBot Ended")
if __name__ == '__main__':
            Main()