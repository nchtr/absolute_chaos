print("Choose your branch:\n1 - Science, 2 - Humanitarian subjects, 3 - Art, 4 - Sport: ")
chs=int(input())
def sci():
    print("Choose your subject:\n1 - Math, 2 - Physics: ")
    sub=int(input())
    if sub==1:
        print("You are Financier")
    elif sub==2:
        print("You are Engineer")
    else:
        print("incorrect input")
def hsub():
    print("Choose your subject:\n1 - History, 2 - Foreign Languages:")
    sub=int(input())
    if sub==1:
        print("You are Historic or Diplomat ")
    elif sub==2:
        print("You are Translator")
    else:
        print("incorrect input")
def art():
    print("Choose your subject:\n1 - Drawing, 2 - Singing:")
    sub=int(input())
    if sub==1:
        print("You are Painter or Architect")
    elif sub==2:
        print("You are Singer or Tamada")
    else:
        print("incorrect input")
def sprt():
    print("Choose your subject:\n1 - Team, 2 - Individual: ")
    sub=int(input())
    if sub==1:
        print("You are footballer or Basketball player")
    elif sub==2:
        print("You are boxer or tennis player ")
    else:
        print("incorrect input")
if chs==1:
    sci()
elif chs==2:
    hsub()
elif chs==3:
    art()
elif chs==4:
    sprt()
else:
    print("incorrect input")