import time #Real time functions
import random #Randomise output
import requests #Initialise with "pip install requests" // external library for API
import datetime #Import todays time and date

def recallAtRand(): #Random chatbot age generator
  makeRequest= input("Would you like to know how old i am?\n")
  textAge= ["18","20","22","24","26","28","30","32","34","36","38","40","42"]
  if makeRequest== ("Yes")or makeRequest==("YES")or makeRequest==("yes")or makeRequest==("ok")or makeRequest==("OK"):
    for answer in textAge:
      print("I am ",random.choice(textAge))
      break
  elif makeRequest == ("No")or makeRequest==("no")or makeRequest==("NO"):
    print("Fine..")
  else:
    print("That doesn't answer my question, moving on "+userName+".. I'm ",random.choice(textAge))
    
def howAreYou(): #ADDITIONAL QUESTIONS
  myValue = str(input("How are you today?\n"))
  inputValues= ["Alright", "alright", "ALRIGHT", "Good", "good", "GOOD", "Ok", "ok", "OK", "Excellent", "excellent", "EXCELLENT"]
  if myValue in inputValues:
     print("That is great news")
  else:
       print("I know that feeling "+userName+".. Hopefully the sun will come out later and change things..")
  userPlans = input("What are you upto today?\n")
  print("Ok, sounds like a plan to me.. "+userName)
  
def weatherAPI(): #WEATHER API
  queWeath = input("Would you like to know what the weather is doing today?\n")
  if queWeath == ("Yes")or queWeath==("yes")or queWeath==("YES")or queWeath==("Y")or queWeath==("y"):
    api_adress ='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = input("Whic City will you be visiting?\n")
    url = api_adress + city
    json_data = requests.get(url).json()
    formatted_data = json_data['weather'][0]['main']
    print(formatted_data)
  elif queWeath==("No")or queWeath==("NO")or queWeath==("no")or queWeath==("N")or queWeath==("n"):
    noPlans = input("Ok, not planning on going out today?\n")
    if noPlans== ("Yes")or noPlans==("yes")or noPlans==("YES")or noPlans==("Y")or noPlans==("y"):
      print("Right, ok... "+userName+", you should probably check the weather before you leave..")
    elif noPlans==("No")or noPlans==("NO")or noPlans==("no")or noPlans==("N")or noPlans==("n"):
      print("I thought so "+userName+"!")
    else:
      print("...?")
  else:
    print("Ok, that doesn't answer my question.. ")
    
def guessMyNum(): #GUESS THE NUMBER
  print("I'm thinking of a number between 1 and 100")
  print("What number am i thinking of "+userName+"?")
  botNum = random.randint(1,100)
  g = int(input())
  myAttempts = 0
  while g != botNum:
    if g > botNum:
      print("Think smaller")
    else:
      print("Think bigger")
    g = int(input())
    myAttempts +=1
  print("it took you ",myAttempts," attempts to guess my number "+userName+"!")
  
def jobStatus(): #EMPLOYMENT // TOOK INSPIRATION FROM CODIO PRACTICE SESSIONS
  jobQuest = str(input("Do you have a job? "+"\n"))
  jobAns= ["Yes", "yes", "Y", "y", "Yeah", "yeah"]
  if jobQuest in jobAns:
    time.sleep(2)
    print("Excellent! Hope you are enjoying the world of work!"+"\n")
  else:
    time.sleep(2)
    print("Sorry to hear that, hopefully you will find a job soon..."+"\n")
  x = input("Hey, do you know what!? We have job opportunities available! " + "\n" + "Enter [vacancy] for list of Vacancies or [salary] for Salary Scales: ")
  if x == "vacancy":
    print("Here are the vacancies: "+"\n")
    jobDept = ["Operations", "Logistics", "Customer Service"]
    skillLevel = [1,2,3]
    jobTitle = ["Apprentice", "General staff", "Management"]
    allPositions=[]
    for D in jobDept:
      for T in jobTitle:
        for L in skillLevel:
          select = "Level " + str(L) + (" ") + T + " in " + D 
          allPositions.append(select)
    print(allPositions)
    userInterest = input("Anything take your fancy?"+"\n")
    print("Ok, if you do decide you want to apply for a specific role; email me your CV.."+"\n")
  elif x == "salary":
    def userInstructions(k): #TOOK INSPIRATION FROM CODIO PRACTICE SESSIONS
      if k <= 0:
        print("\t")
        print("*** End of salary list ***"+"\n")
        userSkill = input("Does this compare to your expectations?"+"\n")
        print("You are welcome to apply for a job with us, just send me an email.."+"\n")
      elif k >= 75000 and k <= 80000:
        print("Management Fixed Salary A: ")
        print(k)
        userInstructions(k-12000)
      elif k >= 55000 and k <= 74000:
        print("Management Fixed Salary B: ")
        print(k)
        userInstructions(k-12000)
      elif k >= 50000 and k <= 54000:
        print("Management Fixed Salary C: ")
        print(k)
        userInstructions(k-12000)
      elif k <=50000 and k >= 40000:
        print("Supervisor Fixed Salary A: ")
        print(k)
        userInstructions(k-12000)
      elif k <=40000 and k >= 25000:
        print("Supervisor Fixed Salary B: ")
        print(k)
        userInstructions(k-12000)
      elif k <= 25000 and k >= 15000:
        print("Basic Starting Salary: ")
        print(k)
        userInstructions(k-12000)
      elif k <= 15000:
        print("Apprentice Starting Salary: ")
        print(k)
        userInstructions(k-12000)  
      else:
        print("\t")
        print("Executive Management Salary: ")
        print(k)
        userInstructions(k-12000)
    userInstructions(90000)
  else:
    print("Nevermind, moving on.."+"\n")
    time.sleep(1)
    
