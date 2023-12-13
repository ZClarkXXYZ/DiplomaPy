#package imports
from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image

import string

#imports from other scripts
from gameBoard import makeBoard, getColorCode, getSupplyCenters, getPieceLocations
from UIenhancements import *
from gameLogic import *


def checkForAllMovesDone(playerProfiles):
    print('CheckingMoves')
    if playerProfiles['piecesToMove'] == [[],[],[],[],[],[],[]]:
        print('If statement Triggered')
        #create list move moves to send to calculate_actions(actionList)
        actionList = []
        for i_moveList in range(len(playerProfiles['Moves'])):
            moveList = playerProfiles['Moves'][i_moveList]
            actionList = actionList + moveList
        print(actionList)

        print('BASICALLY: everything past here is incomplete')
        calculate_actions(actionList)

def resetPlayer(playerProfiles, dynamicLabel_piecesLeft_text):
    global currentPlayer
    i_currentPlayer = playerProfiles['names'].index(currentPlayer)

    playerProfiles['piecesToMove'][i_currentPlayer] = playerProfiles['pieceLocations'][i_currentPlayer][:]
    dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))




def messageRead(playerProfiles):
    global currentPlayer
    i_currentPlayer = playerProfiles['names'].index(currentPlayer)

    messages = '\n'.join(playerProfiles[playerProfiles['armies'][i_currentPlayer]])

    messagebox.showinfo('messages',messages)



def messagePlayer(playerProfiles):
    global currentPlayer

    players = playerProfiles['names'].copy()
    players.remove(currentPlayer)

    player_to_message = 'None'
    while player_to_message not in players:
        player_to_message = simpledialog.askstring("Choose Player", 'Who to Message? ' + str(players))
    writtenMessage = currentPlayer + ': \n' + simpledialog.askstring("Write Message", 'Type your message')

    i_messagedPlayer = playerProfiles['names'].index(player_to_message)
    playerProfiles[playerProfiles['armies'][i_messagedPlayer]].append(writtenMessage)

def useUnit(playerProfiles, board, dynamicLabel_piecesLeft_text):

    global currentPlayer
    i_currentPlayer = playerProfiles['names'].index(currentPlayer)

    #print(playerProfiles['Moves'][i_currentPlayer])

    currentPiece = 'None'
    if len(playerProfiles['piecesToMove'][i_currentPlayer]) > 0:
        while currentPiece == 'None':
            currentPiece = simpledialog.askstring("Choose Unit", 'Use Which Unit?' + str(playerProfiles['piecesToMove'][i_currentPlayer]))
            if currentPiece in playerProfiles['piecesToMove'][i_currentPlayer]:
                tempListCopy = playerProfiles['piecesToMove'][i_currentPlayer].copy()
                tempListCopy.remove(currentPiece)
                playerProfiles['piecesToMove'][i_currentPlayer] = tempListCopy
                #print(playerProfiles)
            else:
                currentPiece = 'None'

        currentAction = 'None'
        if currentPiece[-1] == 'A':
            possibleActionsString = 'M: Move, H: Hold, S: Support, C: Convoy (Convoy is disabled in this version)'
            possibleActions = ['M', 'H', 'S']

        else:
            possibleActionsString = 'M: Move, H: Hold, S: Support'
            possibleActions = ['M', 'H', 'S']
        while currentAction == 'None':
            currentAction = simpledialog.askstring("Choose Action", 'What action would unit at ' + currentPiece[:3] + ' do? ' + possibleActionsString)
            if currentAction not in possibleActions:
                 currentAction = 'None'


        if currentAction == 'M':
            possibleMoves = findPossibleMoves(board, currentPiece)

            chosenMove = 'None'
            while chosenMove not in possibleMoves:
                chosenMove = simpledialog.askstring("Choose Location", 'Where to move piece to?\n' + str(possibleMoves))
            playerProfiles['Moves'][i_currentPlayer].append(currentAction + '_' + chosenMove + '_' + currentPiece[:3])
            dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))

            checkForAllMovesDone(playerProfiles)


        elif currentAction == 'H':
            playerProfiles['Moves'][i_currentPlayer].append(currentAction + '_' + currentPiece[:3])
            dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))

            checkForAllMovesDone(playerProfiles)


        elif currentAction == 'S':
            possibleMoves = findPossibleSupports(board, currentPiece)

            if possibleMoves == []:
                playerProfiles['Moves'][i_currentPlayer].append(currentAction + '_' + currentPiece[:3])
                messagebox.showwarning("Can't Support Pieces", "There are no possible unit to support, action changed to a Hold")
                dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))

                checkForAllMovesDone(playerProfiles)


            chosenMove = 'None'
            while chosenMove not in possibleMoves:
                chosenMove = simpledialog.askstring("Choose Location", 'Where is Unit to support?\n' + str(possibleMoves))
            chosenMove = chosenMove + str(board[chosenMove][-1])

            chosenSupport = 'None'
            supportTypes = ['H', 'M']
            while chosenSupport == 'None':
                chosenSupport = simpledialog.askstring("Choose Location", 'What type of action to support?\n' + str(supportTypes))
                if chosenSupport not in supportTypes:
                    chosenSupport = 'None'
            if chosenSupport == 'M':
                print(chosenMove)
                possibleSuportedMoves = findPossibleMoves(board, chosenMove)

                chosenSupportedMove = 'None'
                while chosenSupportedMove == 'None':
                    chosenSupportedMove = simpledialog.askstring("Choose Move Location", 'Where is the supported Piece Moving To?\n' + str(possibleSuportedMoves))
                    if chosenSupportedMove not in possibleSuportedMoves:
                        chosenSupportedMove = 'None'
                playerProfiles['Moves'][i_currentPlayer].append(currentAction + '_' + currentPiece[:3] + '_M_' + chosenSupportedMove[-3:] + '_' + chosenSupport[-3:])
                dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))



            else:
                playerProfiles['Moves'][i_currentPlayer].append(currentAction + '_' + currentPiece[:3] + '_H_' + chosenMove)
                dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))

                checkForAllMovesDone(playerProfiles)


        elif currentAction == 'C': # NOT AVAILABLE
            pass



