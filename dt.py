def getDate():
    from datetime import datetime
    now= datetime.now()
    date=now.strftime("%d/%m/%y")
    return str(date)
    
def getTime():
    from datetime import datetime
    now= datetime.now()
    time=now.strftime("%H/%M/%S")
    return str(time)
#print(getTime)
#print(getDate())