def schoolSubjects():#QUESTION ON SCHOOL SUBJECTS
  askQ = input("I need to ask you a few quick questions if thats ok?\n")
  if askQ==("Yes")or askQ==("YES")or askQ==("yes"): 
    print("Great! Thank you "+userName)
    time.sleep(1)
  elif askQ==("y")or askQ==("Y")or askQ==("Ok")or askQ==("ok")or askQ==("OK"):
    print(askQ+"? Thats as good as a yes for me!")
    time.sleep(1)
  elif askQ==("No")or askQ==("NO")or askQ==("no"):
    time.sleep(1)
    print("..well i'll ask anyway!")
    time.sleep(1)
  elif askQ==("N")or askQ==("n"):
    time.sleep(1)
    print(askQ+"? I'm guessing thats a no..")
    time.sleep(1)
    print("I'll ask anyway!")
    time.sleep(1)
  else:
    print(askQ+"? I can't tell if thats a yes or a no..\n so i'm going to pretend its a yes..")
    time.sleep(1)
  questEd = input("What was your favourite subject at secondary school?\n")
  if questEd==("maths")or questEd==("MATHS")or questEd==("Maths")or questEd==("science")or questEd==("SCIENCE")or questEd==("Science")or questEd==("english")or questEd==("ENGLISH")or questEd==("English"):
    print(questEd+" is a core subject, its good to know you like a challenge..")
  elif questEd ==("IT")or questEd ==("it")or questEd==("geography")or questEd==("GEOGRAPHY")or questEd==("Geography"):    
    print("Good, "+questEd+" will be valueable to your future..")
  elif questEd==("history")or questEd==("HISTORY")or questEd==("History"):
    print("Ok.. "+questEd+" is probably not the most interesting choice of subjects..")
  elif questEd==("drama")or questEd==("DRAMA")or questEd==("Drama"):
    print(questEd+", good choice! You sound like a creative person to me!")
  elif questEd==("music")or questEd==("MUSIC")or questEd==("Music"):
    print(questEd+", good choice Mozart!")
  elif questEd==("art")or questEd==("ART")or questEd==("Art"):
    print(questEd+", Good choice Van Gough!")
  else:
    print(questEd+"? I'm not familiar with that subject..")

#CONVERSATION WILL START FROM HERE AND CALL ON THE ABOVE FUNCTIONS WHEN REQUESTED    
print("\n>>> An operator will be with you shortly.. <<<\n")
from datetime import date #SOUGHT HELP FROM STACKOVERFLOW
todaysDate = date.today()
print("Todays date:",todaysDate, "\n")
introUser=input("Hello!\n")
if introUser==("Bye")or introUser==("bye")or introUser==("BYE"):
  print("You have to go? ok, speak soon\n")
  print(">>> Operator has left the conversation <<<\n")
else: # RANDOM OPERATOR SELECTION // USED CHAPTER 10 OF THINK PYTHON: HOW TO THINK LIKE A COMPUTER SCIENTIST 
  textAge= ["Adam","Ben","Charlie","Dan","Ester","Fred","Grace","Hannah","Ian","James","Kiera","Liam","Mike"]
  for ans in textAge:
    print("My name is "+random.choice(textAge))
    break
  userName=input("Who am i speaking with?\n")
  if userName==("Bye")or userName==("bye")or userName==("BYE"):
    print("You have to go? ok, bye!\n")
    print(">>> Operator has left the conversation <<<\n")
  else:  
    print(introUser+" "+userName+"!?")
    userAge = input("How old are you "+userName+"?\n")
    if userAge == ("Bye")or userAge==("bye")or userAge==("BYE"):
      print("You have to go "+userName+"? ok, catch you later!\n")
      time.sleep(1)
      print(">>> Operator has left the conversation <<<\n")
      time.sleep(1)
    else:
      print("Ok, "+userName+" you are " + userAge + " but I bet you can't guess my age..?")
      userGuess = input()
      if userGuess == ("Bye")or userGuess==("bye")or userGuess==("BYE"):
        print("You have to go "+userName+"? ok, catch you later!\n")
        time.sleep(1)
        print(">>> Chatbot has left the conversation <<<\n")
        time.sleep(1)
      else:
        print("Good guess! but not quite..")
        
        #CALLING ON FUNCTIONS FOLLOWING INTRODUCTORY QUESTIONS
        recallAtRand() #OPERATOR CREDENTIALS
        time.sleep(1) 
        howAreYou() #BASIC QUESTIONS
        time.sleep(1)
        weatherAPI() #CALL ON WEATHER API CODE
        time.sleep(1)
        schoolSubjects() #FURTHER QUESTIONS
        time.sleep(1)
        guessMyNum() #GUESS NUMBER
        time.sleep(1)
        jobStatus() #JOB RELATED QUESTIONS
        #CONCLUDE CONVERSATION
        userFuture = input("What are your future plans?\n")
        time.sleep(1)
        print("if that is what you want in life then i wish you every success for the future!"+"\n")
        time.sleep(2)
        userBye = input("I have to go now..\n")
        byeBye= input("Bye "+userName+"\n\n")
        time.sleep(3)
        print(">>> Chatbot has left the conversation <<<\n")
        time.sleep(3)
        #END
