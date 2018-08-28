def set_position_nums(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST):
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

#from Implemenation_build_on_closest_to_perf import set_position_nums


def WR3PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countWR3
    print(Dnum)
    print(countWR3)
    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']
    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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
        WR = WR[WR.STD != WR3closest]
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']
        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        #print(first)
        #print(len(WR))
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR3) >= (countWR3 - Dnum):
            print(countWR3)
            print(len(WR3))
            WR3PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no', Dnum)
#        if set1 == 'yes' and len(WR3) < (countWR3 - 2): #count < 1:
#  #          print('ADAMSCERRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#            D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'no')
#            print(first)




#    print(QB)
#    return QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST
#        TEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
# could do variation of position, least variiation on top most on bottom

def TEPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countTE

    #   WR = display_closest(spreadsheetId, rangeName)

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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

        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(TE) >= (countTE - Dnum):
            TEPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
        #        WR2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def WR2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countWR2


    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR2) >= (countWR2 - Dnum ):
            WR2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
 #       FLXPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def FLXPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countFLX


    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(FLX) >= (countFLX - Dnum ):
            FLXPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
     #       RB2PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)


def RB2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countRB2

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(RB2) >= (countRB2 - Dnum ):
            RB2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
#        DSTPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def DSTPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countDST

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #FLX = FLX[FLX.STD != FLXclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
        print('_________________________________________________')
        #WR2 = WR2[WR2.STD != WR2closest]
        print('QB')
        print(len(QB))
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(DST) >= (countDST - Dnum ):
            DSTPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
 #       RBPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def RBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countRB

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #FLX = FLX[FLX.STD != FLXclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(RB) >= (countRB - Dnum ):
            RBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
 #       WRPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def WRPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countWR

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR) >= (countWR - Dnum ):
            WRPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
#        QBPLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)

def QBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    global countQB

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    FLXSTD = FLX['STD']
    FLXSTD = FLXSTD.values.tolist()

    FLX_avg_std = 5.071295935117646
    FLXclosest = min(FLXSTD, key=lambda x:abs(x-FLX_avg_std))
    FLXposition = (FLXSTD.index(FLXclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
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

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        print('QBPLEX PRINT OUT BEFORE')
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
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        FLXSTD = FLX['STD']
        FLXSTD = FLXSTD.values.tolist()

        FLX_avg_std = 5.071295935117646
        FLXclosest = min(FLXSTD, key=lambda x: abs(x - FLX_avg_std))
        FLXposition = (FLXSTD.index(FLXclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(QB) >= (countQB - Dnum ):
            QBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum)
               # WR3PLEX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)
#        else:
#            WR3PLEXX(spreadsheetId, rangeName,  QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST)


def D3xSet1(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 1 -------')
    WR3PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
#    D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'no', 'yes')

def D3xSet2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 2 -------')
    TEPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
#    count = 0

def D3xSet3(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 3 -------')
    WR2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def D3xSet4(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 4 -------')
    FLXPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def D3xSet5(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 5 -------')
    RB2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)

def D3xSet6(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 6 -------')
    DSTPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
def D3xSet7(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 7 -------')
    RBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
def D3xSet8(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 8 -------')
    WRPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)
def D3xSet9(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, set1, set2, Dnum):
    print('settt ------- 8 -------')
    QBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, FLX, DST, 'yes', 'no', Dnum)