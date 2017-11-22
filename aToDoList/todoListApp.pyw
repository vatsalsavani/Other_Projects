#Import Modules
import tkinter
import _tkinter
import random
import tkinter.messagebox
import sys

from tkinter import *

w = 20
fontC = "white"
bgC = "black"
border = 1
hT = 0
bW = 0



tasks = []
doneTasks=[]

#from todolist import *

def updateList():
        clearList()
        for index in range(0,len(tasks)):
                item = "{} {}".format(index+1,tasks[index])
                lb_tasks.insert("end",item)

def clearList():
        lb_tasks.delete(0,"end")

def addTask():
        task = txt_input.get()
        if task != "":
                tasks.append(task)
                updateList()
        else:
                tkinter.messagebox.showwarning("Warning!", "You need to enter in a task!")
        txt_input.delete(0,"end")
        
def removeTask():
        task = list(lb_tasks.get("active"))
        i = int(task[0])
        del tasks[i-1]
        updateList()
        
def doneTask():
        task = list(lb_tasks.get("active"))
        i = int(task[0])
        doneTasks.append(tasks[i-1])
        tkinter.messagebox.showwarning("Task Completed","Your specified task:\n\t {} \n has been Completed".format(tasks[i-1]))
        del tasks[i-1]
        updateList()

def allDone():
        global doneTasks, tasks
        confirmed2 = tkinter.messagebox.askyesno("Please Confirm","Are you sure you would like to mark all tasks as completed?")
        if confirmed2 == True:
                for i in range(0,len(tasks)):
                        doneTasks.append(tasks[i])
                tasks = []
                updateList()
        
def viewTasks():
        updateList()
        lbl_display["text"] = "Showing Current Tasks"
        
def viewDone():
        clearList()
        lbl_display["text"]="Showing Completed Tasks"
        for done in doneTasks:
                lb_tasks.insert("end",done)
                
def deleteAll():
        global tasks
        confirmed= tkinter.messagebox.askyesno("Please Confirm", "Are you sure you want to delete all tasks?")
        if confirmed == True:
                tasks = []
                updateList()
        
def amountTasks():
        noTasks = len(tasks)
        alert = "Numer of tasks: %s" %noTasks
        lbl_display["text"] = alert
        
def sortAscending():
        tasks.sort()
        lbl_display["text"]="Sorted in Ascending Order"
        updateList()
        
def sortDescending():
        tasks.sort()
        tasks.reverse()
        lbl_display["text"]="Sorted in Descending Order"
        updateList()


#Create root window
root = tkinter.Tk()

#Change root window background colour
root.configure(bg = "white")

#Change window size
root.geometry("430x225")

#Change the title
root.title("T, The World's Most Minimalistic To-Do List")

lbl_title = tkinter.Label(root, text="T, The World's Most Minimalistic To-Do List", fg="black",bg="white",borderwidth = bW,bd=border,highlightthickness=hT)
lbl_title.grid(row=0,column=0, columnspan=3)

lbl_display = tkinter.Label(root, text="", bg="white",borderwidth = bW,bd=border,highlightthickness=hT)
lbl_display.grid(row=1,column=0,columnspan=3)

txt_input = tkinter.Entry(root,width=w,bg="white",borderwidth = bW,bd=border,highlightthickness=hT)
txt_input.grid(row=2,column=0)


#Button Add Task
btn_addTask = tkinter.Button(root, text="Add Task", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW, bd=border,command=addTask)
btn_addTask.grid(row=2,column=1)

#Button Remove Task
btn_removeTask = tkinter.Button(root, text="Remove Task", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW,bd=border, command=removeTask)
btn_removeTask.grid(row=3,column=0)

#Remove All
btn_deleteAll = tkinter.Button(root, text="Remove All Tasks", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW,bd=border, command=deleteAll)
btn_deleteAll.grid(row=3,column=1)

#Button Done Certain Task
btn_doneTask = tkinter.Button(root, text="Mark Done", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW, bd=border,command=doneTask)
btn_doneTask.grid(row=4,column=0)

#Button Done All
btn_allDone = tkinter.Button(root, text="Mark All As Done", fg=fontC, bg=bgC, width=w,highlightthickness=hT,borderwidth=bW, bd=border, command=allDone)
btn_allDone.grid(row=4, column=1)

#Button View Current
btn_viewTasks = tkinter.Button(root, text="View Current Tasks", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW, bd=border,command=viewTasks)
btn_viewTasks.grid(row=6,column=0)

#Button View Completed
btn_viewDone = tkinter.Button(root, text="View Completed Tasks", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW,bd=border, command=viewDone)
btn_viewDone.grid(row=6,column=1)

#Sort Ascending
btn_sortAscending = tkinter.Button(root, text="Sort Ascending", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW, bd=border,command=sortAscending)
btn_sortAscending.grid(row=5,column=0)

#Sort Descending
btn_sortDescending = tkinter.Button(root, text="Sort Descending", fg=fontC, bg=bgC, width=w, highlightthickness=hT, borderwidth = bW,bd=border,command=sortDescending)
btn_sortDescending.grid(row=5,column=1)



#Total number of Tasks
#btn_amountTasks = tkinter.Button(root, text="Total Number of Tasks", fg=fontC, bg=bgC, width=w, highlightthickness=hT,borderwidth = bW,bd=border, command=amountTasks)
#btn_amountTasks.grid(row=10,column=0)

lb_tasks = tkinter.Listbox(width=w,highlightthickness=1,bd=1,borderwidth=1)
lb_tasks.grid(row=2,column=2,rowspan=5)

#Exit
btn_exit = tkinter.Button(root, text="Exit", fg="white", bg="black",width=59, highlightthickness=hT, borderwidth = bW,bd=border, command=root.destroy)
btn_exit.grid(row=7,column=0,columnspan=3)

#Start the main events loop
root.mainloop()

