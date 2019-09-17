#print ("Yibby   eh er hewr hrewh rewh hrew  q!")

#skref1
"""búa til function move sem tekur inn staðsetningu og beiðni um færslu og skilar
nýrri staðsetningu eða commenti ef færslan er ekki í boði fyrir tiltekinn reit"""

def move_val(x,y):
    """takes in location (x) and direction (y) and moves accordingly, returns
    new location"""
    #x = float(x)
    y = y.lower()
    if y =="n":
        x += 0.1
        return x
    elif y == "s":
        x -= 0.1
        return x
    elif y == "e":
        x += 1.0
        return x
    elif y == "w":
        x -= 1.0
        return x




def move(x):
    """ takes in a location (x) and returns a new location by conditions"""
    if x == 1.1:
        print("You can travel: (N)orth.")
        y = input("Direction: ").lower()
        while y != "n":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.") 
        y = input("Direction: ").lower()
        while y!= "n" and y!= "e" and y!= "s":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        y = input("Direction: ").lower()
        while  y!= "e" and y!= "s":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 2.1:
        print("You can travel: (N)orth.")
        y = input("Direction: ").lower()
        while y != "n":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 2.2:
        print("You can travel: (S)outh or (W)est.")
        y = input("Direction: ").lower()
        while y != "s" and y != "w":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 2.3:
        print("You can travel: (E)ast or (W)est.")
        y = input("Direction: ").lower()
        while y != "e" and y != "w":
            print("Not a valid direction!")
            y = input("Direction: ").lower()
        else:
            x = move_val(x,y)
            return round(x,1)
    elif x == 3.2:


x= 1.2

y = move(x)

print(y)



#skref 2
#byrjunargildi: tile (1,1) og fyrsta input frá notanda


#skref 3 
# while loop þar sem sem move() er beitt 
