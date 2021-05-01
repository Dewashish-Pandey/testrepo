import random  #to generate random answers
import sys #sys module can be used for exitig the program

responses=["It is certain","You may rely on it","As I see it, yes","Most likely","without a doubt","Bahaha...why not?","You bet","Yes, I see it"]
questions=True

while questions:
    ques=input("Please ask a question\n") #to have a loop of questions
    
    if ques=="": 
        sys.exit()#if empty, exit
    else:
        print(responses[random.randint(0,7)])
