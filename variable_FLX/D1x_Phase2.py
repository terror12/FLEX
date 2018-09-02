import sys

def set_position_nums2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, MIN, QB_std, RB_std, RB2_std, WR_std, WR2_std, WR3_std, TE_std, FLX_std, DST_std):
    global countQB
    countQB = len(QB)
    global countWR3
    countWR3 = len(WR3)
    global countDST
    countDST = len(DST)
    global countWR2
    countWR2 = len(WR2)
    global countRB
    countRB = len(RB)
    global countWR
    countWR = len(WR)
    global countTE
    countTE = len(TE)
    global countFLX
    countFLX = len(FLX)
    global countRB2
    countRB2 = len(RB2)
    global minSal
    minSal = MIN
    global QB_math
    QB_math = QB_std
    global WR_math
    WR_math = WR_std
    global RB_math
    RB_math = RB_std
    global RB2_math
    RB2_math = RB2_std
    global WR2_math
    WR2_math = WR2_std
    global WR3_math
    WR3_math = WR3_std
    global TE_math
    TE_math = TE_std
    global FLX_math
    FLX_math = FLX_std
    global DST_math
    DST_math = DST_std

# File to run removal of 1 player for 2 positions at a time (Phases 1-9)
#global count
def D1xWR3PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countWR3
    print(Dnum)
    print(len(WR3))
    print(countWR3)
    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']
    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        # Figure out how to remove by name instead of by WR3closest
        # Phase? (1,2,3,4,5,6,7,8,9)
        # Set? (D1x, D2x, D3x, D4x, ...., D32x)
# Reorder STD likenups by closest to the AVG STD!!!
#        print(WR)
        WR3 = WR3[WR3.STD != WR3closest]
        WR = WR[WR.STD != WRclosest]
#        print(WR3.head(50))
        print('WR3PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']
        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

        totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        global count
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(WR3) > (countWR3 - Dnum):
            print(countWR3)
            print(len(WR3))
            D1xWR3PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
        elif set1 == 'yes': #and (len(WR3) == (countWR3 - Dnum)): #count < 1:
            D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)
            print(first)
        else:
            print('printing else statement')
            #D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'yes')
# could do variation of position, least variiation on top most on bottom
def D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
 #   WR = display_closest(spreadsheetId, rangeName)

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
    #    print(WR3.head(50))
        TE = TE[TE.STD != TEclosest]
    #    print(WR3.head(50))
        print('TEPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
     #   print(first)


        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        #print(first)

        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
#        set1 = input('run set1??')
#        set2 = input('run set2??')
#        yes = 'yes'
#        global count
        elif len(TE) > (countTE - Dnum):
            print(countTE)
            print(len(TE))
            D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        elif set1 == 'yes' and countWR3 == len(WR3): # and (len(TE) != (countTE - Dnum)):
            D1xWR2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)
#        elif set1 == 'no':
#            D1xWR2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)

#            print(first)
#        if set2 == 'yes':
#            D1xWR2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no')


def D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

      #  print(first)
        print('_________________________________________________')
        WR2 = WR2[WR2.STD != WR2closest]
        WR = WR[WR.STD != WR2closest]

        print('WR2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
 #       if set1 == 'yes' and count < 1:
#            count += 1
#            print(count)
#        D1xFLXPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'yes')
#            print(first)
        elif len(WR2) > (countWR2 - Dnum):
            D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        elif set1 == 'yes' and countTE == len(TE):
            D1xFLXPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)
        #D1xFLXPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def D1xFLXPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

     #   print(first)
        print('_________________________________________________')
        FLX = FLX[FLX.STD != FLXclosest]
        print('FLXPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(FLX) > (countFLX - Dnum):
            D1xFLXPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        if set1 == 'yes' and countWR2 == len(WR2): #and count <= 2:
            D1xRB2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)
#        if set2 == 'yes':
#            D1xRB2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'yes')
        #D1xRB2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def D1xRB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        RB2 = RB2[RB2.STD != RB2closest]
        RB = RB[RB.STD != RB2closest]
        print('RB2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(RB2) > (countRB2 - Dnum):
            D1xRB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        if set1 == 'yes' and countFLX == len(FLX):
            D1xDSTPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)

def D1xDSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        DST = DST[DST.STD != DSTclosest]
        print('DSTPLEX PRINT OUT AFTER')
        print('WR')
        print(len(WR))
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB')
        print(len(RB))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(DST) > (countDST - Dnum):
            D1xDSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        if set1 == 'yes' and countRB2 == len(RB2):
            D1xRBPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)

def D1xRBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        #WR2 = WR2[WR2.STD != WR2closest]
        RB = RB[RB.STD != RBclosest]
        print('RBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(RB) > (countRB - Dnum):
            D1xRBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        if set1 == 'yes' and countDST == len(DST):
            D1xWRPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)

def D1xWRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        #WR2 = WR2[WR2.STD != WR2closest]
        WR = WR[WR.STD != WRclosest]
        print('WRPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(WR) > (countWR - Dnum):
            D1xWRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

        if set1 == 'yes' and countRB == len(RB):
            D1xQBPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)

def D1xQBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = QB_math
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = RB_math
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = RB2_math
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = WR_math
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = WR2_math
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = WR3_math
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = TE_math
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = FLX_math
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = DST_math
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    FLXpos = FLX.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(FLXpos[FLXposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        QB = QB[QB.STD != QBclosest]
        print('QBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('FLX')
        print(len(FLX))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = QB_math
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = RB_math
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = RB2_math
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = WR_math
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = WR2_math
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = WR3_math
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = TE_math
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = FLX_math
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = DST_math
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        FLXpos = FLX.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(FLXpos[FLXposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > minSal and first[-1] < 65000): # and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
            sys.exit()
        elif len(QB) > (countQB - Dnum):
            D1xQBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)


        #D1xWR3PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def Set1(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 1 -------')
    D1xWR3PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
#    D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'yes')

def Set2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 2 -------')
    D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
#    count = 0

def Set3(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 3 -------')
    D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def Set4(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 4 -------')
    D1xFLXPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def Set5(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 5 -------')
    D1xRB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def Set6(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 6 -------')
    D1xDSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
def Set7(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 7 -------')
    D1xRBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
def Set8(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 8 -------')
    D1xWRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

#    D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no')
#    D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xFLXPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xRB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xDSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xRBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xWRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#    D1xQBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)