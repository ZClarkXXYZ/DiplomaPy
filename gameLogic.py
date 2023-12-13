def findPossibleSupports(board, currentPiece):
    '''


    :param board: The board of Diplocacy, type is dictionary
    :param currentPiece: written as X_YYY, where YYY is used as the location of the peice, which is also a key of the dictionary board
    :return: A list of pieces that can be target of support by currentPiece
    '''

    # get easy to calculate possible moves
    possible_moves = board[currentPiece[:3]][5].copy()
    if currentPiece[-1] == 'A':
        possible_moves = possible_moves + board[currentPiece[:3]][3]
        for i_possible_move in range(len(possible_moves)):
            if len(possible_moves[i_possible_move]) != 3:
                possible_moves[i_possible_move] = possible_moves[i_possible_move][-3:] #Slice it for Army Units incase is is a _NS_ coast space
    if currentPiece[-1] == 'F':
        possible_moves = possible_moves + board[currentPiece[:3]][4]

    # remove moves with no pieces on it
    #print(possible_moves)
    removeList = []
    for move in possible_moves:
        if board[move][-1] == 'None':
            removeList.append(move)
            #print(move)
            #print(board[move][-1])
    for move in removeList:
        possible_moves.remove(move)
    return (possible_moves)



def findPossibleMoves(board, currentPiece):
    '''


    :param board: The board of Diplocacy, type is dictionary
    :param currentPiece: written as X_YYY, where YYY is used as the location of the peice, which is also a key of the dictionary board
    :return: A list of possible moves
    '''

    #get easy to calculate possible moves
    possible_moves = board[currentPiece[:3]][5].copy()
    #print(possible_moves)
    if currentPiece[-1] == 'A':
        possible_moves = possible_moves + board[currentPiece[:3]][3]

        for i_possible_move in range(len(possible_moves)):
            if len(possible_moves[i_possible_move]) != 3:
                possible_moves[i_possible_move] = possible_moves[i_possible_move][-3:] #Slice it for Army Units incase is is a _NS_ coast space

    if currentPiece[-1] == 'F':
        possible_moves = possible_moves + board[currentPiece[:3]][4]

    #remove moves with your own color on it, since you can't move there
    removeList = []
    for move in possible_moves:
        if board[move[-3:]][-1][-2] == currentPiece[-2]:
            removeList.append(move)
    for move in removeList:
        possible_moves.remove(move)
    return(possible_moves)

