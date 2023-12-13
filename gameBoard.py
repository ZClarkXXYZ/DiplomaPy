
def getPieceLocations(board, armies):
    pieceLocations = []
    colorCode = getColorCode()

    for army in armies:
        army_locations_for_given_army = []
        for location in board.keys():
            #print(location)
            if board[location][7][-2] == colorCode[army][0]:
                army_locations_for_given_army.append(board[location][1] + '_' + board[location][7])
        pieceLocations.append(army_locations_for_given_army)
    return(pieceLocations)
def getSupplyCenters(board, armies):
    colorCode = getColorCode()
    supplyCenters = []

    for army in armies:
        supply_center_for_given_army = []
        for location in board.keys():
            #print(location)
            if board[location][6] and board[location][7][-2] == colorCode[army][0]:
                supply_center_for_given_army.append(board[location][1])
                #print(supply_center_for_given_army)
        supplyCenters.append(supply_center_for_given_army)

    #print(supplyCenters)
    return supplyCenters

def getColorCode(): #Convert Countries into colors. Function for convenience
    colorCode = {
        'Russia': ['W'],
        'Turkey': ['Y'],
        'France': ['B'],
        'Italy': ['G'],
        'Hungary': ['R'],
        'Germany': ['O'],
        'England': ['P']
    }
    return colorCode
