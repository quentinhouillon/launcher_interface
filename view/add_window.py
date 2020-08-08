from tkinter import *
from tkinter.messagebox import showinfo, showerror

from core.clss import Database


class WindowAdd:
    def __init__(self, bg, fg, accent):
        self.BG = bg
        self.FG = fg
        self.ACCENT = accent

        self.db = Database()

    def window_add(self, name_opening=False, event=False):
        # region: WINDOW
        self.tl_add = Toplevel(bg=self.BG)
        self.tl_add.title("Ajouter un raccourci")
        self.tl_add.iconbitmap("img/icon.ico")
        self.tl_add.geometry("360x150")
        self.tl_add.resizable(False, False)
        self.tl_add.focus_force()
        # endregion: WINDOW

        # region: ENTRY
        self.ent_shortcuts = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                insertbackground=self.FG, bd=0)

        self.ent_opening = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                insertbackground=self.FG, bd=0)
        self.ent_shortcuts.bind(
            "<Return>", lambda event: self.ent_opening.focus())
        self.ent_opening.bind("<Return>", lambda event: self.add_shortcuts(
            self.ent_shortcuts.get(), self.ent_opening.get()))
        # endregion: ENTRY

        # region: LABEL
        self.lbl_shortcuts = Label(self.tl_add,
                                text="Entrer le nom du raccourci",
                                bg=self.BG, fg=self.FG, anchor="w")

        self.lbl_opening = Label(self.tl_add,
                                text="Entrer le chemin d'accès du fichier ou \
l'url du site internet",
                                bg=self.BG, fg=self.FG, anchor="w")
        # endregion: LABEL

        # region: PACK
        self.lbl_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)

        self.lbl_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        # endregion: PACK

        self.autocompletion_window_app(name_opening)
        self.tl_add.mainloop()

    def add_shortcuts(self, name_shortcuts, name_opening):
        list_shortcuts = list()
        for add_shortcuts in self.db.display_shortcuts():
            list_shortcuts.append(add_shortcuts[0])

        if name_shortcuts not in list_shortcuts:
            ls_value = (name_shortcuts, name_opening)
            self.db.add_shortcuts(ls_value)
            showinfo("Ajout", "Votre raccourci a bien été ajouté")
            self.tl_add.destroy()
        
        else:
            showerror("Erreur", "Ce raccourcis existe déjà")
            self.tl_add.destroy()

    def autocompletion_window_app(self, name_opening=False):
        try:
            if len(name_opening) >= 1:
                self.ent_opening.insert(INSERT, name_opening)
                self.ent_shortcuts.focus()

        except:
            self.ent_shortcuts.focus()
