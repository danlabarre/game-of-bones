import random

'''The game is a labyrinth style game where a bone and a user are randomly placed on a 10 by 10 board.
The user must use the 'WASD' keys to navigate blindingly through the labyrinth and try and find the bone.
Once the bone is found the player wins and the game is over.'''
gameslist = []  # Used to store the amount of turns used to play a game
gamecount = {}  # Used to organize the games list and display to the player
row1 = [0, 0, 1, 0, 4, 0, 0, 0, 1, 0]  # Each row is going to be a row in the final labyrinth
row2 = [0, 1, 0, 0, 1, 0, 3, 0, 0, 0]
row3 = [0, 0, 0, 1, 0, 0, 4, 0, 1, 0]
row4 = [0, 1, 0, 4, 0, 0, 3, 0, 0, 0]
row5 = [0, 3, 2, 3, 0, 0, 0, 0, 1, 1]
row6 = [0, 1, 0, 0, 0, 0, 3, 0, 1, 0]
row7 = [0, 0, 0, 1, 3, 0, 2, 0, 0, 0]
row8 = [4, 1, 0, 0, 2, 0, 3, 0, 1, 0]
row9 = [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]
row10 = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
labyrinth = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]  # Final labyrinth user will guide though

'''In the main you choose what type of dog you want to play as.  Each dog is given different stats that are used in
 in the game.  The size gives the type of dog different abilities.  Size 1 you can go through doggy doors, size 2 you
 can go through tunnels, size 3 you get 1 stamina so you can jump over one wall and you can go through fences and size 4
 you are given 3 stamina so you can jump over 3 walls.'''


class dogtype:  # Class that defines the stats of your dog you choose.
    def __init__(self, breed, size, stamina):
        self.breed = breed
        self.size = size
        self.stamina = stamina


def postition():  # Function that randomly assigns a position for you and for the bone.
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    while labyrinth[y][x] != 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    bonex = random.randint(0, 9)
    boney = random.randint(0, 9)
    while labyrinth[boney][bonex] != 0:
        bonex = random.randint(0, 9)
        boney = random.randint(0, 9)
    return x, y, bonex, boney


