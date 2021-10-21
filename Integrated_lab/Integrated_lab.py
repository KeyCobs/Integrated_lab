#This script is made for encrypting data using a private key.
import subprocess
import sys
from cryptography.fernet import Fernet





#every string data is encrypted with a LOCAL key. We encrypt everything so that our data is useless when it's breached.
def Encryption(data):
    fileName = 'privatekey.key'
    #loading key
    with open(fileName, 'rb') as mykey:
        key = mykey.read()
    #print(key)
    f = Fernet(key)
    data = str(data)
    #encrypting
    em = f.encrypt(data.encode())
    #print("original: ",data)
    #print("Encrypted: ",em)
    #insert em in database
    #when reading use Decryption
    return em
    


# every time we want to print our values we have to call this function it will decrypt the data useing the LOCAL key.
def Decryption(dataEncrypt):
    if isinstance(dataEncrypt, (bytes, bytearray)):
        
        #loading key
        fileName = 'privatekey.key'
        with open(fileName, 'rb') as mykey:
            key = mykey.read()
        f = Fernet(key)
        decmessage = f.decrypt(dataEncrypt).decode()
        #print("decrypted: ", decmessage)
        return decmessage


def PrintData(data):
    for i in data:
        for j in i:
            #print(i)
            if isinstance(j, (bytes, bytearray)):
                print(Decryption(j))
            else:
                print(j)
        print("")









import random #Dit notebook maakt dummy data voor 6 personen

#Alle random arrays maken 20 namen
firstname = ["Olivia","Luna","Klara","Louise","Janne","Laura","Kim","Elisabeth","Elien","Helena",
            "Jorik","Jens","Jozef","Pieter","Jan","Christof","Pière","Felix","Thomas","Wout"]
lastname = ["Verbeken","De Heack","Vermeulen","Andes","Raemdonck","De Roeck","Verstreaten","Janssens","Scheers","Van Looke",
           "Smitd","De Beukelare","Goosenes","Van Den Bosch","Vertongen","Crucke","Van Zandberge","De Laete","Conicks","De Clerck"]
#1 hobby per persoon
hobbies = ["Paardrijden","Hockey","Judo","Gamen","Toneel Spelen","Klj","Chiro","Scouts","Rolschaatse","Turnen",
           "Volleybal","Voetbal","Basketbal","Rugby","Ropeskipping","Kaarten","Badminton","Tennis","Knutselen","Tekenen"]
classes= ["Wiskunde","Nederlands","Engels","Programmeren","Aarderijkskunde","L.O.","Frans","Muziek","Biologie","Fysieka","Chemie"]
# 11 classes

#-----------------Persons-----------------
#Persons=[]
#idStart= 0
#for x in range(6):
#    temparr = []
#    Tid ="P" + str(idStart)
#    idStart= idStart + 1
#    Tfirstname = firstname[random.randrange(20)]
#    Tlastname= lastname[random.randrange(20)]
#    Tstatus = "Student"
#    status = random.randrange(2)
#    if status == 1:
#        Tstatus = "Teacher"

#    TEmail = Tfirstname+"."+Tlastname+"@gmail.com"
#    TphoneNumber = "N/A"

#    temparr.extend([Tid , Tfirstname,Tlastname,TEmail, TphoneNumber,Tstatus])
#    Persons.append(temparr)
#print(Persons)
##-----------------Persons Encrypt-----------------
Persons=[]
idStart= 0
for x in range(6):
    temparr = []
    Tid ="P" + str(idStart)
    idStart= idStart + 1
    Tfirstname = firstname[random.randrange(20)]
    Tlastname= lastname[random.randrange(20)]
    Tstatus = Encryption("Student")
    status = Encryption(random.randrange(2))
    if status == 1:
        Tstatus = Encryption("Teacher")

    TEmail = Tfirstname+"."+Tlastname+"@gmail.com"
    #encrypting all
    Tfirstname = Encryption(Tfirstname)
    Tlastname = Encryption(Tlastname)
    TEmail = Encryption(TEmail)
    TphoneNumber = Encryption("N/A")

    temparr.extend([Tid , Tfirstname,Tlastname,TEmail, TphoneNumber,Tstatus])
    Persons.append(temparr)
PrintData(Persons)


#-----------------Class-----------------

#Classes= []
#for y in range(0,len(classes)):
#    temparr = []
#    Cid = "C" + str(y)
#    temparr.extend([Cid, classes[y]])
#    Classes.append(temparr)
#print(Classes)
###-----------------Hobby-----------------
#Hobby= []
#for y in range(0,len(hobbies)):
#    temparr = []
#    Hid = "H" + str(y)
#    temparr.extend([Hid, hobbies[y]])
#    Hobby.append(temparr)
#print(Hobby)

##-----------------PersonClassLink-----------------
#PersonClass =[]
#for y in range(6):
#    temparr = []
#    getal1 = random.randrange(6)
#    getal2 = random.randrange(6)
#    temparr.extend(["P"+str(getal1), "C"+str(getal2)])
#    PersonClass.append(temparr)
#print(PersonClass)
    
##-----------------PersonPersonLink-----------------
#PersonPerson = []
#for y in range(6):
#    temparr=[]
#    getal1 = random.randrange(6)
#    getal2 = random.randrange(6)
#    temparr.extend(["P"+str(getal1), "P"+str(getal2)])
#    PersonPerson.append(temparr)
#print(PersonPerson)
    
##-----------------PersonHobbyLink-----------------
#PersonHobby = []
#for y in range(6):
#    temparr=[]
#    getal1 = random.randrange(6)
#    getal2 = random.randrange(6)
#    temparr.extend(["P"+str(getal1),"H"+ str(getal2)])
#    PersonHobby.append(temparr)
#print(PersonHobby)


#Decryption(Encryption("aa"))
