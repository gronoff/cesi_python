# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.search = tk.Button(self, text="Recherche", command=self.truc)
#         self.search.pack()
#         self.top = tk.Button(self, text="Top 10", command=self.truc)
#         self.top.pack()
#         self.favorite = tk.Button(self, text="Favoris", command=self.truc)
#         self.favorite.pack()
#         self.quit = tk.Button(self, text="Quitter", command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def truc(self):
#         print('truc')


import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Home(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Open Food Fact")
       label.pack(side="top", fill="both", expand=True)


class Search(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Recherche d'un aliment")
       label.pack(side="top", fill="both", expand=True)


class Top10(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Affichage des top 10")
       label.pack(side="top", fill="both", expand=True)


class Favorite(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Vos favoris")
       label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p = Home(self)
        p1 = Search(self)
        p2 = Top10(self)
        p3 = Favorite(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Recherche", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Top 10", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Favoris", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p.show()

        self.quit = tk.Button(self, text="Quitter", command=self.master.destroy)
        self.quit.pack(side="bottom")


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
