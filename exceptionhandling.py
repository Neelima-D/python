from logging import exception


try:
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide zero ")
except ValueError as e:
    print(e)
    print("enter numbers only ")
except exception:
    print(e)
    print("something weent wrong")
else:
    print(result)
finally:
    print("This will always executes")