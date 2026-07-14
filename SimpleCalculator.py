#from timeit import default_timer as timer
def calculator():
   a = float(input("Enter the numbers : "))
   opp = input("Enter the Operator(+,-,*,/) : ")
   b = float(input("Enter the numbers : "))

   #start = timer()

   def addition():
      sum = a+b
      print("=",sum)

   def subtraction():
      sub = a-b
      print("=",sub)

   def multiplication():
      multi = a*b
      print("=",multi)

   def division():
      div = a/b
      print("=",div)

   if(opp == '+'):
      addition()

   elif(opp == '-'):
      subtraction()

   elif(opp == '*'):
      multiplication()

   elif(opp == '/'):
      division()
   
   #stop = timer()
   #print(stop-start)

while True:
  calculator()
