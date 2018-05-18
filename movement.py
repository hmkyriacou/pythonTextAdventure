global x,y
x,y = 0,0

def move():
    global direc
    direc.upper()
    global x,y
    if (direc == 'NORTH'):
        y = y + 1
    if (direc == 'SOUTH'):
        y = y - 1
    if (direc == 'WEST'):
        x = x - 1
    if (direc == 'EAST'):
        x = x + 1
        
def actionInput():
    global command
    global ACTIONS
    commandWords = command.split(' ')
    commandWordsTest = commandWords
    for x in range(len(commandWords)):
        for y in range(len(ACTIONS)):
            if (commandWordsTest[x].upper() == ACIONS[y]):
                return commandWords[x]
