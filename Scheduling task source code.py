import datetime
import json

# For getting the next day of the date provided as string
def nextDay(string):
    y,m,d=string.split("-")
    currDay=datetime.date(int(y),int(m),int(d))
    return str(currDay+datetime.timedelta(days=1))

# For getting the previous day of the date provided as string
def prevDay(string):
    y,m,d=string.split("-")
    currDay=datetime.date(int(y),int(m),int(d))
    return str(currDay-datetime.timedelta(days=1))

#For updating the dictinary values
def update(data,uName,p2,s2,e2):
    dlist=data[uName]
    for i in dlist:
        p1=i["profile"]
        s1=i["startDate"]
        e1=i["endDate"]
        if(p1==p2):
            if((s2==e1 and s2>s1) and (e2>e1 and e2>s1) ):
                s2=s1
                dlist.remove(i)
            elif((s2<s1 and s2<e1) and (e2==s1 and e2<e1 )):
                e2=e1
                dlist.remove(i)                
            elif((s2>s1 and s2<e1) and (e2>e1 and e2>s1) ):
              
                s2=s1                
                dlist.remove(i)
            elif((s2<s1 and s2<e1) and (e2>s1 and e2<e1)):
                e2=e1
                dlist.remove(i)
            elif(s2>s1 and e2==e1):
                s2=s1                                
                dlist.remove(i)
            elif((s2==s1 and s2<e1) and (e2>s1 and e2<e1)):
                e2=e1
                dlist.remove(i)
            elif ( (s2<s1 and s2<e1) and (e2==e1 and e2>s1) ):
                dlist.remove(i)                
            elif( (s2==s1 and s2<e1) and (e2>e1 and e2>s1) ):
                dlist.remove(i)
            elif(s2<e1 and e2<e1 and s2>s1 and e2>s1):            
                s2=s1
                e2=e1
                dlist.remove(i)                                
            elif((s2<s1 and s2<e1) and (e2>s1 and e2>e1)):
                dlist.remove(i)
            elif( (s2==s1 and s2<e1) and (e2==e1 and e2>s1) ):
                dlist.remove(i)
            elif( (s2>e1 and s2>s1) and (e2>e1 and e2>s1) ):
                pass
            elif( (s2<e1 and s2<s1) and (e2<e1 and e2<s1) ):
                pass
        elif(not(p1==p2)):       
            if((s2==e1 and s2>s1) and (e2>e1 and e2>s1)):
                i['endDate']=prevDay(s2)                
            elif((s2<s1 and s2<e1) and (e2==s1 and e2<e1 )):                
                i["startDate"]=nextDay(e2)
            elif((s2>s1 and s2<e1) and (e2>e1 and e2>s1)):
                i["endDate"]=prevDay(s2)
            elif((s2<s1 and s2<e1) and (e2>s1 and e2<e1)):
                i["startDate"]=nextDay(e2)
            elif(s2>s1 and e2==e1):
                i["endDate"]=prevDay(s2)
            elif((s2==s1 and s2<e1) and (e2>s1 and e2<e1)):
                i["startDate"]=nextDay(e2)
            elif ( (s2<s1 and s2<e1) and (e2==e1 and e2>s1) ):
                dlist.remove(i)
            elif( (s2==s1 and s2<e1) and (e2>e1 and e2>s1) ):
                dlist.remove(i)
            elif(s2<e1 and e2<e1 and s2>s1 and e2>s1):               
                temp=nextDay(e2)
                i["endDate"]=prevDay(s2)
                dlist.append({"profile":p1,"startDate":temp,"endDate":e1})
            elif((s2<s1 and s2<e1) and (e2>s1 and e2>e1)):
                dlist.remove(i)
            elif( (s2==s1 and s2<e1) and (e2==e1 and e2>s1) ):
                dlist.remove(i)
    data[uName].append({"profile":p2,"startDate":s2,"endDate":e2})

# For inserting a profile in existing user
def insert():
    
    #getting data from json file
    f_read=open("users.json","r")  
    users=json.load(f_read)  
    
    #getting profile data from users
    while(1):
        u=input("Enter username\n")
        p=input("Enter profile name\n")
        day,month,year=map(int,input("Enter Start Date (DD-MM-YYYY) \n").split("-"))
        sDate=str(datetime.date(year,month,day))
        day,month,year=map(int,input("Enter End Date (DD-MM-YYYY) \n").split("-"))
        eDate=str(datetime.date(year,month,day))
        if(eDate<sDate):
            print("invalid start and end dates")
        else:
            break
    
    #check for updating data in existing user or entering new user
    if(u in users.keys()):
        update(users,u,p,sDate,eDate)
    else:
        users[u]=[{"profile":p,"startDate":sDate,"endDate":eDate}]
        #file pointer to write data
        f_write=open("users.json","w")
        json.dump(users,f_write)
        f_write.close()    
        return 0    
    
    #writing data to file
    f_write=open("users.json","w")    
    json.dump(users,f_write)
    f_write.close()
    f_read.close()
    return 1

def check():
    f_read=open("users.json","r")
    print(json.load(f_read))
    f_read.close()

if __name__ == "__main__":        
    while(1):
        print("Number of operations possible : ")
        print("1 Insert profile for a user")
        print("2 Check profile")
        print("3 To exit")
        print("Enter number \n")
        op=int(input())

        if (op==1):
            if(insert()):
                print("Data inserted")
            else:
                print("Data appended")
        elif(op==2):
            check()
        elif(op==3):
            break
        else:
            print("Enter a valid number \n")