def calculate_actions(action_list):
    '''
    :arg: action_list: a long list of 'actions' that are worked on to determine what happens on the given round

    :return: (Missing), gives a list with the same length as action_list, which has 'True' or 'False' depending on if a given action succeeded or not.

    This is the main function that finds out what happens based on what players choose to do
    Actions are coded as:
    H_{loc_id}: Hold at given location

    M_{loc_id1}_{loc_id2}: Move Unit to location 1 from location 2

    C_{loc_id1}_{loc_id2}_{loc_id3}_...{loc_idN} : Move Army Unit TO location 1 FROM location 2, where the rest of the loc_id are the locations of the fleets that might be attacked
    f_{loc_id} : Used for calculating whether a convoy part succeeds. Created from each part of C_{id}_{id2}_{id3}_{id4}_{....} from id 3 to id n. Has a base power of 1

    S_{loc_id1}_({Action_command} : Unit at location 1 gives +1 power to action {Action_command}. If it exist, then it gets +1 power within actionLocations

    b_loc_id:   Everything at this location is determined to fail. Only found within actionLocations, not in actions_list. Used in cases where units of equal power move to same location, but it is (now) empty


    The order it will look at is:
    1. Find out which spaces players are not moving from (Hold). Give base power 1 to action
    2. Find out which spaces players are moving to. Give power 1 to action
    3. Calculate Convoys and their paths? (?)
    4. Find out which ones support those all these moves. At location of support, give base power 0 as if it was a holding action.
    5. Resolve All Uncontested supports to give +1 power to target action
    6. Contested supports are calculated. Remove supports that fail, give power from those that succeed
    7. Make list of successes and fails based on whether they are in the dictionary actionLocations. Return the list.


    What will be returned is a list of "Succeed", and "Fail" depending whether X action at list succeeded. The order is the same as the list
    Seperate function will take action list and list of successes to determine what happens to the board
    '''

    actionLocations = {}    #Each Key is a location Id. The list will have alternating commands and power of that command.
    #Example: {'NAF': ['H_NAF', 2, M_
    #At the end of calculation, at the location (key), the final winning action will be the only item in that key's list, along with the power

    supportCommands = []    #List of support commands that will check at the end of calculation if the support succeeds
    moveCommands = []       #List of move commands used for more complicate "bounce" mechancics
    convoyCommands = []     #List of convoy moves used for determine if the full convoy succeeds in moving the unit

    #PART1: Go Through All Commands and put them in actionLocations
    for action_i in range(len(action_list)):
        action = action_list[action_i]
        if action[2:5] not in actionLocations.keys(): #Create location key if it does not exist
            actionLocations[action[2:5]] = []

        if action[0] != 'S':
            actionLocations[action[2:5]] = actionLocations[action[2:5]] + [action, 1]
            if action[0] == 'M':
                    moveCommands.append(action)
            if action[0] == 'C': #Create part of convoy chain at each location with base power 1
                convoyCommands.append(action)
                convoy_i = 10    #Starting index for extraction the location_id of each fleet involved in the convoy
                for c_location in range(((len(action[10:])) +1) /4): #Locations of each fleet is given in chunks of 4: 'XYZ_', with the exception of the end, which is a chuck of 3.
                    f_location = action[convoy_i:convoy_i + 3]
                    if action[convoy_i:convoy_i + 3] not in actionLocations.keys():  # Create location key if it does not exist
                        actionLocations[action[convoy_i:convoy_i + 3]] = []

                    actionLocations[action[convoy_i:convoy_i + 3]] = actionLocations[action[convoy_i:convoy_i + 3]] + ['f_' + action[convoy_i:convoy_i + 3], 1]
                    convoy_i += 4

        else: #It is a support action
            actionLocations[action[2:5]] = actionLocations[action[2:6]] + [action,0]
            supportCommands.append(action)

    #PART2: Check Successes of Supports. The method involves always giving +1 power to target, but then take it away if support location is targeted

    supportCommandRemoval = []
    tested_all_supports = True
    for support_i in range(len(supportCommands)):
        support = supportCommands[support_i]
        tested_all_supports = True

        if support[8:11] in actionLocations.keys(): #If there is nothing holding in that location or moving to that location, then it fails by default
            index_of_supported_act = get_index_of_target(support, actionLocations)

            if index_of_supported_act != None:
                actionLocations[support[8:11]][index_of_supported_act + 1] += 1#increase power of the action by one
            else:
                supportCommandRemoval.append(support)
                index_of_support_act = actionLocations[support[2:5]].index(support)
                actionLocations[support[2:5]][index_of_support_act + 1] += 1  # give +1 power to the location that was the supporter
                actionLocations[support[2:5]][index_of_support_act] = 'H' + actionLocations[support[2:5]][index_of_support_act][1:]  # changes action into holding for the purposes of "Movement calculations"
        else:
            supportCommandRemoval.append(support)
            index_of_support_act = actionLocations[support[2:5]].index(support)
            actionLocations[support[2:5]][index_of_support_act + 1] += 1  # give +1 power to the location that was the supporter
            actionLocations[support[2:5]][index_of_support_act] = 'H' + actionLocations[support[2:5]][index_of_support_act][1:]  # changes action into holding for the purposes of "Movement calculations"

    for support_to_remove in supportCommandRemoval:
        supportCommands.remove(support_to_remove)

    while (not tested_all_supports) and supportCommands != []:
        supportCommandRemoval = []

        #figure out which supports need to be taken back. Give the location of the support +1 for holding, and -1 to target location
        for support_i in range(len(supportCommands)):
            support = supportCommands[support_i]

            if undoSupport(support, actionLocations):
                tested_all_supports = False
                supportCommandRemoval.append(support)

                index_of_supported_act = get_index_of_target(support, actionLocations)
                if index_of_supported_act != None:
                    actionLocations[support[8:11]][index_of_supported_act + 1] = actionLocations[support[8:11]][index_of_supported_act + 1] - 1

                index_of_support_act = actionLocations[support[2:5]].index(support)
                actionLocations[support[2:5]][index_of_support_act + 1] += 1 #give +1 power to the location that was the supporter
                actionLocations[support[2:5]][index_of_support_act] = 'H' + actionLocations[support[2:5]][index_of_support_act][1:] #changes action into holding for the purposes of "Movement calculations"

        for support_to_remove in supportCommandRemoval:
            supportCommands.remove(support_to_remove)


    #PART3: Convoys. Check each chain to make sure they aren't attack with more power than its power, otherwise the convoy fails.


    #Part 4: Calculate success of moves and holds
    for location in actionLocations.keys():
        pass
        #if len(actionLocation[location]) != 2:  #If location is contested by another action

    #Part 5: Calculate Convoy Success


    #PART FINAL: Compare powers at each location


def undoSupport(support, actionLocations):
    if len(actionLocations[support[2:5]]) == 2: # If there are no movement options against this location, then never undo support.
        return False
    for action in actionLocations[2:5]:
        if action[0] == 'M' or action [0] == 'C': #If is either a movement option against this location or a convoy targeting this location.
            pass

def get_index_of_target(support, actionLocations):
    '''

    :param support: a location, written like XYZ, which is a target of a support action
    :param actionLocations:


    :return:
    '''


    if support[6:] in actionLocations[support[2:5]]:  # if the exact command is in the action, then this is pretty fast
        return actionLocations[support[2:5]].index(support[6:])
    if support[6] == 'M':  # Support can only have two main types: 'M' or 'H'. if it was 'M', then since the first if statement didn't trigger, that means the support of the movement type failed.
        return None

    for action_target_i in actionLocations[support[2:5]]:  # Check if the target is a convoy or support action instead, which would have been 'S_XXX' or 'f_YYY'
        action_target = actionLocations[support[2:5]][action_target_i]
        if 'H' + action_target[1:5] == support[6:11]:
            return action_target_i
    # It searched through, and found nothing
    return None






def testing_actions():
    actions1 = ['']


if __name__ == '__main__':
    testing_actions()

