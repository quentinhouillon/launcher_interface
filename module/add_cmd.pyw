from tkinter import *
from json import dump, load

with open("file\\run.json", 'r') as file:
    run = load(file)

with open("file\\theme.json", 'r') as theme:
    th = load(theme)

def execute_app(event):
    lnk_e.focus()

    global get_app
    get_app = app_e.get()

def execute_lnk(event):
    cmd_e.focus()

    global get_lnk
    get_lnk = lnk_e.get()

def execute_cmd(event):
    global get_cmd
    get_cmd = cmd_e.get()

    to_append = {
        "app": get_app,
        "lnk": get_lnk,
        "cmd": get_cmd}

    with open("file\\run.json", 'w') as file:
        run.append(to_append)
        dump(run, file, indent=4)
        exit()

color1 = th["my_theme"]["bg"]
color2 = th["my_theme"]["fg"]
color3 = th["my_theme"]["ft"]
tf = "consolas"

window = Tk()
app_text = StringVar()
lnk_text = StringVar()
cmd_text = StringVar()

#WINDOW
window.title("add - command")
window.geometry("200x250")
window.minsize(200,250)
window.iconbitmap("img\\favicon.ico")
window.configure(cursor="pirate", bg=color1)

#LABEL
app = Label(text="app: ", bg=color1, fg=color2, font=tf, anchor="w")
lnk = Label(text="lnk: ", bg=color1, fg=color2, font=tf, anchor="w")
cmd = Label(text="cmd: ", bg=color1, fg=color2, font=tf, anchor="w")

#ENTRY
app_e = Entry(bd=0, bg=color1, fg=color2, insertbackground=color2,
              textvariable=app_text, font=tf)
app_e.focus()

lnk_e = Entry(bd=0, bg=color1, fg=color2, insertbackground=color2,
              textvariable=lnk_text, font=tf)

cmd_e = Entry(bd=0, bg=color1, fg=color2, insertbackground=color2,
              textvariable=cmd_text, font=tf)

app_e.bind('<Return>', execute_app)
lnk_e.bind('<Return>', execute_lnk)
cmd_e.bind('<Return>', execute_cmd)

#GRID
app.grid(row=0, column=0)
app_e.grid(row=0, column=1)

lnk.grid(row=1, column=0)
lnk_e.grid(row=1, column=1)

cmd.grid(row=2, column=0)
cmd_e.grid(row=2, column=1)

window.mainloop()
