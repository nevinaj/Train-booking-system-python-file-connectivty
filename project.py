import matplotlib.pyplot as plt
import numpy as np
import random
se=random.randint(1,10)
stat=[]
name=[]
train=[]
no=0
bo=0
st=''
nst=''
fp=open("file.txt","a+")
fp.seek(0,0)
k=fp.readlines()
for i in k:
    el=i.rstrip('\n')
    name.append(el)
print("\t\t\t\t\t\tINDIAN RAILWAYS")
print("\t\t\t\toooo--------------------------------------oooo")
print("\t\t\t\toooo--------------------------------------oooo")
print("\t\t\t\toooo--------------------------------------oooo")
print("\t\t\t\t\tSafety Security and Punctuality")
print("\n")
print("BOOK YOUR TICKETS!!!!!!")
print("_______________________")
print("\n")
con='yes'
while con=='yes':
    print("1.Login With Username AND Password")
    print("2.Don't Have An Account!!!Create New Account")
    opt=int(input("Enter Option :"))
    if opt==1:
        user=input("Enter Username :")
        pas=input("Enter Password :")
        st=user+" "+pas
        if st in name:
            print("LOGIN ACCEPTED")
            break
        else:
            print("Sorry Username or Password Does Not Exist")
            con=input("DO YOU WANT TO RETRY(yes/no) :")
    if opt==2:
        nuser=input("Enter new Username :")
        npas=input("Enter new Password :")
        nst=nuser+" "+npas
        print(nst)
        if nst in name:
            print("Username Already Exists")
            con=input("DO YOU WANT TO RETRY(yes/no)")
        else:
            fp.write('\n')
            fp.write(nst)
            fp.close()
            print("Account Created")
            break
print("\t\t\tYou Have Succesfully Logged In")
hp=open("train.txt","r")
li=hp.readlines()
for i in li:
    ew=i.rstrip('\n')
    train.append(ew)
leng=len(train)
print("TRAINS STATIONS ARE :")
for i in range(leng-1):
    l=train[i].split()
    if l[0] not in stat:
        stat.append(l[0])
    else:
        pass
for h in stat:
    print(h)
c='yes'
while c=='yes':
    fro=input("ENTER STARTING TRAIN STATION :")
    to=input('ENTER DESTINATION :')
    for j in range(leng):
        l=train[j].split()
        if fro in l:
            print("Timings available For Your Train Are:")
            print(train[j])
            print('\n')
            no+=1
            c='no'
        else:
            pass
    if no<1:
        print("NO TRAINS AVAILABLE FROM THIS LOCATION")
        c=input("DO YOU WANT TO RETRY(yes/no)")
else:
    pass
co='yes'
while co=='yes':
    tname=input("ENTER TRAIN YOU WANT TO BOOK :")
    time=input("ENTER TIME YOU WANT TO BOOK :")
    seat=int(input("ENTER YOUR SEAT NUMBER(1,10):"))
    for i in train:
        l=i.split()
        if tname in l:
            if time in l:
                bo+=1
                if seat!=se:
                    print("YOUR TRAIN HAS BEEN BOOKED")
                    co='no'
                else:
                    print("This Seat Is Already Reserved")
                    print('\n')
                    co=input("DO YOU WANT TO RETRY(yes/no) :")
        else:
            pass
if bo<1:
    print("Sorry Your Train Name And Time is Not Matching")
else:
    pass

print("\t\t\t\t\t\t\tTrend of what people eat during travel.")
print('\n')
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
hp=open("foodgraph.txt","r")
li=hp.readlines()
le=len(li)
u="yes"
while u=="yes":
    print("1.Breakfast Itams")
    print("2.Lunch Items")
    print("3.DINNER Items")
    n=int(input("Enter option :"))
    if n==1:
        for i in range(le):
            if i==1:
                l=li[i].split()
                for h in l:
                    a.append(float(h))
            if i==0:
                 l=li[i].split()
                 for h in l:
                    b.append(h)
        plt.bar(b,a,width=0.3,label='NO: OF PEOPLE BUYING EACH FOOD',color='r')
        plt.xlabel("FOOD ITMES")
        plt.ylabel("NO: OF PEOPLE PER 100")
        plt.legend()
        plt.show()
        u=input("DO YOU WANT TO CONTINUR(yes/no)")
    if n==2:
        for i in range(le):
            if i==3:
                l=li[i].split()
                for h in l:
                    c.append(float(h))
            if i==2:
                 l=li[i].split()
                 for h in l:
                     d.append(h)
        plt.bar(d,c,width=0.2,label='NO: OF PEOPLE BUYING EACH FOOD',color='royalblue')
        plt.xlabel("FOOD ITMES")
        plt.ylabel("NO: OF PEOPLE PER 100")
        plt.legend()
        plt.show()
        u=input("DO YOU WANT TO CONTINUR(yes/no)")
    if n==3:
        for i in range(le):
            if i==5:
                l=li[i].split()
                for h in l:
                    e.append(float(h))
            if i==4:
                 l=li[i].split()
                 for h in l:
                     f.append(h)
        plt.bar(f,e,width=0.3,label='NO: OF PEOPLE BUYING EACH FOOD',color='g')
        plt.xlabel("FOOD ITMES")
        plt.ylabel("NO: OF PEOPLE PER 100")
        plt.legend()
        plt.show()
        u=input("DO YOU WANT TO CONTINUR(yes/no)")
        






    



            
            
        
    

        

