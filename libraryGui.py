from cProfile import label
from pydoc_data.topics import topics
from tkinter import*
from matplotlib.pyplot import grid

from pyparsing import col
import library_database as db



window = Tk()
window.title("Library app")
window.geometry("1000x500")

def getSelectedRow(event):
    try:
        global selectedTuple
        index = list1.curselection()[0]
        selectedTuple = list1.get(index)
    except:
        pass


def addBook(topic,author):
    db.insert(topic,author)
    addDialog.destroy()
    viewCommand()

def UpdateBook(id,topic ,author):
    db.update(id,topic,author)
    updateDialog.destroy()
    viewCommand()

def deleteBook (id):
    id= str(id)
    db.delete(id)
    deleteDialog.destroy()
    viewCommand()

def viewCommand():
    list1.delete(0,END)
    for row in db.view_all():
        list1.insert(END,row)
    


def addBookDialog():
    global addDialog
    addDialog = Toplevel(window)
    topicLabel = Label(addDialog,text="Topic")
    topicLabel.grid(column=0,row=0)
    topicText= Entry(addDialog,font=("Arial",20),width=20)
    topicText.grid(column=1,row=0)

    authourLabel = Label(addDialog,text="Author")
    authourLabel.grid(column=0,row=1)
    authourText= Entry(addDialog,font=("Arial",20),width=20)
    authourText.grid(column=1,row=1)

    topicText.get()
    authourText.get()
    btnSave =Button(addDialog,text="Save",padx=10,command=lambda:addBook(topicText.get(),authourText.get()))
    btnSave.grid(column=1,row=2)

def UpdateBookDialog(id,topic,author):
    global updateDialog
    updateDialog = Toplevel(window)

    updateTopicLabel =Label(updateDialog,text="Topic")
    updateTopicLabel.grid(column=0,row=1)
    updateTopictxt = Entry(updateDialog,font=("Arial",15),width=20)
    updateTopictxt.insert(END,topic)
    updateTopictxt.grid(column=1,row=1)

    updateAuthorLabel =Label(updateDialog,text="Author")
    updateAuthorLabel.grid(column=0,row=2)
    updateAuthortxt = Entry(updateDialog,font=("Arial",15),width=20)
    updateAuthortxt.grid(column=1,row=2)
    updateAuthortxt.insert(END,author)


    btnUpdate = Button(updateDialog,text="Update",command=lambda:UpdateBook(id,updateTopictxt.get(),updateAuthortxt.get()))
    btnUpdate.grid(column=1,row=3)


def deleteBookDialog():
    global deleteDialog
    deleteDialog= Toplevel(window) 
    sureMeter = Label(deleteDialog, text="Are you sure",font=("Arial Bold",20))
    sureMeter.grid(column=0 ,row=0 )

    btnYes = Button(deleteDialog,text="Yes",font=("Arial",18),fg="red",command=lambda:deleteBook(selectedTuple[0]))
    btnYes.grid(column=0,row=1)

    btnNo = Button(deleteDialog,text="No",font=("Arial",18),fg="green",command=lambda:deleteDialog.destroy())
    btnNo.grid(column=1,row=1)



# add new button 
btnAdd= Button(window,text="Add book",command=addBookDialog,width=17)
btnAdd.grid(row=2,column=3)

#update Button
btnUpdate = Button(window,text="Update Book" ,width=15,font=("Arial",10),command=lambda: UpdateBookDialog(selectedTuple[0],selectedTuple[1],selectedTuple[2]))
btnUpdate.grid(column=3,row=3)

#list box 
list1=  Listbox(window,height=10,width=35)
list1.grid(column=0,row=0,rowspan=6,columnspan=2)

#scroll bar 
scb1 = Scrollbar(window)
scb1.grid(row=2,column=2,rowspan=6)

list1.bind("<<ListboxSelect>>",getSelectedRow)
list1.configure(yscrollcommand=scb1.set)
scb1.configure(command=list1.yview)

# to view all the books in the digital library 
btnViewAll =  Button(window,text="view All ",width=17,command=viewCommand)
btnViewAll.grid(column=0,row=7)

#To delete the selected row
btnDelete = Button(window,text="Delete",width=20,command=deleteBookDialog)
btnDelete.grid(column=3,row=4)



window.mainloop()