from tkinter import *

def load_tasks(listbox):
    try:
        with open('tasks.txt', 'r') as tasks_list_file:
            for task in tasks_list_file:
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        print("File not found. Creating a new one.")

def add_item(entry, listbox):
    new_task = entry.get().strip()

    if new_task:
        listbox.insert(END, new_task)

        with open('tasks.txt', 'a') as tasks_list_file:
            tasks_list_file.write(f'\n{new_task}')

        entry.delete(0, END)  # Clear the entry after adding

def delete_item(listbox):
    selected_task = listbox.get(ACTIVE)

    listbox.delete(ACTIVE)

    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()
        tasks_list_file.seek(0)

        for line in lines:
            if selected_task != line.strip():
                tasks_list_file.write(line)

        tasks_list_file.truncate()

def main():
    root = Tk()
    root.title('To-Do List')
    root.geometry('300x400')
    root.resizable(0, 0)
    root.config(bg="Blue")

    Label(root, text='To Do List', bg='Blue', font=("Comic Sans MS", 15), wraplength=300).place(x=35, y=0)

    tasks = Listbox(root, selectbackground='Black', bg='Silver', font=('Helvetica', 12), height=12, width=25)
    tasks.place(x=35, y=50)

    scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
    scroller.place(x=260, y=50, height=232)
    tasks.config(yscrollcommand=scroller.set)

    load_tasks(tasks)

    new_item_entry = Entry(root, width=37)
    new_item_entry.place(x=35, y=310)

    add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                    command=lambda: add_item(new_item_entry, tasks))
    add_btn.place(x=45, y=350)

    delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                    command=lambda: delete_item(tasks))
    delete_btn.place(x=150, y=350)

    root.mainloop()

if __name__ == "__main__":
    main()
