first_name = input("Please enter you'r name ")
last_name = input("Please enter you'r last name ")
phone = input("Please enter you'r phone number ")
age = input("Please enter you'r age ")
address = input("Please enter you'r address ")
skill = input("Please enter one skill ")

html = f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible'><title>Document</title></head><body><h1>{first_name}  {last_name} </h1><h2>{age}</h2><h2>{phone}</h2><h3>{address}</h3><h4>{skill}</h4></body></html>"

print(html)

newFile = open("cv.html","w")
newFile.write(html)
newFile.close()