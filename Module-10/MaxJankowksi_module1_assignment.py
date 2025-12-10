#Max Jankowski
#csd-325 module 10 assignment


import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk): # creating class todo main class for the application as specified in reading
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks: #initalizing the tasks list
            self.tasks = []
        else:
            self.tasks = tasks


        #Frame setup from reading this week, will allow for scrolling
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

#scroll bar setup from reading, setup vertical scroll
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical",
                                      command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # First modification, changing window title to my last name
        self.title("Jankowski-ToDo")
        self.geometry("300x400")

    #creating the menu bar
        self.menubar = tk.Menu(self, bg="#2C3E50", fg="#ECF0F1")  # Modified: Menu colors

        # 5th mod on the list, adding a menu with an option to exit
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="#34495E", fg="#ECF0F1")
        self.file_menu.add_command(label="Exit", command=self.exit_program)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.config(menu=self.menubar)

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0),
                                                            window=self.tasks_frame,
                                                            anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Modification 4, updating instruction to sate right click to delete
        todo1 = tk.Label(self.tasks_frame,
                         text="--- Add Items Here (Right-Click to Delete) ---",
                         bg="#F03E1D", fg="black", pady=10) # had some issues, needed to include "#" in the color ser number

        # Modification 3, changing from left click to right click
        todo1.bind("<Button-3>", self.remove_task)  # button-3 is right-click

        self.tasks.append(todo1)

        for task in self.tasks: # pack an existing task from the tutorial reading
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task) #event binding, came from readings they connect keyboard and mouse
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.colour_schemes = [{"bg": "#90EE90", "fg": "#006400"}, # alternating colors
                               {"bg": "#FFB6C6", "fg": "#8B0000"}]

#creating a method to add tasks
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip() # getting text from the entry box

        if len(task_text) > 0: # adds only if there is actual text
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task) #appling the alternating colors

            # Moodification 3 binding the right mouse button for deleting
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task) # add to tasks

        self.task_create.delete(1.0, tk.END) # clearing text from box

    def remove_task(self, event): # part of modification 3, triggering by the right click
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self): # reorders alternating colors after entry deletion
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task): # applies color selection ordered by the position
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None): # adjusting the area that can be scrolled
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event): # based on reading keeps the tasks at full width when resizing
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event): # takes care of the mouse wheel scrolling
        if event.delta: # for window machines
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else: # for linux and other
            if event.num == 5:
                move = 1
            else:
                move = -1
            self.tasks_canvas.yview_scroll(move, "units")

    def exit_program(self): # mod 5 to exit program
        """Exit the program cleanly"""
        self.destroy()


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()


# color resource page: https://colorhunt.co/