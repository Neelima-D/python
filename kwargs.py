def hello(**kwargs):
   # print("hello "+kwargs[first]+" "+kwargs[last])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title="mr",first="bro",middle="dude",last="code")