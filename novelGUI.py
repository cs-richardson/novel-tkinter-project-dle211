from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

import sqlite3 as sq

con = sq.connect("/Users/tuandunglephan/Desktop/IB CS/sql/novel.db")
c = con.cursor()

def getAuthors():
    c.execute("SELECT * FROM Authors")
    data = c.fetchall()
    return data

def getConsumers():
    c.execute("SELECT * FROM Consumers")
    data = c.fetchall()
    return data

def getNovels():
    c.execute("SELECT * FROM Novels")
    data = c.fetchall()
    return data

def getPurchases():
    c.execute("SELECT * FROM Purchases")
    data = c.fetchall()
    return data

def registerAuthor(name, date):
    authors = getAuthors()
    ins_str = 'INSERT INTO Authors VALUES (' + str(authors[-1][0] + 1) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def registerConsumer(name, date):
    consumers = getConsumers()
    ins_str = 'INSERT INTO Consumers VALUES (' + str(consumers[-1][0] + 1) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def registerNovel(authorID, name, date):
    novels = getNovels()
    ins_str = 'INSERT INTO Novels VALUES (' + str(novels[-1][0] + 1) + ', ' + str(authorID) + ', "' + str(name) + '", "' + str(date) + '");'
    c.execute(ins_str)
    con.commit()

def logPurchase(consumerID, novelID, date, quantity):
    ins_str = 'INSERT INTO Purchases VALUES (' + str(consumerID) + ', ' + str(novelID) + ', "' + str(date) + '", ' + str(quantity) + ');'
    c.execute(ins_str)
    con.commit()
   

