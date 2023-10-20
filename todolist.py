from tkinter import *
import tkinter.messagebox

def entertask():
    def add():
        input_text = entry_task.get("1.0", "end-1c")
        if input_text.strip():  # Check if the input is not just whitespace
            listbox_task.insert(END, input_text.strip())  # Strip the input of leading/trailing spaces
            root1.destroy()
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")

    root1 = Toplevel()
    root1.title("Add Task")
    root1.geometry("300x150")
    imageicon = PhotoImage(file="add.png")
    root1.iconphoto(False, imageicon)
    root1.resizable(False, False)

    entry_task = Text(root1, width=30, height=4, font=("Helvetica", 12))
    entry_task.pack(pady=10)

    button_temp = Button(root1, text="Add Task", command=add, bg="#088F8F", fg="white", font=("Helvetica", 12))
    button_temp.pack()

def deletetask():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected)

def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        task_text = listbox_task.get(temp)
        # Create a Label widget with custom styling
        task_label = Label(frame_task, text=task_text, font=("Helvetica", 12, "italic"), fg="darkblue")
        task_label.pack(anchor=W)
        listbox_task.delete(temp)  

def delete_completed_tasks():
    for widget in frame_task.winfo_children():
        if widget.winfo_class() == 'Label':
            widget.destroy()

window = Tk()
window.title("To-Do List")
window.configure(bg="lightgray")
image_icon = PhotoImage(file="logo.png")
window.iconphoto(False, image_icon)

frame_task = Frame(window)
frame_task.pack(pady=10)

listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font=("Helvetica", 12))
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add Task", width=50, command=entertask, bg="#088F8F", fg="white", font=("Helvetica", 12))
entry_button.pack(pady=10)

delete_button = Button(window, text="Delete Selected Task", width=50, command=deletetask, bg="#9F2B68", fg="white", font=("Helvetica", 12))
delete_button.pack(pady=10)

mark_button = Button(window, text="Mark as Completed", width=50, command=markcompleted, bg="#0F52BA", fg="white", font=("Helvetica", 12))
mark_button.pack(pady=10)

delete_completed_button = Button(window, text="Clear Completed Tasks", width=50, command=delete_completed_tasks, bg="#E0115F", fg="white", font=("Helvetica", 12))
delete_completed_button.pack(pady=10)

window.mainloop()