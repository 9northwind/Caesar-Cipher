upalp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowalp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ["0","1","2","3","4","5","6","7","8","9"]
sym = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',
           '/', ':', ';', '"', "'", '.', ',', '?',"<", ">", '~']
space = [" "]
newspace = ["^", "`"]

def caesar(x,y,z):
  cipher = ""
  for i in text:
    if choice == "encrypt"  or choice == "e":
      if i in upalp:
        loc = upalp.index(i)
        newloc = (loc + z)%26
        newi = upalp[newloc]
        cipher += newi
      elif i in lowalp:
        loc = lowalp.index(i)
        newloc = (loc + z)%26
        newi = lowalp[newloc]
        cipher += newi
      elif i in num:
        loc = num.index(i)
        newloc = (loc + z)%10
        newi = num[newloc]
        cipher += newi
      elif i in sym:
        loc = sym.index(i)
        newloc = (loc + z)%31
        newi = sym[newloc]
        cipher += newi
      elif i in space:
        if shift%2 == 0:
          cipher += "^"
        else:
          cipher += "`"
    elif choice == "decrypt" or choice == "d":
      if i in upalp:
        loc = upalp.index(i)
        newloc = (loc - z)%26
        newi = upalp[newloc]
        cipher += newi
      elif i in lowalp:
        loc = lowalp.index(i)
        newloc = (loc - z)%26
        newi = lowalp[newloc]
        cipher += newi
      elif i in num:
        loc = num.index(i)
        newloc = (loc - z)%10
        newi = num[newloc]
        cipher += newi
      elif i in sym:
        loc = sym.index(i)
        newloc = (loc - z)%31
        newi = sym[newloc]
        cipher += newi
      elif i in newspace:
        cipher += " "
  if choice == "encrypt"  or choice == "e":
    print(f"The encryped text is:\n{cipher}")
  elif choice == "decrypt" or choice == "d":
    print(f"The decryped text is:\n{cipher}")

while True:
  choice = input('Do you want to encrypt or decrypt:\n').lower()
  if choice not in ["encrypt", "decrypt", "e", "d"]:
    print("Invalid entry")
    continue
  text = input('Enter the text:\n')
  shift = int(input("Enter shift value:\n"))
  caesar(x = choice,y = text,z = shift)
  result = input("Continue?(Yes\\No):\n").lower()
  if result == "no" or result == "n":
    break
