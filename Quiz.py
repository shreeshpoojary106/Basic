
def Quiz():
    question_1 = {
        1 : "Which is the capital state of India ? : ",
        'a' : 'Karnataka',
        'b' : 'Delhi',
        'c' : 'Maharastra',
        'd' : 'Kashmir',
        'ans' : 'b'
    }

    question_2 = {
        2 : "How many bits make a Byte ? : ",
        'a' : '1',
        'b' : '2',
        'c' : '4',
        'd' : '8',
        'ans' : 'd'
    }

    question_3 = {
        3 : "How many sqaures are there in a chess board ? : ",
        'a' : '48',
        'b' : '56',
        'c' : '64',
        'd' : '92',
        'ans' : 'c'
    }

    question_4 = {
        4 : "On what year India got Independence ? : ",
        'a' : '1947',
        'b' : '1948',
        'c' : '1949',
        'd' : 'India never became got freedom !',
        'ans' : "a" and "d"
    }

    question_5 = {
        5 : "which is the programming language , known as updated language ? : ",
        'a' : 'C',
        'b' : 'C++',
        'c' : 'Python',
        'd' : 'Java',
        'ans' : 'b'
    }

    def question1():
      for key,values in question_1.items():
          if (key == 'ans'):
            continue
          print(key,":",values)
      ans_1 = input("\nEnter the answer (a/b/c/d) : ").lower()
      if(ans_1 == question_1['ans']):
        #score += 1
        print("correct Answer !!\n")
        #print("Your score is :",score)
      else:
        print("Wrong answer !!")
        print("The correct answer is : ",question_1['ans'],"\n")
    
    def question2():
      for key,values in question_2.items():
          if (key == 'ans'):
            continue
          print(key,":",values)
      ans_2 = input("\nEnter the answer (a/b/c/d) : ").lower()
      if(ans_2 == question_2['ans']):
        #score += 1
        print("correct Answer !!\n")
        #print("Your score is :",score)
      else:
        print("Wrong answer !!")
        print("The correct answer is : ",question_2['ans'],"\n")
    
    def question3():
      for key,values in question_3.items():
          if (key == 'ans'):
            continue
          print(key,":",values)
      ans_3 = input("\nEnter the answer (a/b/c/d) : ").lower()
      if(ans_3 == question_3['ans']):
        #score += 1
        print("correct Answer !!\n")
        #print("Your score is :",score)
      else:
        print("Wrong answer !!")
        print("The correct answer is : ",question_3['ans'],"\n")

    def question4():
      for key,values in question_4.items():
          if (key == 'ans'):
            continue
          print(key,":",values)
      ans_4 = input("\nEnter the answer (a/b/c/d) : ").lower()
      if(ans_4 == question_4['ans']):
        #score += 1
        print("correct Answer !!\n")
        #print("Your score is :",score)
      else:
        print("Wrong answer !!")
        print("The correct answer is : ",question_4['ans'],"\n")
        
    def question5():
      for key,values in question_5.items():
          if (key == 'ans'):
            continue
          print(key,":",values)
      ans_5 = input("\nEnter the answer (a/b/c/d) : ").lower()
      if(ans_5 == question_5['ans']):
        #score += 1
        print("correct Answer !!\n")
        #print("Your score is :",score)
      else:
        print("Wrong answer !!")
        print("The correct answer is : ",question_5['ans'],"\n")

    question1()
    question2()
    question3()
    question4()
    question5()


Quiz()
