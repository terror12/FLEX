# File to run removal of 1 player for 3 positions at a time (Phases 3)
#global count
def D1xWR3PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

        totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
       # print(first)
        global count
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes': #count < 1:
            D1xTEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', 'no', 'no')
#            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

            print(first)
        else:
            print('printing else statement')
            #D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
# could do variation of position, least variiation on top most on bottom
def D1xTEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2, set3, set4):
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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
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

        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
#        set1 = input('run set1??')
#        set2 = input('run set2??')
#        yes = 'yes'
        global count
        if set1 == 'yes':
            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'no')
        if set2 == 'yes':
            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', 'no', 'no')
        if set3 == 'yes':
            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no', 'no' ,'no')
        if set4 == 'yes':
            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'yes' ,'no')
#            D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

#            print(first)
#        if set2 == 'yes':
#            D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')


def D1xWR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2, set3, set4):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
 #       if set1 == 'yes' and count < 1:
#            count += 1
#            print(count)
#        D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#            print(first)
        if set1 == 'yes': # = Kill
            D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'yes')
        if set2 == 'yes': # = Go
            D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no','no','no')
        if set3 == 'yes':
            D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', 'no', 'no')
        if set4 == 'yes':
            D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'yes', 'no')

#            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

        #D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def D1xKPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2, set3, set4):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        K = K[K.STD != Kclosest]
        print('KPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
       # print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes': #and count <= 2:
            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'no')
        if set2 == 'yes':
            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no', 'no','no')
        if set3 == 'yes':
            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no','yes','no')
        if set4 == 'yes':
            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no','no','yes')
#            D1xDSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

#        if set2 == 'yes':
#            D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
        #D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def D1xRB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2, set3, set4):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes':
            D1xDSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'no')
        if set2 == 'yes':
            D1xDSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no','no', 'no')
        if set3 == 'yes':
            D1xDSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no','no','yes')
        if set4 == 'yes':
            D1xDSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes','no','no')
#            D1xRBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

def D1xDSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2,set3,set4):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes':
            D1xRBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no','yes')
        if set2 == 'yes':
            D1xRBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes','no')
        if set3 == 'yes':
            D1xRBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no','no')
        if set4 == 'yes':
            D1xRBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no','no') #, 'no','no')
#            D1xWRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')

def D1xRBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2, set3):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
 #       print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes':
            D1xWRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
        if set2 == 'yes':
            D1xWRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')
        if set3 == 'yes':
            D1xWRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#        if set3 == 'yes':
#            D1xWRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#            D1xQBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')
def D1xWRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
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
        WR = WR[WR.STD != WRclosest]
        print('WRPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        if set1 == 'yes':
            D1xQBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')
        if set2 == 'yes':
            D1xQBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no')
def D1xQBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):

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

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

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
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
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
        print('K')
        print(len(K))
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

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

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
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
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
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #: #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)

        #D1xWR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase5Set1(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
    print('settt ------- 1 -------')
    D1xWR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#    D1xTEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')

def Phase5Set2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
    print('settt ------- 2 -------')
    D1xTEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'yes')
#    count = 0
##########################################
## Step 3 and down need work!!!!
#########################################
def Phase5Set3(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
    print('settt ------- 3 -------')
    D1xWR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'yes')

def Phase5Set4(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
    print('settt ------- 4 -------')
    D1xKPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'no', 'no', 'yes')

def Phase5Set5(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST, set1, set2):
    print('settt ------- 5 -------')
    D1xRB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', 'no','no')
