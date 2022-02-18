# -------------------------
#All modules
import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
import requests

#importing json file
with open("quiz.json","r") as question:
    data = json.load(question)
#print(random.choice(range(no_of_question)))
'''
print(data)
print(data["Question 1"])

print(data["Question 1"]["Question"])
'''
#Player input
user_name = input("Enter your name:")
print("Hello",user_name,"Welcome to Quiz Program")
no_of_question = int(input("How many questions you want? \n 5: \n 10: \n 15: \n 20: \n 25:"))
#user_score = 0
#for quest in range(1,no_of_question+1):
    #print("Your Choice:")
    #print(random.choice(range(no_of_question)))
def new_quiz():
    global user_score
    global correct_answers
    global wrong_answers
    user_score = 0
    correct_answers = 0
    wrong_answers = 0
    input_answers = []
    for i in range(1,no_of_question+1):
    #for i in range(1,len(data)+1):
        #print(i)
        print("Question-",str(i))
        print(data["Question " +str(i)]["Question"])
        print("A:",data["Question " +str(i)]["A"])
        print("B:",data["Question " +str(i)]["B"])
        print("C:",data["Question " +str(i)]["C"])
        #print("Correct answer:",data["Question " +str(i)]["Correct answer"])
        user_input = input("Enter your answers as A, B or C:")
        input_answers.append(user_input)
        
        if user_input == data["Question " +str(i)]["Correct answer"]:
            print("Correct Answer! You scored points.")
            user_score=user_score+1
            correct_answers = correct_answers+1
            print("Current Score:",user_score)
            #print("The Correct Answer is:",data["Question " +str(i)]["Answer"])
        else:
            print("Wrong Answer! You loss point")
            user_score = user_score-1
            wrong_answers = wrong_answers+1
            print("Current Score:",user_score)
            print("The Correct Answer is:",data["Question " +str(i)]["Answer"])
'''        
def check_answer(correct_answers,user_input):
    user_score = 0
    if user_input == data["Question " +str(i)]["Correct answer"] :
                print("Correct Answer! You scored points.")
                user_score=user_score+1
                print("Current Score:",user_score)
    else:
                print("Wrong Answer! You loss point")
                user_score = user_score-1
                print("Current Score:",user_score)
'''    
def play_again():

    user_response = input("Do you want to play again? (Y or N): ")

    if user_response == "Y":
        return True
    else:
        return False

new_quiz()

while play_again():
    new_quiz()

print("Thank you for playing quiz")
print("=========Final Scores==========")
print(user_name,"Your final score is:",str(user_score))
print("You have attempted",correct_answers,"correct answers")
print("You have attempted",wrong_answers,"wrong answers")
#print("=========ANSWERS===========")
#Sending score via mobile
mobile_no=int(input("Enter your mobile number to receive score on sms:"))
mobile_Li = []
mobile_Li.append(mobile_no)
#Sending score via email
e_mail=input("Enter your mail-id to receive score on email:")
eMail_Li = []
eMail_Li.append(e_mail)
try:  
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    # start TLS for security
    s.starttls()
  
    # Authentication
    s.login("authentication_email", "password")
  
    # message to be sent
    #message = "Hi"
    def message(subject="Quiz Notification",text="Message body"):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['Text'] = text
        return msg
    msg = message("Quiz Results Score","Your score is")
    to = eMail_Li
    # sending the mail
    s.sendmail(from_addr="sender_email",to_addrs=to, msg=msg.as_string())
  
    # terminating the session
    s.quit()
    print("Email sent successfully")
except Exception as ex:
    print("Something went wrong....",ex)
#sending via SMS
url = "https://www.fast2sms.com/dev/bulk"
number = mobile_no 
  
# create a dictionary
my_data = {
     # Your default Sender ID
    'sender_id': 'FSTSMS', 
    
     # Put your message here!
    'message': 'This is a test message', 
    
    'language': 'english',
    'route': 'p',
    
    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': number   
}
# create a dictionary
headers = {
    'authorization': 'API KEY',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}
# make a post request
try:
    response = requests.request("POST", url,
                                data = my_data,
                                headers = headers)
    #load json data from source
    returned_msg = json.loads(response.text)
      
    print(returned_msg['message'])
except:
    print("Oops! Something wrong")
    

