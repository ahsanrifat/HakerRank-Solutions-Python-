def minion_game(s):
    vow={'A','E','I','O','U'}
    stu=0
    kev=0
    n=len(s)
    for i in range(n):
        
        if s[i] in vow:
            kev+=n-i
        else:
            stu+=n-i
            
    if kev>stu:
        print("Kevin {}".format(kev))
    elif stu>kev:
        print("Stuart {}".format(stu))
    else:
        print("Draw")

minion_games('BANANA')