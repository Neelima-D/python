capitals={'india':'new delhi',
          'china':'beijing',
          'russia':'moscow'}
#print(capitals.items())
#capitals.update({'china':'tokyo'})
print(capitals.pop('china'))     
for key,value in capitals.items():
    print(key,value) 
         