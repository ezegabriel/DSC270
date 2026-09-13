import MySQLdb


def getData(sql):
    
    print("DavesDB: starting connection")


    db = MySQLdb.connect("cscdata.centre.edu", "dave", "DSC270F@ll2023", "soccer")
    cursor = db.cursor()
    

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        #print("DavesDB: ", results)
        print("DavesDB: success!")
    except:
        print("DavesDB: there was an error")

    print("DavesDB: closing connection")
    db.close()

    #print("DavesDB: ", results)
    return results
