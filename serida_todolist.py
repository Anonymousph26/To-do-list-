#######Leader: Serida,Danwen C. ####################
import customtkinter
import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox

### background_color in windows 
customtkinter.set_appearance_mode("dark")

####Window_loop 
ds=ctk.CTk()
ds.title("My-To-Do-List App " "developed by; Serida")
ds.geometry("500x500")
###String variable to use for text content in button and label 
font1 = ("Arial",30,'bold')
font2 = ("Arial",18,'bold')
font3 = ("Arial",10,'bold')
height_btn = 50

############ {Function for using each button}#####
def clearall():
    tasks_list.delete(0, END)
    save_tasks()

def completed():
    chosen = tasks_list.curselection()
    if chosen:
        tasks_list.itemconfig(chosen[0], bg="#39e629")
        save_tasks()
    else: 
        messagebox.showerror('Error', 'Pls.Try again later  (_)')
def add_task():
    task = task_entry.get()
    if task: 
        tasks_list.insert(0, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Enter a Task")#gives alert message from user 

def remove_task(): 
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else: 
        messagebox.showerror("Error", "Choose a Task to delete.")
######This function that automatically saved your progression of task 
def save_tasks():
    with open("tasks.txt", "w") as f: 
        tasks = tasks_list.get(0,END)
        for task in tasks: 
            f.write(task + "/n")
######This function that automatically load your progression of task 
def load_tasks():
    try: 
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks: 
                tasks_list.insert(0, task.strip())
    except FileNotFoundError:
        messagebox.showerror("Error_404", "Connot load tasks.")
#### Title of the app 
text_label = customtkinter.CTkLabel(ds,font=font1,text='"My-To-Do-List"', text_color='#fff')
text_label.place(x=132,y=20)

####TAsk_Entry_for_user or mao ni ang box entry na mo input ang usa ka user 
task_entry = customtkinter.CTkEntry(ds, font=font2,text_color='#000',fg_color='#fff',border_color='#fff', width=280)
task_entry.place(x=42,y=140)
#List_Box
frame_1 = Frame(ds,bd=3,width=700,height=280,bg="#32405b")
frame_1.place(x=40, y=179)
tasks_list = Listbox(frame_1, width=39, height=15,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff",font=font3)
tasks_list.pack(side=LEFT, fill=BOTH, padx=2)

##Scroll_Function
scrollbar = Scrollbar(frame_1)
scrollbar.pack(side=RIGHT, fill=BOTH)
tasks_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_list.yview)


add_Btn =  ctk.CTkButton(ds,font=font2 ,text="Add Task_list",text_color='#fff',fg_color='#06911f',hover_color='#96061c',bg_color="#09112e",corner_radius=6, height=50,width=85,cursor='hand2', command=add_task)
add_Btn.grid(row=7, column=0, padx=75.0, pady=80.0)

remove_Btn = ctk.CTkButton(ds, text="Delete", height=height_btn,fg_color='#b82306',font=font2,cursor='hand2',command=remove_task)
remove_Btn.place(x=220, y=80)

clear_Btn = ctk.CTkButton(ds,text="Clear Task", font=font2, hover_color="aqua",height=height_btn, cursor='hand2', command=clearall)
clear_Btn.place(x=350, y=190)

complete_Btn = ctk.CTkButton(ds, text='Complete', height=height_btn,font=font2,hover_color='#20ba2a', cursor='hand2',command=completed)
complete_Btn.grid(row=9, column=1, padx=68, pady=60.0)

load_tasks()
ds.mainloop()