def doggytunnel(userinput, x, y, bonex, boney, dog, step):  # Function that is used if a you run into a tunnel.
    if userinput == 's':
        print('You found a doggy tunnel!')
        if dog.size == 1:
            print("You are too small to reach the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 2:
            print("You jump up to the tunnel and come out the other side!")
            if abs(boney - y - 4) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y + 4
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit in the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'a':
        print('You found a doggy tunnel!')
        if dog.size == 1:
            print("You are too small to reach the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 2:
            print("You jump up to the tunnel and come out the other side!")
            if abs(bonex - x + 4) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x - 4
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit in the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'w':
        print('You found a doggy tunnel!')
        if dog.size == 1:
            print("You are too small to reach the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 2:
            print("You jump up to the tunnel and come out the other side!")
            if abs(boney - y + 4) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y - 4
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit in the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'd':
        print('You found a doggy tunnel!')
        if dog.size == 1:
            print("You are too small to reach the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 2:
            print("You jump up to the tunnel and come out the other side!")
            if abs(bonex - x - 4) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x + 4
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit in the tunnel so you can't move.")
            movement(x, y, bonex, boney, dog, step)


def doggydoor(userinput, x, y, bonex, boney, dog, step):  # Function that is used if a you run into a doggydoor.
    if userinput == 's':
        print('You found a doggy door!')
        if dog.size == 1:
            print('You move through the door to the other side!')
            if abs(boney - y - 2) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y + 2
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the door so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'a':
        print('You found a doggy door!')
        if dog.size == 1:
            print('You move through the door to the other side!')
            if abs(bonex - x + 2) < abs(bonex - x):
                print('The smell of the bone is getting stronger')
            else:
                print('The smell of the bone is getting weaker.')
            x = x - 2
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the door so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'w':
        print('You found a doggy door!')
        if dog.size == 1:
            print('You move through the door to the other side!')
            if abs(boney - y + 2) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y - 2
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the door so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'd':
        print('You found a doggy door!')
        if dog.size == 1:
            print('You move through the door to the other side!')
            if abs(bonex - x - 2) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x + 2
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the door so you can't move.")
            movement(x, y, bonex, boney, dog, step)


def fence(userinput, x, y, bonex, boney, dog, step):  # Function that is used if a you run into a fence.
    if userinput == 's':
        print('You found a fence!')
        if dog.size == 3:
            print('You jump through the fence to the other side!')
            if abs(boney - y - 2) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y + 2
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 1 or dog.size == 2:
            print("You are too small to jump through the fence so you can't move")
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the fence so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'a':
        print('You found a fence!')
        if dog.size == 3:
            print('You jump through the fence to the other side!')
            if abs(bonex - x + 2) < abs(bonex - x):
                print('The smell of the bone is getting stronger')
            else:
                print('The smell of the bone is getting weaker.')
            x = x - 2
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 1 or dog.size == 2:
            print("You are too small to jump through the fence so you can't move")
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the fence so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'w':
        print('You found a fence!')
        if dog.size == 3:
            print('You jump through the door to the other side!')
            if abs(boney - y + 2) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y - 2
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 1 or dog.size == 2:
            print("You are too small to jump through the fence so you can't move")
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the fence so you can't move.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'd':
        print('You found a fence!')
        if dog.size == 3:
            print('You jump through the fence to the other side!')
            if abs(bonex - x - 2) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x + 2
            movement(x, y, bonex, boney, dog, step)
        elif dog.size == 1 or dog.size == 2:
            print("You are too small to jump through the fence so you can't move")
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You are too big to fit through the fence so you can't move.")
            movement(x, y, bonex, boney, dog, step)


def walljump(userinput, x, y, bonex, boney, dog,
             step):  # Function that is used if a you run into a wall and can jump it.
    if userinput == 's':
        print('Because of your size you may jump over the wall.')
        print('You have ' + str(dog.stamina) + ' jumps left before your stamina runs out.')
        jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        while jump not in ['y', 'n']:
            print("Oops you didn't pick one of the directions given.")
            jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        if jump == 'y':
            for i in range(y + 1, 10):
                if labyrinth[i][x] == 0:
                    ty = i
                    break
                else:
                    ty = 10
            if ty == 10:
                print("This wall doesn't end so you jump back down")
            else:
                temp = ty - y
                print("You jump down at the other end of the wall moving " + str(temp) + " spaces!")
                if abs(boney - y - temp) < abs(boney - y):
                    print('The smell of the bone is getting stronger.')
                else:
                    print('The smell of the bone is getting weaker.')
                y = ty
            dog.stamina = dog.stamina - 1
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You don't move and keep your stamina.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'a':
        print('Because of your size you may jump over the wall.')
        print('You have ' + str(dog.stamina) + ' jumps left before your stamina runs out.')
        jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        while jump not in ['y', 'n']:
            print("Oops you didn't pick one of the directions given.")
            jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        if jump == 'y':
            for i in range(x - 1, -1, -1):
                if labyrinth[y][i] == 0:
                    tx = i
                    break
                else:
                    tx = 10
            if tx == 10:
                print("This wall doesn't end so you jump back down")
            else:
                temp = x - tx
                print("You jump down at the other end of the wall moving " + str(temp) + " spaces!")
                if abs(bonex - x + temp) < abs(bonex - x):
                    print('The smell of the bone is getting stronger.')
                else:
                    print('The smell of the bone is getting weaker.')
                x = tx
            dog.stamina = dog.stamina - 1
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You don't move and keep your stamina.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'w':
        print('Because of your size you may jump over the wall.')
        print('You have ' + str(dog.stamina) + ' jumps left before your stamina runs out.')
        jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        while jump not in ['y', 'n']:
            print("Oops you didn't pick one of the directions given.")
            jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        if jump == 'y':
            for i in range(y - 1, -1, -1):
                if labyrinth[i][x] == 0:
                    ty = i
                    break
                else:
                    ty = 10
            if ty == 10:
                print("This wall doesn't end so you jump back down")
            else:
                temp = y - ty
                print("You jump down at the other end of the wall moving " + str(temp) + " spaces!")
                if abs(boney - y + temp) < abs(boney - y):
                    print('The smell of the bone is getting stronger.')
                else:
                    print('The smell of the bone is getting weaker.')
                y = ty
            dog.stamina = dog.stamina - 1
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You don't move and keep your stamina.")
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'd':
        print('Because of your size you may jump over the wall.')
        print('You have ' + str(dog.stamina) + ' jumps left before your stamina runs out.')
        jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        while jump not in ['y', 'n']:
            print("Oops you didn't pick one of the directions given.")
            jump = input('Would you like to jump over the wall: (Y)es  (N)o').lower()
        if jump == 'y':
            for i in range(x + 1, 10):
                if labyrinth[y][i] == 0:
                    tx = i
                    break
                else:
                    tx = 10
            if tx == 10:
                print("This wall doesn't end so you jump back down")
            else:
                temp = tx - x
                print("You jump down at the other end of the wall moving " + str(temp) + " spaces!")
                if abs(bonex - x - temp) < abs(bonex - x):
                    print('The smell of the bone is getting stronger.')
                else:
                    print('The smell of the bone is getting weaker.')
                x = tx
            dog.stamina = dog.stamina - 1
            movement(x, y, bonex, boney, dog, step)
        else:
            print("You don't move and keep your stamina.")
            movement(x, y, bonex, boney, dog, step)


def movement(x, y, bonex, boney, dog, step):
    #print(y, x, boney, bonex)
    if x == bonex and y == boney:
        print('Congratulations you have found the bone!')
        print('It took you ' + str(step) + ' steps to reach it!')
        gameslist.append(step)
        gamecount[len(gameslist)] = step
        if len(gameslist) > 1:
            print('For all your games it took you ')
            for i in gamecount:
                print('Game ' + str(i) + ': ' + str(gamecount[i]) + ' turns')
        pa = input('\nDo you want to play again?\n(Y)es  (N)o').lower()
        while pa not in ['y', 'n']:
            print("Oops you didn't pick one of the directions given.")
            pa = input('Do you want to play again?\n(Y)es  (N)o').lower()
        if pa == 'y':
            main()
        else:
            pass
    step = step + 1
    userinput = input('Choose a direction to walk:\n(w):Up  (a):Left  (s):Down  (d):Right').lower()
    while userinput not in ['w', 'a', 's', 'd']:
        print("Oops you didn't pick one of the directions given.")
        userinput = input('Choose a direction to walk:\n(w):Up  (a):Left  (s):Down  (d):Right').lower()
    if userinput == 's':
        if y + 1 == 10:
            print('You have run into the edge of the room so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
        elif y + 1 == boney and x == bonex:
            print('Congratulations you have found the bone!')
            print('It took you ' + str(step) + ' steps to reach it!')
            gameslist.append(step)
            gamecount[len(gameslist)] = step
            if len(gameslist) > 1:
                print('For all your games it took you ')
                for i in gamecount:
                    print ('Game ' + str(i) + ': ' + str(gamecount[i]) + ' turns')
            pa = input('\nDo you want to play again?\n(Y)es  (N)o').lower()
            while pa not in ['y', 'n']:
                print("Oops you didn't pick one of the directions given.")
                pa = input('Do you want to play again?\n(Y)es  (N)o').lower()
            if pa == 'y':
                main()
            else:
                pass
        elif labyrinth[y + 1][x] == 2 and labyrinth[y + 2][x] == 0:
            doggydoor(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y + 1][x] == 3 and labyrinth[y + 3][x] == 3:
            doggytunnel(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y + 1][x] == 4 and labyrinth[y + 2][x] == 0:
            fence(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y + 1][x] == 0:
            if abs(boney - y - 1) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y + 1
            movement(x, y, bonex, boney, dog, step)
        elif dog.stamina != 0:
            walljump(userinput, x, y, bonex, boney, dog, step)
        else:
            print('You have run into a wall so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'a':
        if x - 1 == -1:
            print('You have run into the edge of the room so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
        elif y == boney and x - 1 == bonex:
            print('Congratulations you have found the bone!')
            print('It took you ' + str(step) + ' steps to reach it!')
            gameslist.append(step)
            gamecount[len(gameslist)] = step
            if len(gameslist) > 1:
                print('For all your games it took you ')
                for i in gamecount:
                    print('Game ' + str(i) + ': ' + str(gamecount[i]) + ' turns')
            pa = input('\nDo you want to play again?\n(Y)es  (N)o').lower()
            while pa not in ['y', 'n']:
                print("Oops you didn't pick one of the directions given.")
                pa = input('Do you want to play again?\n(Y)es  (N)o').lower()
            if pa == 'y':
                main()
            else:
                pass
        elif labyrinth[y][x - 1] == 2 and labyrinth[y][x - 2] == 0:
            doggydoor(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x - 1] == 3 and labyrinth[y][x - 3] == 3:
            doggytunnel(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x - 1] == 4 and labyrinth[y][x - 2] == 0:
            fence(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x - 1] == 0:
            if abs(bonex - x + 1) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x - 1
            movement(x, y, bonex, boney, dog, step)
        elif dog.stamina != 0:
            walljump(userinput, x, y, bonex, boney, dog, step)
        else:
            print('You have run into a wall so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'w':
        if y - 1 == -1:
            print('You have run into the edge of the room so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
        elif y - 1 == boney and x == bonex:
            print('Congratulations you have found the bone!')
            print('It took you ' + str(step) + ' steps to reach it!')
            gameslist.append(step)
            gamecount[len(gameslist)] = step
            if len(gameslist) > 1:
                print('For all your games it took you ')
                for i in gamecount:
                    print('Game ' + str(i) + ': ' + str(gamecount[i]) + ' turns')
            pa = input('\nDo you want to play again?\n(Y)es  (N)o').lower()
            while pa not in ['y', 'n']:
                print("Oops you didn't pick one of the directions given.")
                pa = input('Do you want to play again?\n(Y)es  (N)o').lower()
            if pa == 'y':
                main()
            else:
                pass
        elif labyrinth[y - 1][x] == 2 and labyrinth[y - 2][x] == 0:
            doggydoor(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y - 1][x] == 3 and labyrinth[y - 3][x] == 3:
            doggytunnel(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y - 1][x] == 4 and labyrinth[y - 2][x] == 0:
            fence(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y - 1][x] == 0:
            if abs(boney - y + 1) < abs(boney - y):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            y = y - 1
            movement(x, y, bonex, boney, dog, step)
        elif dog.stamina != 0:
            walljump(userinput, x, y, bonex, boney, dog, step)
        else:
            print('You have run into a wall so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
    if userinput == 'd':
        if x + 1 == 10:
            print('You have run into the edge of the room so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)
        elif y == boney and x + 1 == bonex:
            print('Congratulations you have found the bone!')
            print('It took you ' + str(step) + ' steps to reach it!')
            gameslist.append(step)
            gamecount[len(gameslist)] = step
            if len(gameslist) > 1:
                print('For all your games it took you ')
                for i in gamecount:
                    print('Game ' + str(i) + ': ' + str(gamecount[i]) + ' turns')
            pa = input('\nDo you want to play again?\n(Y)es  (N)o').lower()
            while pa not in ['y', 'n']:
                print("Oops you didn't pick one of the directions given.")
                pa = input('Do you want to play again?\n(Y)es  (N)o').lower()
            if pa == 'y':
                main()
            else:
                pass
        elif labyrinth[y][x + 1] == 2 and labyrinth[y][x + 2] == 0:
            doggydoor(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x + 1] == 3 and labyrinth[y][x + 3] == 3:
            doggytunnel(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x + 1] == 4 and labyrinth[y][x + 2] == 0:
            fence(userinput, x, y, bonex, boney, dog, step)
        elif labyrinth[y][x + 1] == 0:
            if abs(bonex - x - 1) < abs(bonex - x):
                print('The smell of the bone is getting stronger.')
            else:
                print('The smell of the bone is getting weaker.')
            x = x + 1
            movement(x, y, bonex, boney, dog, step)
        elif dog.stamina != 0:
            walljump(userinput, x, y, bonex, boney, dog, step)
        else:
            print('You have run into a wall so you stay in the same position.')
            movement(x, y, bonex, boney, dog, step)


def main():
    step = 0
    x, y, bonex, boney = postition()
    while x == bonex and y == boney:
        x, y, bonex, boney = postition()
    print('Welcome to Game of Bones!')
    print('Select a breed of dog to start.')
    breedindicator = input('(G):Greyhound  (B):Beagle \n(L):Labrador   (C):Chihuahua').upper()
    while breedindicator not in ['G', 'B', 'L', 'C']:
        print("Oops you didn't pick one of the breeds given.")
        print('Select a breed of dog to start.')
        breedindicator = input('(G):Greyhound  (B):Beagle \n(L):Labrador   (C):Chihuahua').upper()
    if breedindicator == 'G':
        dog = dogtype('Greyhound', 4, 3)
        print('You have chosen House ' + dog.breed + '!')
    elif breedindicator == 'B':
        dog = dogtype('Beagle', 2, 0)
        print('You have chosen House ' + dog.breed + '!')
    elif breedindicator == 'L':
        dog = dogtype('Labrador', 3, 1)
        print('You have chosen House ' + dog.breed + '!')
    elif breedindicator == 'C':
        dog = dogtype('Chihuahua', 1, 0)
        print('You have chosen House ' + dog.breed + '!')
    print("You have now been placed in a labyrinth with no sight.\nYou must try to navigate your way through the "
          "labyrinth to find a bone only using your sense of smell. ")
    movement(x, y, bonex, boney, dog, step)


main()
