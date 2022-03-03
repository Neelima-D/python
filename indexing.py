name="bro Code !"
#if(name[0].islower()):
 #   name=name.capitalize()
#if(name[4].isupper()):
 #   name=name.lower()
#print(name)
first_name=name[:3].upper()
last_name=name[4:].upper()
last_character=name[-1]
print(first_name)
print(last_name)
print(last_character)
