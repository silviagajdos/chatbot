import time
import random


name = raw_input("What is your name? ")

time.sleep(1)
print("Hello im Jess. Nice to meet you " + str(name))

feeling = raw_input("How are you feeling today? ")

time.sleep(1)
if "good" in feeling:
    print ("Thats good to hear. ")
elif "great" in feeling:
   emotion = raw_input("why do you feel so great? ")
   print(str(emotion) + " Well i hope you feel like that all the time. ")
else:
    print("I hope you feel better soon ")

time.sleep(1)
colour = raw_input("What is your favourite colour? ")

mycolour = ["Red","Blue","Green","Yellow","Purple","Black","Grey","White"]

time.sleep(1)
print("My favourite colour is " + random.choice(mycolour))

if random.choice(mycolour) == colour:
    print("That my favourite colour too. ")

time.sleep(1)
sports = raw_input("what is your favourite sports? ")

mysports = ["Basketball","Baseball","Football","Cricket","Netball","Tennis","Vollyball"]

time.sleep(1)
print("The sport that i like is " + random.choice(mysports))

sport = raw_input("Whats your favourite team? ")
Match = raw_input("Did you watch there latest game? ")
Result = raw_input("Did your team win? ")
if "yes" in Result:
    print("That good. ")
else:
    print("Hopefully they do better next time. ")