def changePlayer(playerProfiles, btn_use_unit, btn_message, btn_resetPlayer, dynamicLabel_player_text, dynamicLabel_pieces_text, dynamicLabel_piecesLeft_text, btn_read_message):

    global currentPlayer
    #print(currentPlayer)
    if currentPlayer == 'None':
        while currentPlayer == 'None':
            nextPlayer = simpledialog.askstring("Change Player ", 'Which Player Are You? ' + str(playerProfiles['names']))
            if nextPlayer in playerProfiles['names']:
                currentPlayer = nextPlayer

                btn_use_unit['state'] = 'normal'
                btn_message['state'] = 'normal'
                btn_resetPlayer['state'] = 'normal'
                btn_read_message['state'] = 'normal'

                #print(playerProfiles)
                i_currentPlayer = playerProfiles['names'].index(currentPlayer)

                dynamicLabel_player_text.set('Current Player: ' + currentPlayer)
                dynamicLabel_pieces_text.set('Your Piece Locations: ' + str(playerProfiles['pieceLocations'][i_currentPlayer]))
                dynamicLabel_piecesLeft_text.set('Pieces Left to Move: ' + str(playerProfiles['piecesToMove'][i_currentPlayer]))


    else: # make it so that it is no player current
        currentPlayer = 'None'
        btn_use_unit['state'] = 'disabled'
        btn_message['state'] = 'disabled'
        btn_resetPlayer['state'] = 'disabled'
        btn_read_message['state'] = 'disabled'

        dynamicLabel_player_text.set('Current Player: ' + currentPlayer)
        dynamicLabel_pieces_text.set('...')
        dynamicLabel_piecesLeft_text.set('...')



