"""while not tested_all_supports:
    supportCommandRemoval = []
    tested_all_supports = True
    for support_i in range(len(supportCommands)):
        support = supportCommands[support_i]

        if len(actionLocations[support[
                               2:5]]) == 2 and support not in supportCommandRemoval:  # meaning, only support and its power is at given location. This is the simplest interaction possible with Support. The "and" condition is to prevent something from breaking, hopefully
            # give support to listed action, if action exist. If it doesn't exist, there is nothing to give +1 power
            if support[
               8:11] in actionLocations.keys():  # If there is nothing holding in that location or moving to that location, then it fails by default
                if support[6:] in actionLocations[support[8:11]]:  # If the target command is in
                    index_of_supported_act = actionLocations[support[8:11]].index(
                        support[6:])  # [support6:] slices the command to give the target command the
                    actionLocations[support[8:11]][
                        index_of_supported_act + 1] = + 1  # increase power of the action by one
                elif support[6:] in ('S' + actionLocations[support[
                                                           9:11]]):  # This one deals with the complicated interaction of a unit supporting a unit that is also supporting.
                    index_of_supported_act = actionLocations[support[8:11]].index(support[6:])
                    actionLocations[support[8:11]][
                        index_of_supported_act + 1] = + 1  # increase power of the action by one
            supportCommandRemoval.append(support)  # Support is checked fully, remove it from list of support commands

        elif support not in supportCommandRemoval:  # Else this will be complicated. That means that another unit is either using Convoy or Move to the spot the supporting unit this currently at.
            pass"""


{'names': ['Russ', 'Turk', 'Fran', 'Italy', 'Hun', 'Ger', 'Eng'], 'armies': ['Russia', 'Turkey', 'France', 'Italy', 'Hungary', 'Germany', 'England'], 'supplyCenters': [['STP', 'WAR', 'MOS', 'SEV'], ['CON', 'ANK', 'SMY'], ['BRE', 'PAR', 'MAR'], ['VEN', 'ROM', 'NAP'], ['VIE', 'TRI', 'BUD'], ['KIE', 'BER', 'MUN'], ['EDI', 'LVP', 'LON']], 'pieceLocations': [['STP__S_WF', 'WAR_WA', 'MOS_WA', 'SEV_WF'], ['CON_YA', 'ANK_YF', 'SMY_YA'], ['BRE_BF', 'PAR_BA', 'MAR_BA'], ['VEN_GA', 'ROM_GA', 'NAP_GF'], ['VIE_RA', 'TRI_RF', 'BUD_RA'], ['KIE_OF', 'BER_OA', 'MUN_OA'], ['EDI_PF', 'LVP_PA', 'LON_PF']], 'piecesToMove': [['STP__S_WF', 'WAR_WA', 'MOS_WA', 'SEV_WF'], ['CON_YA', 'ANK_YF', 'SMY_YA'], ['BRE_BF', 'PAR_BA', 'MAR_BA'], ['VEN_GA', 'ROM_GA', 'NAP_GF'], ['VIE_RA', 'TRI_RF', 'BUD_RA'], ['KIE_OF', 'BER_OA', 'MUN_OA'], ['EDI_PF', 'LVP_PA', 'LON_PF']], 'Russia': [], 'Turkey': [], 'France': [], 'Italy': [], 'Hungary': [], 'Germany': [], 'England': [], 'Moves': [[], [], [], [], [], [], []]}
{'names': ['Russ', 'Turk', 'Fran', 'Italy', 'Hun', 'Ger', 'Eng'], 'armies': ['Russia', 'Turkey', 'France', 'Italy', 'Hungary', 'Germany', 'England'], 'supplyCenters': [['STP', 'WAR', 'MOS', 'SEV'], ['CON', 'ANK', 'SMY'], ['BRE', 'PAR', 'MAR'], ['VEN', 'ROM', 'NAP'], ['VIE', 'TRI', 'BUD'], ['KIE', 'BER', 'MUN'], ['EDI', 'LVP', 'LON']], 'pieceLocations': [['STP__S_WF', 'WAR_WA', 'MOS_WA', 'SEV_WF'], ['CON_YA', 'ANK_YF', 'SMY_YA'], ['BRE_BF', 'PAR_BA', 'MAR_BA'], ['VEN_GA', 'ROM_GA', 'NAP_GF'], ['VIE_RA', 'TRI_RF', 'BUD_RA'], ['KIE_OF', 'BER_OA', 'MUN_OA'], ['EDI_PF', 'LVP_PA', 'LON_PF']], 'piecesToMove': [['STP__S_WF', 'WAR_WA', 'MOS_WA', 'SEV_WF'], [], ['BRE_BF', 'PAR_BA', 'MAR_BA'], ['VEN_GA', 'ROM_GA', 'NAP_GF'], ['VIE_RA', 'TRI_RF', 'BUD_RA'], ['KIE_OF', 'BER_OA', 'MUN_OA'], ['EDI_PF', 'LVP_PA', 'LON_PF']], 'Russia': [], 'Turkey': [], 'France': [], 'Italy': [], 'Hungary': [], 'Germany': [], 'England': [], 'Moves': [[], ['H_CON', 'H_ANK'], [], [], [], [], []]}

