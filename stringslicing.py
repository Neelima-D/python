name="happy life"
first_name=name[3]
print(first_name)

name="happy life"
first_name=name[:4]
print(first_name)

name="happy life"
funky_name=name[:10:3]
print(funky_name)

reversed_name=name[::-1]
print(reversed_name)
print("SLICE FUNCTIONS")
website="http://google.com"
slice=slice(7,-4)
print(website[slice])