def makeBoardImage(playerProfiles, baseImg):
    baseImgCopy = baseImg.copy()

    from gameBoard import getColorCode
    colorCode = getColorCode()

    #First, place the claimed supply centers onto the board image
    i_sc = 0
    for army in playerProfiles['armies']:
        for supplyC in playerProfiles['supplyCenters'][i_sc]:
            image_file_to_paste = getImageFileCode(colorCode[army][0]) #image file should only be based on the color of the owner. This is a 1 character input.
            pic_location_sc = getPictureLocation_SupplyCenter(supplyC)
            image_to_paste = Image.open(image_file_to_paste)
            image_to_paste = image_to_paste.resize((16,16))
            baseImgCopy.paste(image_to_paste, pic_location_sc, image_to_paste)
        i_sc = i_sc + 1

    #Next, place image pieces on image
    #print(playerProfiles['pieceLocations'])
    for pieceList in playerProfiles['pieceLocations']:
        for piece in pieceList:
            #print(piece)
            image_file_to_paste = getImageFileCode(piece[-2:])
            piece_loc = getPictureLocation_PieceLocation(piece[:3])

            image_to_paste = Image.open(image_file_to_paste)
            if piece[-1] == 'A':
                image_to_paste = image_to_paste.resize((12,12))
            else:
                image_to_paste = image_to_paste.resize((20, 20))
            baseImgCopy.paste(image_to_paste, piece_loc, image_to_paste)

    return(baseImgCopy)







def gameStartMain(playerProfiles, board, root):
    #print(playerProfiles)

    baseImg = Image.open('MAPfinalVersion2.png')
    img_size = (300, 300)
    baseImg.resize(img_size)
    boardImg = ImageTk.PhotoImage(makeBoardImage(playerProfiles, baseImg))


    #root = Tk()
    root.title('Diplomacy Game')
    board_label = Label(root, image=boardImg)
    board_label.grid(row=0, column=0)


    global currentPlayer
    currentPlayer = 'None'
    dynamicLabel_player_text = StringVar()
    dynamicLabel_player_text.set('Current Player: ' + currentPlayer)
    dynamicLabel_player = Label(root, textvariable=dynamicLabel_player_text)
    dynamicLabel_player.grid(row=7, column=5)

    dynamicLabel_pieces_text = StringVar()
    dynamicLabel_pieces_text.set('...')
    dynamicLabel_pieces = Label(root, textvariable=dynamicLabel_pieces_text)
    dynamicLabel_pieces.grid(row=6, column=5)

    dynamicLabel_piecesLeft_text = StringVar()
    dynamicLabel_piecesLeft_text.set('...')
    dynamicLabel_piecesLeft = Label(root, textvariable=dynamicLabel_piecesLeft_text)
    dynamicLabel_piecesLeft.grid(row=5, column=5)

    #BUTTONS: Change player, Choose Piece then Choose Action/place, Message Player, undo all moves?
    btn_change_player = Button(root, text='Change Current Player', command=lambda : changePlayer(playerProfiles, btn_use_unit, btn_message, btn_resetPlayer, dynamicLabel_player_text, dynamicLabel_pieces_text, dynamicLabel_piecesLeft_text, btn_read_message))
    btn_change_player.grid(row=4, column=5)

    btn_use_unit = Button(root, text='Command Unit', command=lambda : useUnit(playerProfiles, board, dynamicLabel_piecesLeft_text), state=DISABLED)
    btn_use_unit.grid(row=3, column=5)

    btn_message = Button(root, text='Message', command=lambda : messagePlayer(playerProfiles), state=DISABLED)
    btn_message.grid(row=2, column=5)

    btn_read_message = Button(root, text='Read Messages',command=lambda : messageRead(playerProfiles), state = DISABLED)
    btn_read_message.grid(row=2, column=6)

    btn_resetPlayer = Button(root, text='Reset All Moves', command=lambda : resetPlayer(playerProfiles, dynamicLabel_piecesLeft_text), state=DISABLED)
    btn_resetPlayer.grid(row=1, column=5)



    root.mainloop()

