import MySQLdb
import matplotlib.pyplot as plt
print("ok")

db = MySQLdb.connect("cscdata.centre.edu", "gabe", "G@be123!", "soccer")
cursor = db.cursor()
sql = "SELECT * FROM players"
l_team,i_count, l_yellow, years, goals, assist = [], 0, [], [], [], []
color = ["pink"]
othercolor = ["black"]
try:
    print("try to run query")
    cursor.execute(sql)
    print("query ran ok")
    db.commit()
    results = cursor.fetchall()
    
##    for i in range(len(results)):
##        l_team.append(results[i][-2])
##    plt.hist(l_team)
##    plt.show()

##    for i in range(len(results)):
##        l_yellow.append(results[i][-4])
##    plt.hist(l_yellow)
##    plt.xlabel("Yellow Cards")
##    plt.ylabel("Frequency")
##    plt.title("Number of Yellow Cards")
##    plt.show()
##
    for i in range(len(results)):
        goals.append(results[i][3])
        years.append(results[i][2].year)
        assist.append(results[i][4])
    plt.scatter(years,goals, c = color)
    plt.scatter(years, assist, c = othercolor)

    #plt.plot(x, "o:r")
    #plt.plot(goals, mfc = "hotpink")
    plt.show()

    for 
except:
    print("error running query")

db.close()