def renderMainMenu():
    mainWndw = Tk()
    mainWndw.title("Amazone")
    mainWndw.geometry("200x125")

    infoFrm = Frame(mainWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu")
    infoLbl.pack()

    registerBtn = Button(mainWndw, text = "Register", width = 10, command = renderRegistrationMenu)
    registerBtn.pack()

    purchaseBtn = Button(mainWndw, text = "Purchase", width = 10, command = renderPurchaseRequest)
    purchaseBtn.pack()

    adminBtn = Button(mainWndw, text = "Admin", width = 10, command = renderAdminRequest)
    adminBtn.pack()

    exitBtn = Button(mainWndw, text = "Exit", width = 10, command = lambda:endProgram(mainWndw))
    exitBtn.pack()
    mainWndw.mainloop()


def renderRegistrationMenu():
    registrationWndw = Tk()
    registrationWndw.title("Amazone")
    registrationWndw.geometry("200x125")

    infoFrm = Frame(registrationWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Register")
    infoLbl.pack()

    authorBtn = Button(registrationWndw, text = "As an Author", width = 15, command = renderAuthorRequest)
    authorBtn.pack()

    consumerBtn = Button(registrationWndw, text = "As a Consumer", width = 15, command = renderConsumerRequest)
    consumerBtn.pack()

    novelBtn = Button(registrationWndw, text = "As a Novel", width = 15, command = renderNovelRequest)
    novelBtn.pack()

    backBtn = Button(registrationWndw, text = "Back", width = 15, command = lambda:closeWindow(registrationWndw))
    backBtn.pack()

    registrationWndw.mainloop()


def renderAdminRequest():
    loginWndw = Tk()
    loginWndw.title("Amazone")
    loginWndw.geometry("200x100")

    infoFrm = Frame(loginWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin")
    infoLbl.pack()

    passwordFrm = Frame(loginWndw)
    passwordFrm.pack()
    passwordLbl = Label(passwordFrm, text = "Password")
    passwordLbl.pack()

    pswd = tk.StringVar(loginWndw)

    passwordEty = Entry(passwordFrm, text = "Password", textvariable = pswd)
    passwordEty.pack()
    passwordBtn = Button(passwordFrm, text = "Enter", width = 10, command = lambda: attemptLogin(loginWndw, pswd.get()))
    passwordBtn.pack()

    loginWndw.mainloop()


def attemptLogin(window, password):
    if password == "1234":
        window.destroy()
        renderAdminMenu()
    else:
        messagebox.showinfo("Error", "Incorrect password.")


def renderAdminMenu():
    adminWndw = Tk()
    adminWndw.title("Amazone")
    adminWndw.geometry("200x150")

    infoFrm = Frame(adminWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin")
    infoLbl.pack()

    authorBtn = Button(adminWndw, text = "Author Report", width = 15, command = renderAuthorReport)
    authorBtn.pack()

    consumerBtn = Button(adminWndw, text = "Consumer Report", width = 15, command = renderConsumerReport)
    consumerBtn.pack()

    novelBtn = Button(adminWndw, text = "Novel Report", width = 15, command = renderNovelReport)
    novelBtn.pack()

    purchaseBtn = Button(adminWndw, text = "Purchase Report", width = 15, command = renderPurchaseReport)
    purchaseBtn.pack()

    backBtn = Button(adminWndw, text = "Back", width = 15, command = lambda:closeWindow(adminWndw))
    backBtn.pack()

    adminWndw.mainloop()


def closeWindow(window):
    window.destroy()


def endProgram(window):
    con.close()
    window.destroy()


def renderAuthorReport():
    infoAuthorWndw = Tk()
    infoAuthorWndw.title("Amazone")
    infoAuthorWndw.geometry("600x600")

    infoFrm = Frame(infoAuthorWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin > Author Report")
    infoLbl.pack()

    okBtn = Button(infoAuthorWndw, text = "OK", width = 10, command = lambda: closeWindow(infoAuthorWndw))
    okBtn.pack()

    authors = getAuthors()

    infoAuthorTable = "––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    infoAuthorTable += "\nAuthorID\t\tAuthorName\tDateOfBirth"
    infoAuthorTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    for r in range(len(authors)):
        infoAuthorTable += "\n"

        for c in range(len(authors[r])):
            if len(str(authors[r][c])) <= 9 and c != 2:
                infoAuthorTable += str(authors[r][c]) + "\t\t"
            elif len(str(authors[r][c])) > 9 and c != 2:
                infoAuthorTable += str(authors[r][c]) + "\t"
            else:
                infoAuthorTable += str(authors[r][c])

        infoAuthorTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––"
    
    infoAuthorLbl = Label(infoAuthorWndw, text = infoAuthorTable, justify = LEFT)
    infoAuthorLbl.pack()

    infoAuthorWndw.mainloop()


def renderConsumerReport():
    infoConsumerWndw = Tk()
    infoConsumerWndw.title("Amazone")
    infoConsumerWndw.geometry("600x600")

    infoFrm = Frame(infoConsumerWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin > Consumer Report")
    infoLbl.pack()

    okBtn = Button(infoConsumerWndw, text = "OK", width = 10, command = lambda: closeWindow(infoConsumerWndw))
    okBtn.pack()

    consumers = getConsumers()

    infoConsumerTable = "––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    infoConsumerTable += "\nConsumerID\tConsumerName\tDateOfBirth"
    infoConsumerTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    for r in range(len(consumers)):
        infoConsumerTable += "\n"

        for c in range(len(consumers[r])):
            if len(str(consumers[r][c])) <= 9 and c != 2:
                infoConsumerTable += str(consumers[r][c]) + "\t\t"
            elif len(str(consumers[r][c])) > 9 and c != 2:
                infoConsumerTable += str(consumers[r][c]) + "\t"
            else:
                infoConsumerTable += str(consumers[r][c])

        infoConsumerTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––"
    
    infoConsumerLbl = Label(infoConsumerWndw, text = infoConsumerTable, justify = LEFT)
    infoConsumerLbl.pack()

    infoConsumerWndw.mainloop()


def renderNovelReport():
    infoNovelWndw = Tk()
    infoNovelWndw.title("Amazone")
    infoNovelWndw.geometry("600x600")

    infoFrm = Frame(infoNovelWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin > Novel Report")
    infoLbl.pack()

    okBtn = Button(infoNovelWndw, text = "OK", width = 10, command = lambda: closeWindow(infoNovelWndw))
    okBtn.pack()

    novels = getNovels()

    infoNovelTable = "––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    infoNovelTable += "\nNovelID\t\tAuthorID\t\tNovelName\tDateOfPublication"
    infoNovelTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    for r in range(len(novels)):
        infoNovelTable += "\n"

        for c in range(len(novels[r])):
            if len(str(novels[r][c])) <= 9 and c != 3:
                infoNovelTable += str(novels[r][c]) + "\t\t"
            elif len(str(novels[r][c])) > 9 and c != 3:
                infoNovelTable += str(novels[r][c]) + "\t"
            else:
                infoNovelTable += str(novels[r][c])

        infoNovelTable += "\n––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"
    
    infoNovelLbl = Label(infoNovelWndw, text = infoNovelTable, justify = LEFT)
    infoNovelLbl.pack()

    infoNovelWndw.mainloop()


def renderPurchaseReport():
    infoPurchaseWndw = Tk()
    infoPurchaseWndw.title("Amazone")
    infoPurchaseWndw.geometry("600x600")

    infoFrm = Frame(infoPurchaseWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Admin > Purchase Report")
    infoLbl.pack()

    okBtn = Button(infoPurchaseWndw, text = "OK", width = 10, command = lambda: closeWindow(infoPurchaseWndw))
    okBtn.pack()

    purchases = getPurchases()

    infoPurchaseTable = "–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    infoPurchaseTable += "\nConsumerID\tNovelID\t\tDateOfPurchase\tQuantity"
    infoPurchaseTable += "\n–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"

    for r in range(len(purchases)):
        infoPurchaseTable += "\n"

        for c in range(len(purchases[r])):
            if len(str(purchases[r][c])) <= 9 and c != 3:
                infoPurchaseTable += str(purchases[r][c]) + "\t\t"
            elif len(str(purchases[r][c])) > 9 and c != 3:
                infoPurchaseTable += str(purchases[r][c]) + "\t"
            else:
                infoPurchaseTable += str(purchases[r][c])

        infoPurchaseTable += "\n–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"
    
    infoPurchaseLbl = Label(infoPurchaseWndw, text = infoPurchaseTable, justify = LEFT)
    infoPurchaseLbl.pack()

    infoPurchaseWndw.mainloop()


def renderAuthorRequest():
    registerAuthorWndw = Tk()
    registerAuthorWndw.title("Amazone")
    registerAuthorWndw.geometry("400x400")

    infoFrm = Frame(registerAuthorWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Register > Author")
    infoLbl.pack()

    backBtn = Button(infoFrm, text = "Back", width = 10, command = lambda: closeWindow(registerAuthorWndw))
    backBtn.pack()

    inputFrm = Frame(registerAuthorWndw)
    inputFrm.pack(side = LEFT)
    inputLbl = Label(inputFrm, text = "Inputs")
    inputLbl.pack()

    dd = tk.StringVar(registerAuthorWndw)
    mm = tk.StringVar(registerAuthorWndw)
    yyyy = tk.StringVar(registerAuthorWndw)
    name = tk.StringVar(registerAuthorWndw)

    dayLbl = Label(inputFrm, text = "Day")
    dayLbl.pack()
    dayEty = Entry(inputFrm, text = "DD", textvariable = dd)
    dayEty.pack()

    monthLbl = Label(inputFrm, text = "Month")
    monthLbl.pack()
    monthEty = Entry(inputFrm, text = "MM", textvariable = mm)
    monthEty.pack()

    yearLbl = Label(inputFrm, text = "Year")
    yearLbl.pack()
    yearEty = Entry(inputFrm, text = "YYYY", textvariable = yyyy)
    yearEty.pack()

    nameLbl = Label(inputFrm, text = "Name")
    nameLbl.pack()
    nameEty = Entry(inputFrm, text = "NAME", textvariable = name)
    nameEty.pack()

    optionFrm = Frame(registerAuthorWndw)
    optionFrm.pack(side = RIGHT)
    optionLbl = Label(optionFrm, text = "Options")
    optionLbl.pack()

    noneLbl = Label(optionFrm, text = "None")
    noneLbl.pack()

    registerAuthorBtn = Button(inputFrm, text = "Register Author", width = 15,
                 command = lambda: checkAndEnterAuthorSelection(dd.get(), mm.get(), yyyy.get(),
                 name.get()))
    registerAuthorBtn.pack()

    registerAuthorWndw.mainloop()


def renderConsumerRequest():
    registerConsumerWndw = Tk()
    registerConsumerWndw.title("Amazone")
    registerConsumerWndw.geometry("400x400")

    infoFrm = Frame(registerConsumerWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Register > Consumer")
    infoLbl.pack()

    backBtn = Button(infoFrm, text = "Back", width = 10, command = lambda: closeWindow(registerConsumerWndw))
    backBtn.pack()

    inputFrm = Frame(registerConsumerWndw)
    inputFrm.pack(side = LEFT)
    inputLbl = Label(inputFrm, text = "Inputs")
    inputLbl.pack()

    dd = tk.StringVar(registerConsumerWndw)
    mm = tk.StringVar(registerConsumerWndw)
    yyyy = tk.StringVar(registerConsumerWndw)
    name = tk.StringVar(registerConsumerWndw)

    dayLbl = Label(inputFrm, text = "Day")
    dayLbl.pack()
    dayEty = Entry(inputFrm, text = "DD", textvariable = dd)
    dayEty.pack()

    monthLbl = Label(inputFrm, text = "Month")
    monthLbl.pack()
    monthEty = Entry(inputFrm, text = "MM", textvariable = mm)
    monthEty.pack()

    yearLbl = Label(inputFrm, text = "Year")
    yearLbl.pack()
    yearEty = Entry(inputFrm, text = "YYYY", textvariable = yyyy)
    yearEty.pack()

    nameLbl = Label(inputFrm, text = "Name")
    nameLbl.pack()
    nameEty = Entry(inputFrm, text = "NAME", textvariable = name)
    nameEty.pack()

    optionFrm = Frame(registerConsumerWndw)
    optionFrm.pack(side = RIGHT)
    optionLbl = Label(optionFrm, text = "Options")
    optionLbl.pack()

    noneLbl = Label(optionFrm, text = "None")
    noneLbl.pack()

    registerConsumerBtn = Button(inputFrm, text = "Register Consumer", width = 15,
                 command = lambda: checkAndEnterConsumerSelection(dd.get(), mm.get(), yyyy.get(),
                 name.get()))
    registerConsumerBtn.pack()

    registerConsumerWndw.mainloop()


def renderNovelRequest():
    registerNovelWndw = Tk()
    registerNovelWndw.title("Amazone")
    registerNovelWndw.geometry("400x400")

    infoFrm = Frame(registerNovelWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Register > Novel")
    infoLbl.pack()

    backBtn = Button(infoFrm, text = "Back", width = 10, command = lambda: closeWindow(registerNovelWndw))
    backBtn.pack()

    inputFrm = Frame(registerNovelWndw)
    inputFrm.pack(side = LEFT)
    inputLbl = Label(inputFrm, text = "Inputs")
    inputLbl.pack()

    dd = tk.StringVar(registerNovelWndw)
    mm = tk.StringVar(registerNovelWndw)
    yyyy = tk.StringVar(registerNovelWndw)
    name = tk.StringVar(registerNovelWndw)

    dayLbl = Label(inputFrm, text = "Day")
    dayLbl.pack()
    dayEty = Entry(inputFrm, text = "DD", textvariable = dd)
    dayEty.pack()

    monthLbl = Label(inputFrm, text = "Month")
    monthLbl.pack()
    monthEty = Entry(inputFrm, text = "MM", textvariable = mm)
    monthEty.pack()

    yearLbl = Label(inputFrm, text = "Year")
    yearLbl.pack()
    yearEty = Entry(inputFrm, text = "YYYY", textvariable = yyyy)
    yearEty.pack()

    nameLbl = Label(inputFrm, text = "Name")
    nameLbl.pack()
    nameEty = Entry(inputFrm, text = "NAME", textvariable = name)
    nameEty.pack()

    optionFrm = Frame(registerNovelWndw)
    optionFrm.pack(side = RIGHT)
    optionLbl = Label(optionFrm, text = "Options")
    optionLbl.pack()

    authors = getAuthors()
    authorLtbx = renderAuthorListbox(registerNovelWndw, optionFrm, authors)

    registerNovelBtn = Button(inputFrm, text = "Register Novel", width = 15,
                 command = lambda: checkAndEnterNovelSelection(dd.get(), mm.get(), yyyy.get(),
                 authors[authorLtbx.curselection()[0]][0],
                 name.get()))
    registerNovelBtn.pack()

    registerNovelWndw.mainloop()


def renderPurchaseRequest():
    purchaseWndw = Tk()
    purchaseWndw.title("Amazone")
    purchaseWndw.geometry("400x400")

    infoFrm = Frame(purchaseWndw)
    infoFrm.pack()
    infoLbl = Label(infoFrm, text = "Main Menu > Purchase")
    infoLbl.pack()

    backBtn = Button(infoFrm, text = "Back", width = 10, command = lambda: closeWindow(purchaseWndw))
    backBtn.pack()

    inputFrm = Frame(purchaseWndw)
    inputFrm.pack(side = LEFT)
    inputLbl = Label(inputFrm, text = "Inputs")
    inputLbl.pack()

    dd = tk.StringVar(purchaseWndw)
    mm = tk.StringVar(purchaseWndw)
    yyyy = tk.StringVar(purchaseWndw)
    quantity = tk.IntVar(purchaseWndw)

    dayLbl = Label(inputFrm, text = "Day")
    dayLbl.pack()
    dayEty = Entry(inputFrm, text = "DD", textvariable = dd)
    dayEty.pack()

    monthLbl = Label(inputFrm, text = "Month")
    monthLbl.pack()
    monthEty = Entry(inputFrm, text = "MM", textvariable = mm)
    monthEty.pack()

    yearLbl = Label(inputFrm, text = "Year")
    yearLbl.pack()
    yearEty = Entry(inputFrm, text = "YYYY", textvariable = yyyy)
    yearEty.pack()

    quantityLbl = Label(inputFrm, text = "Quantity")
    quantityLbl.pack()
    quantityEty = Entry(inputFrm, text = "QUANTITY", textvariable = quantity)
    quantityEty.pack()

    optionFrm = Frame(purchaseWndw)
    optionFrm.pack(side = RIGHT)
    optionLbl = Label(optionFrm, text = "Options")
    optionLbl.pack()

    consumers = getConsumers()
    consumerLtbx = renderConsumerListbox(purchaseWndw, optionFrm, consumers)

    novels = getNovels()
    novelLtbx = renderNovelListbox(purchaseWndw, optionFrm, novels)

    registerNovelBtn = Button(inputFrm, text = "Purchase", width = 15,
                 command = lambda: checkAndEnterPurchaseSelection(dd.get(), mm.get(), yyyy.get(),
                 consumers[consumerLtbx.curselection()[0]][0],
                 novels[novelLtbx.curselection()[0]][0],
                 quantity.get()))
    registerNovelBtn.pack()

    purchaseWndw.mainloop()


def checkAndEnterAuthorSelection(d, m, y, n):
    try:
        dt = date(int(y), int(m), int(d))
        registerAuthor(n, dt)
        messagebox.showinfo("Success", "You have registered an author.")
    except:
        messagebox.showinfo("Error", "Possible reasons:\n- You chose an invalid date.")


def checkAndEnterConsumerSelection(d, m, y, n):
    try:
        dt = date(int(y), int(m), int(d))
        registerConsumer(n, dt)
        messagebox.showinfo("Success", "You have registered a consumer.")
    except:
        messagebox.showinfo("Error", "Possible reasons:\n- You chose an invalid date.")


def checkAndEnterNovelSelection(d, m, y, a, n):
    try:
        dt = date(int(y), int(m), int(d))
        registerNovel(a, n, dt)
        messagebox.showinfo("Success", "You have registered a novel.")
    except:
        messagebox.showinfo("Error", "Possible reasons:\n- You chose an invalid author and/or date.")


def checkAndEnterPurchaseSelection(d, m, y, c, n, q):
    try:
        dt = date(int(y), int(m), int(d))
        logPurchase(c, n, dt, q)
        messagebox.showinfo("Success", "You have purchased books.")
    except:
        messagebox.showinfo("Error", "Possible reasons:\n- There is already a purchase for that combination.\n- You chose an invalid consumer, novel and/or date.")
        return


def renderAuthorListbox(w, f, authors):
    authorLbl = Label(f, text = "AuthorID")
    authorLbl.pack(side = TOP)

    authorLtbx = Listbox(f, height = 8, width = 26, font = ("Consolas", 12), exportselection = False) 
    authorLtbx.pack(side = TOP, fill = Y)
                
    authorSb = Scrollbar(w, orient = VERTICAL)
    authorSb.config(command = authorLtbx.yview)
    authorSb.pack(side = RIGHT, fill = Y)
    authorLtbx.config(yscrollcommand = authorSb.set)
    

    i = 0
    for currentAuthor in authors:
        authorLtbx.insert(i, currentAuthor)
        i += 1
    authorLtbx.selection_set(first = 0)

    return authorLtbx


def renderConsumerListbox(w, f, consumers):
    consumerLbl = Label(f, text = "ConsumerID")
    consumerLbl.pack(side = TOP)

    consumerLtbx = Listbox(f, height = 8, width = 26, font = ("Consolas", 12), exportselection = False) 
    consumerLtbx.pack(side = TOP, fill = Y)
                
    consumerSb = Scrollbar(w, orient = VERTICAL)
    consumerSb.config(command = consumerLtbx.yview)
    consumerSb.pack(side = RIGHT, fill = Y)
    consumerLtbx.config(yscrollcommand = consumerSb.set)
    

    i = 0
    for currentConsumer in consumers:
        consumerLtbx.insert(i, currentConsumer)
        i += 1
    consumerLtbx.selection_set(first = 0)

    return consumerLtbx


def renderNovelListbox(w, f, novels):
    novelLbl = Label(f, text = "NovelID")
    novelLbl.pack(side = TOP)

    novelLtbx = Listbox(f, height = 8, width = 26, font = ("Consolas", 12), exportselection = False) 
    novelLtbx.pack(side = TOP, fill = Y)
                
    novelSb = Scrollbar(w, orient = VERTICAL)
    novelSb.config(command = novelLtbx.yview)
    novelSb.pack(side = RIGHT, fill = Y)
    novelLtbx.config(yscrollcommand = novelSb.set)
    

    i = 0
    for currentConsumer in novels:
        novelLtbx.insert(i, currentConsumer)
        i += 1
    novelLtbx.selection_set(first = 0)

    return novelLtbx


renderMainMenu()