#print ("Yibby   eh er hewr hrewh rewh hrew  q!")

#skref1
"""búa til function move sem tekur inn staðsetningu og beiðni um færslu og skilar
nýrri staðsetningu eða commenti ef færslan er ekki í boði fyrir tiltekinn reit"""
NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"
def move_val(location,direction):
    """takes in location (x) and direction (y) and moves accordingly, returns
    new location"""
    #x = float(x)
    direction = direction.lower()
    if direction == NORTH:
        location += 0.1
        return location
    elif direction == SOUTH :
        location -= 0.1
        return location
    elif direction == EAST:
        location += 1.0
        return location
    elif direction == WEST:
        location -= 1.0
        return location

def pull_a_lever(total_coin):

    pull = input("Pull a lever (y/n): ").lower()
    
    if pull == "y":
        total_coin += 1
        print("You received 1 coin, your total is now {}.".format(total_coin))

    else:
        total_coin += 0

    return total_coin


def move(location):
    """ takes in a location and returns a new location by conditions"""
    if location == 1.1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ").lower()
        while direction != NORTH:
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.") 
        direction = input("Direction: ").lower()
        while direction!= NORTH and direction!= EAST and direction != SOUTH:
            print("Not a valid direction!")
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ").lower()
        while  direction!= EAST and direction!= SOUTH:
            print("Not a valid direction!")
            print("You can travel: (E)ast or (S)outh.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 2.1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ").lower()
        while direction != NORTH:
            print("Not a valid direction!")
            print("You can travel: (N)orth.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 2.2:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()
        while direction != SOUTH and direction != WEST:
            print("Not a valid direction!")
            print("You can travel: (S)outh or (W)est.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 2.3:
        print("You can travel: (E)ast or (W)est.")
        direction = input("Direction: ").lower()
        while direction != EAST and direction != WEST:
            print("Not a valid direction!")
            print("You can travel: (E)ast or (W)est.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ").lower()
        while direction != NORTH and direction != SOUTH:
            print("Not a valid direction!")
            print("You can travel: (N)orth or (S)outh.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)
    elif location == 3.3:
        print("You can travel: (S)outh or (W)est.")
        direction = input("Direction: ").lower()
        while direction != SOUTH and direction != WEST:
            print("Not a valid direction!")
            print("You can travel: (S)outh or (W)est.")
            direction = input("Direction: ").lower()
        else:
            location = move_val(location,direction)
            return round(location,1)


def the_game(position, total_coin, lever_position):
    while position != 3.1:
        position = move(position)
        if position in lever_position:
            total_coin = pull_a_lever(total_coin)
    print("Victory! Total coins {}.".format(total_coin))

position = 1.1
total_coin = 0
lever_position = [1.2 , 2.2 , 2.3 , 3.2]

the_game(position, total_coin, lever_position)
play_again = input("Play again (y/n): ").lower()

while play_again == "y":
    the_game(position, total_coin, lever_position)
    play_again = input("Play again (y/n): ").lower()

