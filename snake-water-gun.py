print("lets play snake water gun")
import random
l = ["Snake", "Water", "Gun"]
m=0
c=0
d=0
for i in range(11):
        r = random.choice(l)
        a = input("press S for snake W for water G for gun:")
        if a=="S" or a=="s":
            if r=="Water":
                print(f"You won to {r}")
                m +=1
            elif r=="Gun":
                print(f"you lost to {r}")
                c +=1
            else:
                print("DRAW")
                d +=1

        elif a=="W" or a=="w":
            if r=="Snake":
                print(f"you lost to {r}")
                m +=1
            elif r=="Gun":
                print(f"you won to {r}")
                c +=1
            else:
                print("DRAW")
                d += 1

        elif a=="G" or a=="g":
            if r=="Water":
                print(f"you lost to {r}")
                m +=1
            elif r=="Snake":
                print(f"you won to {r}")
                c +=1
            else:
                print("DRAW")
                d += 1
        else:
            print("enter valid input")

print("GAME OVER")
print("Your Score :", m)
print("system score :", c)
print("Draws:",d)

