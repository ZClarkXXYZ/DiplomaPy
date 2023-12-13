


def getImageFileCode(fileInput):
    '''


    Returns image file corresponding to what the input is.
    Single letter inputs refer to supply center image. The rest refer to unit of given type and color
    '''

    imageFileCode = {
        'W': ['white'],
        'Y': ['yellow'],
        'B': ['blue'],
        'G': ['green'],
        'R': ['red'],
        'O': ['orange'],
        'P': ['purple'],
        'WA': ['white_A'],
        'YA': ['yellow_A'],
        'BA': ['blue_A'],
        'GA': ['green_A'],
        'RA': ['red_A'],
        'OA': ['orange_A'],
        'PA': ['purple_A'],
        'WF': ['white_F'],
        'YF': ['yellow_F'],
        'BF': ['blue_F'],
        'GF': ['green_F'],
        'RF': ['red_F'],
        'OF': ['orange_F'],
        'PF': ['purple_F'],
    }
    return(imageFileCode[fileInput][0] + '.png')



def getPictureLocation_SupplyCenter(location):


    '''

    Returns the cords of where to put piece images on the image of the board for supply centers

    '''

    supplyLocationCode = {
        'EDI': [(220,264)],
        'LVP': [(210,308)],
        'LON': [(226,356)],
        'BRE': [(202,394)],
        'PAR': [(226,428)],
        'MAR': [(273,496)],
        'KIE': [(336,318)],
        'BER':[(372,357)],
        'MUN': [(346,394)],
        'NWY': [(345,212)],
        'SWE': [(401,184)],
        'DEN': [(360,310)],
        'POR': [(61,544)],
        'SPA':[(124,566)],
        'TUN': [(310,655)],
        'HOL': [(290, 357)],
        'BEL': [(285,382)],
        'STP': [(538,222)],
        'MOS': [(631, 262)],
        'WAR': [(457,361)],
        'SEV': [(688,427)],
        'VEN':[(352, 494)],
        'ROM': [(376, 554)],
        'NAP': [(395,576)],
        'VIE': [(428,468)],
        'BUD': [(493,465)],
        'TRI': [(441,515)],
        'CON': [(605,559)],
        'ANK': [(637,560)],
        'SMY': [(613,612)]
    }

    return supplyLocationCode[location][0]


def getPictureLocation_PieceLocation(location):
    '''Todo


    Returns the cords of where to put claimed supply center on the image of the board.
    '''
    pieceLocationCode = {
        'NAO' : [(90, 200)],
        'NWG': [(250, 160)],
        'BAR': [(590, 20)],
        'CLY': [(194, 245)],
        'EDI': [(229, 252)],
        'NTH': [(263, 273)],
        'NWY': [(370, 144)],
        'STP': [(577,157)],
        'MID': [(30,430)],
        'IRI': [(150,320)],
        'LVP': [(206,286)],
        'YOR': [(222,322)],
        'SKA': [(356,261)],
        'SWE': [(400,150)],
        'FIN': [(478,172)],
        'WHA': [(183,346)],
        'LON': [(243,335)],
        'ENG': [(184,370)],
        'BEL': [(274,381)],
        'HOL': [(300,339)],
        'HEL': [(302,311)],
        'DEN': [(339,278)],
        'BAL': [(424,297)],
        'BOT': [460, 236],
        'BRE': [(181,420)],
        'PAR': [(238,411)],
        'PIC': [(257,395)],
        'RUH': [(303,406)],
        'KIE': [(331,363)],
        'BER': [(376,323)],
        'PRU': [(428,333)],
        'LVN': [(495,291)],
        'GAS': [(202,476)],
        'BUR': [(256,451)],
        'MUN': [(358,399)],
        'SIL': [(421,379)],
        'WAR': [(504,349)],
        'MOS': [(666,230)],
        'POR': [(75,500)],
        'SPA': [(173,526)],
        'MAR': [(265,478)],
        'PIE': [(333,471)],
        'TYR': [(387,439)],
        'BOH': [(393,410)],
        'GAL': [(489,413)],
        'UKR': [(572,390)],
        'SEV': [(697,380)],
        'VIE': [(434,423)],
        'WES': [(235,595)],
        'LYO': [(263,555)],
        'TUS': [(3343,525)],
        'VEN': [(360,507)],
        'TRI': [(394,483)],
        'BUD': [(461,466)],
        'RUM': [(539,489)],
        'BLA': [(634,491)],
        'ARM': [(745,555)],
        'ADR': [(406,531)],
        'ALB': [(464,568)],
        'SER': [(467,498)],
        'GRE': [(491,577)],
        'BUL': [(521,535)],
        'CON': [(572,575)],
        'ANK': [(678,532)],
        'NAF': [(146,651)],
        'TUN': [(295,655)],
        'TYS': [(335,591)],
        'ROM': [(358,554)],
        'APU': [(411,565)],
        'NAP': [(397,607)],
        'ION': [(443,637)],
        'AEG': [(566,628)],
        'SMY': [(667,589)],
        'EAS': [(677,639)],
        'SYR': [(744,637)]

    }

    return pieceLocationCode[location][0]