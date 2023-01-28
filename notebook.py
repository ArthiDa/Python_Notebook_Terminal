import os
import json
from datetime import datetime



def showParticularPage(searchNo,fileData):
    os.system('cls')
    searchNo = int(searchNo) - 1
    title = fileData[searchNo]["Title"]
    cDate = fileData[searchNo]["Creation-Date"]
    mDate = fileData[searchNo]["Modification-Date"]
    des = fileData[searchNo]['Description']

    print("Title:",title)
    print("Creation Date: ***",cDate,"***")
    print("Modification Date: ***",mDate,"***")
    print("-----------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------")
    # Per Line 10 Words 
    wordList = des.split()
    i = 0
    for word in wordList:
        print(word,end =" ")
        i += 1
        if i == 10:
            print("\n")
            i = 0
    print()
    print("-----------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------")
    

def showNotebook(check):
    os.system('cls')
    file = open("data.json")
    fileData = json.load(file)
    cn = 0
    for data in fileData:
        print("\t\t\t(",cn+1,")",data["Title"])
        cn += 1
    file.close()
    totalData = str(cn)
    if check == "delete" or check == "update":
        return cn
    choice = input("Do You Want To Read? If You Want Than Enter The Serial Number otherwise N: ")
    if choice >= "1" and choice <= totalData:
        showParticularPage(choice,fileData)

def addNewPage():
    os.system('cls')
    title = input("Enter Your New Notebook Page Title: ")
    des = input("Enter Tour New Notebook Page Description: ")
    now = datetime.now()
    d = now.strftime("%d/%m/%Y %H:%M:%S")
    newPage = {
        "Title": title,
        "Description": des,
        "Creation-Date" : d,
        "Modification-Date" : d
    }
    with open("data.json",'r+') as file: 
        # Load exiting data from file 
        fileData = json.load(file)
        # Appending new data in file 
        fileData.append(newPage)
        file.seek(0)
        # Convert data back to json 
        json.dump(fileData, file, indent = 4)
    print("Hurray!", title, "is successfully created.")

def deletePage():
    totalPage = showNotebook('delete')
    counter = str(totalPage)
    choice = input("Do You Want To Delete? If You Want Than Enter The Serial Number otherwise N: ")
    if choice>="1" and choice<=counter:
        choice = int(choice) - 1
        with open("data.json",'r+') as file: 
            # Load exiting data from file 
            fileData = json.load(file)
            # Delete user choice data 
            del fileData[choice]
            file.seek(0) 
            # to erase all data 
            file.truncate()
            # Convert data back to json 
            json.dump(fileData, file, indent = 4)
        print("Hurray! Successfully Deleted.")
        showNotebook("1")

def update(fileData):
    with open("data.json",'r+') as file: 
        file.seek(0) 
        # to erase all data 
        file.truncate()
        # Convert data back to json 
        json.dump(fileData, file, indent = 4)
    print("Hurray! Successfully Updated.")

def updateParticularPage(searchNo):
    os.system('cls')
    file = open("data.json")
    fileData = json.load(file)
    file.close()
    showParticularPage(searchNo,fileData)
    searchNo = int(searchNo) - 1
    choice = input("Press T for Title Update or Press D for Description Update: ")
    if choice == 'T':
        addTitle = input("Enter the word/sentence you want to add: ")
        title = fileData[searchNo]["Title"] + " " + addTitle
        # title = title + " " + addTitle
        fileData[searchNo]["Title"] = title
        now = datetime.now()
        d = now.strftime("%d/%m/%Y %H:%M:%S")
        fileData[searchNo]["Modification-Date"] = d
        update(fileData)
        input("Press Enter to See The new Content...")
        showParticularPage(searchNo+1,fileData)

    elif choice == 'D':
        addDes = input("Enter the word/sentence you want to add: ")
        des = fileData[searchNo]["Description"] + " " + addDes
        fileData[searchNo]["Description"] = des
        now = datetime.now()
        d = now.strftime("%d/%m/%Y %H:%M:%S")
        fileData[searchNo]["Modification-Date"] = d
        update(fileData)
        input("Press Enter to See The new Content...")
        showParticularPage(searchNo+1,fileData)
    else:
        print("Wrong Choice!!!")


def updatePage():
    os.system('cls')
    totalPage = showNotebook('update')
    counter = str(totalPage)
    choice = input("Do You Want To Update? If You Want Than Enter The Serial Number otherwise N: ")
    if choice>="1" and choice<=counter:
        updateParticularPage(choice)


i = 1
while i:
    # Clearing the Screen
    os.system('cls')
    print("\t\t\t\t Welcome To Our Notebook World!!!")
    print("\t\t\t\t Features of Our Notebook")
    print("\t\t\t\t 1.Show all Notebook Title")
    print("\t\t\t\t 2.Add New Notebook Page")
    print("\t\t\t\t 3.Delete Notebook Page")
    print("\t\t\t\t 4.Update Existing Notebook Page")
    print("\t\t\t\t 5.Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        showNotebook('1')
    elif choice == '2':
        addNewPage()
    elif choice == '3':
        deletePage()
    elif choice == '4':
        updatePage()
    elif choice == '5':
        break
    else:
        print("Wrong Choice!!! Try Again")
    input("Press Enter to Continue...")
        