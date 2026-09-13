def first(l2d, l_yellow):
    '''
    Function to solve the first problem

    Parameters
    ----------
    l2d : TYPE: list
        DESCRIPTION. 2D list holding all the information in the league
    l_yellow : list
        DESCRIPTION. List holding all the players with 5 or more yellows

    Returns
    -------
    None.

    '''
    print()
    for i in range(len(l2d)):
        if int(l2d[i][-2]) >= 5:
            l_yellow.append(l2d[i][1])
    print(l_yellow)
    
def second(l2d, l_red):
    '''
    

    Parameters
    ----------
    l2d : list
        DESCRIPTION.
    l_red : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    print()
    for i in range(len(l2d)):
        if int(l2d[i][-1]) >= 1:
            l_red.append(l2d[i][1])
    print(l_red)
    
def third(l2d,d):
    print()
    for i in range(len(l2d)):
        d[l2d[i][1]] = int(l2d[i][-5])
    print(d)
    
def fourth(l2d, l):
    print()
    for i in range(len(l2d)):
        l.append(int(l2d[i][-3]) - int(l2d[i][-4]))
    print(l2d[l.index(max(l))][1]) # Player with the most missed penalties

def fifth(l2d, l):
    print()
    for i in range(len(l2d)):
        try:
            l.append(int(l2d[i][-4]) / int(l2d[i][-3]) * 100)
        except ZeroDivisionError:
            l.append(100)
    i_min, l_worst = min(l), []
    while i_min != 100:
        l_worst.append(l2d[l.index(i_min)][1])
        l[l.index(i_min)] = 100
        i_min = min(l)
    print(l_worst)

def sixth(l2d, d):
    print()
    for i in range(len(l2d)):
        if not l2d[i][4] in d:
            d[l2d[i][4]] = 0
        else:
            d[l2d[i][4]] = d[l2d[i][4]] + int(l2d[i][5])
    print(d)
    
def seventh(l2d, d):
    print()
    for i in range(len(l2d)):
        if l2d[i][4] == "Chelsea":
            d[l2d[i][1]] = l2d[i][6]
    print(d)
    
def eighth(l2d, l):
    print()
    for i in range(len(l2d)):
        if l2d[i][3] == "GK":
            l.append(l2d[i][1])
    print(l)

def main():
    f_wsl = open("DSC270_WSL_Data.csv", mode = "r")
    l_wsl = f_wsl.readlines()
    del l_wsl[0]
    l2d_wsl = []

    for item in l_wsl:
        item = item.strip("\n")
        l_temp = item.split("\t")
        l2d_wsl.append(l_temp)
        
    first(l2d_wsl, [])
    second(l2d_wsl, [])
    third(l2d_wsl, {})
    fourth(l2d_wsl, [])
    fifth(l2d_wsl, [])
    sixth(l2d_wsl, {})
    seventh(l2d_wsl, {})
    eighth(l2d_wsl, [])
    
    f_wsl.close()
    
if "__main__" == __name__:
    main()