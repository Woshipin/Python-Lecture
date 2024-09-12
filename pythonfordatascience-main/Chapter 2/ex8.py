#Chan Yip Chun

while True:
  name = input("Who are you? ")
  if name == 'Joe':
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == 'swordfish':
      print('Access Granted.')
      break
  else:
    continue