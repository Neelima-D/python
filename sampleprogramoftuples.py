employee=("name","address","mail")
print(employee.count("mail"))
print(employee.index("address"))
for j in employee:
    print(j)
if "value" in employee:
    print("value is there:")
else:
    print("value is not there:")