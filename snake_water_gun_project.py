from random import randint

d=0
c=0
for i in range(100):
    k=input("if u want to play writ\"Yes\" and if not print\"No\"")
    if(k=="Yes"):
        user=int(input("Enter 1 for snake,2 for water and 3 for gun"))
        comp=randint(1,3)
        print(f"yours choice is{user} and computer choice is{comp}")
        if(comp==user):
            print("Draw")
        elif((comp==1 and user==3)or(comp==2 and user==1)or (comp==3 and user==2)):
             print ("you won")
             c+=1
        elif((comp==2 and user==3)or(comp==3 and user==1)or (comp==1 and user==2)):
         
             print("You Lose")
             d+=1
        else:
            print("Wrong choice")
    elif(k=="No"):
        break
print("Your score is",c)
print("Computer's score is",d)
if(c>d):
    print("You wins the match")
else:
    print("You Lose the match")



    