def makeBoard():
    """TODO: Make Here

    Instead of making BoardSpace object, which would be hard to work with, a dictionary is set up with the following information
    key is same as location_id : name, location_id, space_type, land_connects, sea_connects, coast_connects, supplyC, piece_on

    Here is what each "attribute" does:
    name:                #string, gives full name of space
    location_id          #string, 3 letters. Fast, simple reference of the space
    space_type           #string, "Sea, Land, Coast, or _NS_Coast
    land_connects        #list, Used to find what spaces can be reached by Army Units
    sea_connects         #list For MultiCoast, starts with '_X_', where X is N, S. Used to find what spaces can be reached by Fleet Units.
    coast_connects       #list For MultiCoast, starts with '_X_', where X is N, S. Used to find what spaces can be reached by any Unit
    supplyC = supplyC    #Boolean, tells whether there is a supply center on the given space.
    piece_on             #string, If there is none, then 'None', otherwise, Starting with a color, 'W' (White, Russia), Y (Yellow, Turkey), 'B' (Blue, France), 'G' (Green, Italy), 'R' (Red, Austria/Hungary), 'O' (Orange, Germany, 'P' (Purple, England). Then has either 'A' (Army) or 'F' (Fleet). However, if it is a multi-coast, then at start it might has something like '_N_ to show what coast the Fleet is on. "N", or "S" for North, South


    """

    #If I was smart, I might set this all in a separate file and important it in instead of keeping it in code.
    board = {
        'NAO': ['North_Atlantic_Ocean', 'NAO', 'Sea', [], ['NWG', 'IRI', 'MID'], ['CLY', 'LVP'], False, 'None'],
        'NWG': ['Norwegian_Sea', 'NWG', 'Sea', [], ['NAO', 'NTH', 'BAR'],['CLY', 'EDI', 'NWY'], False, 'None'],
        'BAR': ['Barents_Sea', 'BAR', 'Sea', [], ['NWG'], ['NWY', '_N_STP'], False, 'None'],
        'CLY': ['Clyde', 'CLY', 'Coast', [], ['NAO', 'NWG'], ['LVP', 'EDI'], False, 'None'],
        'EDI': ['Edinburgh', 'EDI', 'Coast', ['LVP'], ['NWG', 'NTH'], ['CLY', 'YOR'], True, 'PF'],   #England (P) supply center, starts with Fleet
        'NTH': ['North_Sea', 'NTH', 'Sea', [], ['NWG','SKA', 'HEL'], ['EDI','YOR','NWY','LON','BEL','HOL'], False, 'None'],
        'NWY': ['Norway', 'NWY', 'Coast', ['FIN'], ['NWG','BAR', 'NTH','SKA'], ['SWE', '_N_STP'],  True, 'None'],   #neutral supply center
        'STP': ['St_Petersburg', 'STP', '_NS_Coast', ['MOS'], ['_N_BAR', '_S_LYO'], ['_N_NWY', '_S_FIN', '_S_LVN'], True, '_S_WF'], #Russia (W) supply center, starts with Fleet on South Coast
        'MID': ['Mid_Atlantic_Ocean', 'MID', 'Sea', [], ['NTH', 'IRI', 'ENG', 'WES'], ['BRE', 'GAS', '_N_SPA', '_S_SPA', 'POR', 'NAF'], False, 'None'],
        'IRI': ['Irish_Sea', 'IRI', 'Sea', [], ['NAO', 'MID', 'ENG'], ['LVP', 'WAL'], False, 'None'],
        'LVP': ['Liverpool', 'LVP', 'Coast', ['EDI','YOR'], ['NAO', 'IRI'], ['WAL','CLY'], True, 'PA'],   #England (P) supply center, starts with Army
        'YOR': ['Yorkshire', 'YOR', 'Coast', ['WAL', 'LVP'], ['NTH'], ['LON','EDI'], False, 'None'],
        'SKA': ['Skagerrak', 'SKA', 'Sea', [], ['NTH'], ['NWY','SWE','DEN'], False, 'None'],
        'SWE': ['Sweden', 'SWE', 'Coast', [], ['SKA', 'BAL','BOT'], ['DEN', 'NWY','FIN'], True, 'None'],    #neutral supply center
        'FIN': ['Finland', 'FIN', 'Coast', ['NWY'], ['BOT'], ['SWE','_S_STP'], False, 'None'],
        'WAL': ['Whales', 'WAL', 'Coast', ['YOR'], ['IRI','ENG'], ['LVP','LON'], False, 'None'],
        'LON': ['London', 'LON', 'Coast', [], ['NTH','ENG'], ['YOR','WAL'], True, 'PF'],    #England (P) supply center, starts with Fleet
        'ENG': ['English_Channel', 'ENG', 'Sea', [], ['ENG','NTH'], ['YOR','WAL'], False, 'None'],
        'BEL': ['Belgium', 'BEL', 'Coast', ['BUR','RUH'], ['ENG','NTH'], ['PIC','HOL'], True, 'None'],     #neutral supply center
        'HOL': ['Holland', 'HOL', 'Coast', ['RUH'], ['HEL','NTH',], ['BEL','KIE'], True, 'None'],   #neutral supply center
        'HEL': ['Helgoland_Bight', 'HEL', 'Sea', [], ['NTH'], ['KIE','DEN','HOL'], False, 'None'],
        'DEN': ['Denmark', 'DEN', 'Coast', [], ['SKA','HEL','BAL','NTH'], ['KIE','SWE'], True, 'None'], #neutral supply center
        'BAL': ['Baltic_Sea', 'BAl', 'Sea', [], ['BOT'], ['DEN','SWE','BER','PRU','LVN','KIE'], False, 'None'],
        'BOT': ['Gulf_of_Bothnia', 'BOT', 'Sea', [], ['BAL'], ['SWE','FIN','_S_STP','LVN'], False, 'None'],
        'BRE': ['Brest', 'BRE', 'Coast', ['PAR'], ['MID','ENG'], ['GAS','PIC'], True, 'BF'], #France (B) supply center, starts with Fleet
        'PAR': ['Paris', 'PAR', 'Land', ['BRE','PIC','BUR','GAS'], [], [], True, 'BA'], #France (B) supply center, starts with Army
        'PIC': ['Picardy', 'PIC', 'Coast', ['PAR','BUR'], ['ENG'], ['BRE','BEL'], False, 'None'],
        'RUH': ['Ruhr', 'RUH', 'Land', ['MUN','BUR','KIE','HOL','BEL'], [], [], False, 'None'],
        'KIE': ['Kiel', 'KIE', 'Coast', ['MUN','RUH'], ['HEL','BAL'], ['DEN','HOL','BER'], True, 'OF'],  #Germany (O) supply center, starts with Fleet
        'BER': ['Berlin', 'BER', 'Coast', ['MUN','SIL'], ['BAL'], ['KIE','PRU'], True, 'OA'],    #Germany (O) supply center, starts with Army
        'PRU': ['Prussia', 'PRU', 'Coast', ['SIL','WAR'], ['BAL'], ['LVN','BER'], False, 'None'],
        'LVN': ['Livonia', 'LVN', 'Coast', ['WAR','MOS'], ['BAL','BOT'], ['PRU','_S_STP'], False, 'None'],
        'GAS': ['Gascony', 'GAS', 'Coast', ['PAR','BUR','MAR'], ['MID'], ['_N_SPA','BRE'], False, 'None'],
        'BUR': ['Burgundy', 'BUR', 'Land', ['PAR','RUH','MUN','PIC','BEL','MAR','GAS'], [], [], False, 'None'],
        'MUN': ['Munich', 'MUN', 'Land', ['RUH','BUR','SIL','BOH','TYR','KIE','BER'], [], [], True, 'OA'],   #Germany (O) supply center, starts with Army
        'SIL': ['Silesia', 'SIL', 'Land', ['MUN','BOH','GAL','WAR','BER','PRU'], [], [], False, 'None'],
        'WAR': ['Warsaw', 'WAR', 'Land', ['SIL','GAL','UKR','MOS','PRU','LVN'], [], [], True, 'WA'],     #Russia (W) supply center, starts with Army
        'MOS': ['Moscow', 'MOS', 'Land', ['WAR','UKR','LVN','SEV','STP'], [], [], True, 'WA'],        #Russia (W) supply center, starts with Army
        'POR': ['Portugal', 'POR', 'Coast', ['SPA'], ['MID'], [], True, 'None'],        #neutral supply center
        'SPA': ['Spain', 'SPA', '_NS_Coast', [], ['MID','_S_WES','_S_LYO'], ['_S_MAR','_N_GAS'], True, 'None'],   #neutral supply center
        'MAR': ['Marseilles', 'MAR', 'Coast', ['GAS','BUR'], ['LYO'], ['_S_SPA','PIE'], True, 'BA'], #France (B) supply center, starts with Army
        'PIE': ['Piedmont', 'PIE', 'Coast', ['TYR','VEN'], ['LYO'], ['TUS','MAR'], False, 'None'],
        'TYR': ['Tyrolia', 'TYR', 'Land', ['MUN','BOH','VIE','TRI','VEN','PIE'], [], [], False, 'None'],
        'BOH': ['Bohemia', 'BOH', 'Land', ['MUN','SIL','GAL','VIE','TYR'], [], [], False, 'None'],
        'GAL': ['Galicia', 'GAL', 'Land', ['SIL','WAR','UKR','RUM','BUD','VIE','BOH'], [], [], False, 'None'],
        'UKR': ['Ukraine', 'UKR', 'Land', ['WAR','MOS','SEV','RUM','GAL'], [], [], False, 'None'],
        'SEV': ['Sevastapol', 'SEV', 'Coast', ['UKR','MOS'], ['BLA'], ['RUM','ARM'], True, 'WF'],       #Russia (W) supply center, starts with Fleet
        'VIE': ['Vienna', 'VIE', 'Land', ['TYR','BOH','GAL','BUD','TRI'], [], [], True, 'RA'],    #Austria (R) supply center, Starts with Army
        'WES': ['Western_Mediterranean_Sea', 'WES', 'Sea', [], ['MID','TYS','LYO'], ['_S_SPA','NAF','TUN'], False, 'None'],
        'LYO': ['Gulf_of_Lyon', 'LYO', 'Sea', [], ['WES','TYS'], ['_S_SPA','MAR','PIE','TUS'], False, 'None'],
        'TUS': ['Tuscany', 'TUS', 'Coast', ['VEN'], ['LYO','TYS'], ['ROM','PIE'], False, 'None'],
        'VEN': ['Venice', 'VEN', 'Coast', ['TYR','PIE','TUS','ROM'], ['ADR'], ['TRI','APU'], True, 'GA'],         #Italy (G) supply center, starts with Army
        'TRI': ['Trieste', 'TRI', 'Coast', ['SER','TYR','VIE'], ['ADR'], ['ALB','VEN'], True, 'RF'],  #Austria (R) supply center, starts with Fleet
        'BUD': ['Budapest', 'BUD', 'Land', ['TRI','VIE','GAL','RUM','SER'], [], [], True, 'RA'],  #Austria (R) supply center, starts with Army
        'RUM': ['Rumania', 'RUM', 'Coast', ['SER','BUD','GAL','UKR'], ['BLA'], ['SEV','_N_BUL'], True, 'None'],  #neutral supply center
        'BLA': ['Black_Sea', 'BLA', 'Sea', [], [], ['_N_BUL','RUM','SEV','ARM','ANK','CON'], False, 'None'],
        'ARM': ['Armenia', 'ARM', 'Coast', ['SMY','SYR'], ['BLA'], ['ANK','SEV'], False, 'None'],
        'ADR': ['Adriatic_Sea', 'ADR', 'Sea', [], ['ION'], ['VEN','APU','TRI','ALB'], False, 'None'],
        'ALB': ['Albania', 'ALB', 'Coast', ['SER'], ['ADR','ION'], ['TRI','GRE'], False, 'None'],
        'SER': ['Serbia', 'SER', 'Land', ['TRI','BUD','RUM','BUL','GRE','ALB'], [], [], True, 'None'],      #neutral supply center
        'GRE': ['Greece', 'GRE', 'Coast', ['SER'], ['ION','AEG'], ['ALB','_S_BUL'], True, 'None'],  #neutral supply center
        'BUL': ['Bulgaria', 'BUL', '_NS_Coast', ['SER'], ['_N_BLA','_S_AEG'], ['_S_GRE','_N_RUM','CON'], True, 'None'],  #neutral supply center
        'CON': ['Constantinople', 'CON', 'Coast', [], ['BLA','AEG'], ['_N_BUL','_S_BUL','ANK','SMY'], True, 'YA'],  #Turkey (Y) supply center, starts with Army
        'ANK': ['Ankara', 'ANK', 'Coast', ['SMY'], ['BLA'], ['ARM','CON'], True, 'YF'],  #Turkey (Y) supply center, starts with Fleet
        'NAF': ['North_Africa', 'NAF', 'Coast', [], ['MID','WES'], ['TUN'], False, 'None'],
        'TUN': ['Tunis', 'TUN', 'Coast', [], ['WES','TYS','ION'], ['NAF'], True, 'None'],   #neutral supply center
        'TYS': ['Tyrrhenian_Sea', 'TYS', 'Sea', [], ['WES','LYO','ION'], ['TUN','TUS','ROM','NAP'], False, 'None'],
        'ROM': ['Rome', 'ROM', 'Coast', ['APU','VEN'], ['TYS'], ['NAP','TUS'], True, 'GA'],  #Italy (G) supply center, starts with Army
        'APU': ['Apulia', 'APU', 'Coast', ['ROM'], ['ION','ADR'], ['NAP','VEN'], False, 'None'],
        'NAP': ['Naples', 'NAP', 'Coast', [], ['TYS','ION'], ['ROM','APU'], True, 'GF'],     #Italy (G) supply center, starts with Fleet
        'ION': ['Ionian_Sea', 'ION', 'Sea', [], ['TYS','AEG','EAS'], ['NAP','APU','ALB','GRE','TUN'], False, 'None'],
        'AEG': ['Aegean_Sea', 'AEG', 'Sea', [], ['ION','EAS'], ['GRE','_S_BUL','SMY','CON'], False, 'None'],
        'SMY': ['Smyrna', 'SMY', 'Coast', ['ARM','ANK'], ['AEG','EAS'], ['SYR','CON'], True, 'YA'],  #Turkey (Y) supply center, starts with Army
        'EAS': ['Eastern_Mediterranean_Sea', 'EAS', 'Sea', [], ['ION','AEG'], ['SMY','SYR'], False, 'None'],
        'SYR': ['Syria', 'SYR', 'Coast', ['ARM'], ['EAS'], ['SMY'], False, 'None']

        #'XXXX': ['XXXXX', 'X', 'XX', [], [], [], False, 'None'],    #Template for making spaces
    }

    #print(board.keys())

    return(board)


def makeTestBoard(): #This board is not the original board of Diplomacy, but should is used for testing
    test_board1 = { #Test board 1 is purposed for testing support system
        'AAA': ['A_Land', 'AAA', 'Land', ['BBB', 'CCC', 'DDD'], [], [], True, 'WArmy'],
        'BBB': ['B_Land', 'BBB', 'Land', ['AAA', 'EEE'], [], [], False, 'WArmy'],
        'CCC': ['C_Land', 'CCC', 'Land', ['AAA', 'DDD'], [], [], False, 'None'],
        'DDD': ['D_Land', 'DDD', 'Land', ['AAA','EEE', 'CCC'], [], [], True, 'BArmy'],
        'EEE': ['E_Land', 'EEE', 'Land', ['BBB', 'DDD'], [], [], True, 'BArmy']
    }

    return(test_board1)



#This is a testing fuction only
def main():
    pass
    #print(makeBoard())

if __name__ == '__main__':
    main()