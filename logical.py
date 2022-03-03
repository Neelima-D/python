temp=int(input("what is the temp outside"))
#if temp>=0 and temp<+30:
  #  print("the weather is good today")
#elif temp<0 or temp<30:
 #   print("weather is bad today")

if not(temp>=0 and temp<=30):
    print("weather is bad today") 
elif not(temp<0 and temp>30):
    print("weather is good today")           
    