def createPlayerProfiles(playerNames, armies, root):
    '''




    Create Player profile that includes:
    1. Name of player
    2. Name of team (Russia, Turkey, France, Italy, Hungary, Germany, England)
    3. Supply Centers (everything here and after are initially empty on creation on player profile)
    4. Piece locations + type [PFleet_Loc, PArmy_Loc, PArmy_Loc,]...
    5. Pieces to move (starts as same as Piece locations
    6-12. Messages from others player (does not send messages to self)
    '''
    board = makeBoard()
    supplyCenters = getSupplyCenters(board, armies)
    pieceLocations = getPieceLocations(board, armies)


    playerProfiles = {
        'names': playerNames,
        'armies': armies,
        'supplyCenters': supplyCenters,
        'pieceLocations': pieceLocations[:],
        'piecesToMove': pieceLocations[:],
        'Russia': [],
        'Turkey': [],
        'France': [],
        'Italy': [],
        'Hungary': [],
        'Germany': [],
        'England': [],
        'Moves': [[],[],[],[],[],[],[]]

    }

    #print(playerProfiles)
    #print(playerProfiles['pieceLocations'] is playerProfiles['piecesToMove'])

    gameStartMain(playerProfiles, board, root)

def playerInput(playerNames, armies, availableArmies, armyDisplayText, buttonText, start_game_btn, add_player_btn):
    if len(playerNames) != 7:
        playerName = None
        newPlayerName = False
        while newPlayerName == False:
            playerName = simpledialog.askstring("Name: ", "Enter your player Name")
            if playerName not in playerNames and playerName not in string.whitespace:
                print(playerName)
                playerNames.append(playerName)
                newPlayerName = True
            else:
                messagebox.showwarning("Name Taken", "Try Another Name")

        chosenArmy = None
        while chosenArmy == None:
            chosenArmy = simpledialog.askstring("Chose your army from the list given",
                                               "Available Armies: " + ' , '.join(availableArmies))
            if chosenArmy not in availableArmies:
                chosenArmy = None
                messagebox.showwarning("Army Unavailable", "Did you spell it right?")
            else:
                armies.append(chosenArmy)
                availableArmies.remove(chosenArmy)
        armyDisplayText.set('Players: ' + ' , '.join(playerNames) + '\nArmies: ' + ' , '.join(armies))
        if len(playerNames) != 7:
            buttonText.set("Add New Player (" + str(7-len(playerNames)) + ' More Needed)')
        else:
            buttonText.set('7 Player Game Ready!')
            start_game_btn['state'] = 'normal'
            add_player_btn['state'] = 'disabled'
    else:
        buttonText.set('7 Player Game Ready!')
        start_game_btn['state'] = 'normal'
        add_player_btn['state'] = 'disabled'



def main(testMode):
    playerNames = []
    armies = []
    availableArmies = ['Russia', 'Turkey', 'France', 'Italy', 'Hungary', 'Germany', 'England']

    root = Tk()
    root.title('Python Diplomacy: 7 Player Setup')
    armyDisplayText = StringVar()
    armyDisplayText.set('Players: ' + ' , '.join(playerNames) + '\nArmies: ' + ' , '.join(armies))
    armyDisplay = Label(root, textvariable=armyDisplayText)

    armyDisplay.grid(row=0,column=0)

    buttonText = StringVar()
    buttonText.set("Add New Player (" + str(7-len(playerNames)) + ' More Needed)')
    add_player_btn = Button(root, textvariable=buttonText, command=lambda : playerInput(playerNames, armies, availableArmies, armyDisplayText, buttonText, start_game_btn, add_player_btn), padx=20)
    add_player_btn.grid(row=1, column=0)

    start_game_btn = Button(root, text='Start Game', command=root.quit, state=DISABLED)
    start_game_btn.grid(row=2, column=0)

    if testMode:    #The only purpose this has is to speed up testing of things outside this "main" function's area of UI
        print('testMode is enabled in main. Disable it!')
        playerNames = ['Russ', 'Turk', 'Fran', 'Italy', 'Hun', 'Ger', 'Eng']
        armies = ['Russia', 'Turkey', 'France', 'Italy', 'Hungary', 'Germany', 'England']
    root.mainloop()
    print('game set')

    armyDisplay.destroy()
    add_player_btn.destroy()
    start_game_btn.destroy()
    #root.quit()
    
    createPlayerProfiles(playerNames, armies, root)

#main(True) #USE THIS TO SPEED UP TESTING
main(False)