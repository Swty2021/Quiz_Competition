import json
total_dict = {
    "Question 1":
    {"Question":"Which is immutable data structure?","A": "List","B": "Tuple","C": "Dictionary","Correct answer": "B","Answer":"Tuple"},
    "Question 2":
    {"Question":"Which is mutable data structure?","A": "Set","B": "List","C": "Dictionary","Correct answer": "B","Answer":"List"},
    "Question 3":
    {"Question":"Which collection does not allow duplicate members?","A": "Set","B": "List","C": "Dictionary","Correct answer": "A","Answer":"Set"},
    "Question 4":
    {"Question":"What is the correct file extension for Python files?","A": ".py","B": ".pyt","C": ".yt","Correct answer": "A","Answer":".py"},
    "Question 5":
    {"Question":"What is the correct keyword to write a function for Python files?","A": "def","B": "func","C": "function","Correct answer": "A","Answer":"def"},
    "Question 6":
    {"Question":"What is the keyword to take input in Python program?","A": "input()","B": "int()","C": "str()","Correct answer": "A","Answer":"input()"},
    "Question 7":
    {"Question":"Which of the following is Tuple?","A": "{1,2,3}","B": "[1,2,3]","C": "(1,2,3)","Correct answer": "C","Answer":"(1,2,3)"},
    "Question 8":
    {"Question":"Which of the following is Set?","A": "{1,2,3}","B": "[1,2,3]","C": "(1,2,3)","Correct answer": "A","Answer":"{1,2,3}"},
    "Question 9":
    {"Question":"Which of the following is List?","A": "{1,2,3}","B": "[1,2,3]","C": "(1,2,3)","Correct answer": "B","Answer":"[1,2,3]"},
    "Question 10":
    {"Question":"Which of the following is correct?","A": "x=5","B": "str=5","C": "x='5'","Correct answer": "A","Answer":"x=5"},
    "Question 11":
    {"Question":"What is a correct syntax to output Hello World in Python?","A": "p('Hello World')","B": "print('Hello World')","C": "echo('Hello World')","Correct answer": "B","Answer":"print('Hello World')"},
    "Question 12":
    {"Question":"How do you insert COMMENTS in Python code?","A": "//This is a comment","B": "#This is a comment","C": "/*This is a comment*/","Correct answer": "B","Answer":"#This is a comment"},
    "Question 13":
    {"Question":"Which one is NOT a legal variable name?","A": "Myvar","B": "my-var","C": "_myvar","Correct answer": "B","Answer":"my-var"},
    "Question 14":
    {"Question":"Which method can be used to remove any whitespace from both the beginning and the end of a string?","A": "trim","B": "len","C": "strip","Correct answer": "C","Answer":"strip"},
    "Question 15":
    {"Question":"Which method can be used to return a string in upper case letters?","A": "toUpperCase()","B": "uppercase","C": "upper()","Correct answer": "C","Answer":"upper()"},
    "Question 16":
    {"Question":"Which operator is used to multiply numbers?","A": "X","B": "*","C": "%","Correct answer": "B","Answer":"*"},
    "Question 17":
    {"Question":"Which operator can be used to compare two values?","A": "==","B": "=","C": "><","Correct answer": "A","Answer":"=="},
    "Question 18":
    {"Question":"How do you start writing an if statement in Python?","A": "if(x>y)","B": "if x>y:","C": "if x>y then:","Correct answer": "B","Answer":"if x>y:"},
    "Question 19":
    {"Question":"How do you start writing a while loop in Python?","A": "while x>y{","B": "while x>y:","C": "while(x>y):","Correct answer": "B","Answer":"while x>y:"},
    "Question 20":
    {"Question":"All keywords in Python are in?","A": "Upper case","B": "Capitalize","C": "Lower case","Correct answer": "C","Answer":"Lower case"},
    "Question 21":
    {"Question":"Which of the following is used to define a block of code in Python language?","A": "Indentation","B": "Key","C": "Brackets","Correct answer": "A","Answer":"Indentation"},
    "Question 22":
    {"Question":"Python supports the creation of anonymous functions at runtime, using a construct called?","A": "pi","B": "anonymous","C": "lambda","Correct answer": "C","Answer":"lambda"},
    "Question 23":
    {"Question":"Which of the following functions is a built-in function in python?","A": "factorial()","B": "print()","C": "seed()","Correct answer": "B","Answer":"print()"},
    "Question 24":
    {"Question":"What arithmetic operators cannot be used with strings in Python?","A": "*","B": "-","C": "+","Correct answer": "B","Answer":"-"},
    "Question 25":
    {"Question":"Which of the following concepts is not a part of Python?","A": "Pointers","B": "Loops","C": "Dynamic programming","Correct answer": "A","Answer":"Pointers"}
   
    }
print("Writing into json")
with open("quiz.json","w") as outfile:
    b = json.dump(total_dict,outfile)
    #print (b)
