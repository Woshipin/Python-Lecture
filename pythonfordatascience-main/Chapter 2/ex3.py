#Eng Kok Bing
#Gan Wei Bin

name = input("What is your name?")
name = name.strip()
if name == 'Alice':
  print('Hi, Alice.')
else:
  age = input("How old are you?")
  age = int(age)
  if age < 12:
    print('You are not Alice, kiddo.')