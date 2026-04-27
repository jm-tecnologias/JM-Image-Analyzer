
import customtkinter as ctk
import os
from tkinter import ttk


from model.MineSateliteMap import MiniSateliteMap


class Pallet:

    def __init__(self, master, on_folder_selected):

        self.on_folder_selected = on_folder_selected

        self.selected_item = None
        self.dataSource = {}
        self.master = master
        # ________________________ Pallet Side ________________________

        self.palletFrame = ctk.CTkFrame(master)
        self.palletFrame.grid(row=0, column=0, sticky='nswe')

        # coluna única expansível
        self.palletFrame.columnconfigure(0, weight=1)

        # ⭐ Header / Content /
        # self.palletFrame.rowconfigure(0, weight=0)  # title
        # self.palletFrame.rowconfigure(1, weight=1)  # scroll area

        self.palletFrame.rowconfigure(1, weight=1)
        self.palletFrame.columnconfigure(0, weight=1)

        # ---------- Title ----------
        self.titleLab = ctk.CTkLabel(
            self.palletFrame,
            text='Media File Explore',
            font=('Berlin Sans FB Demi', 32)
        )

        self.titleLab.grid(row=0, column=0, sticky='we', pady=(40, 10))

        # # ---------- ScrollPane for images ----------
        # self.scrollPane = ctk.CTkScrollableFrame(self.palletFrame, fg_color="#141414")
        # self.scrollPane.grid(row=1, column=0, sticky='nswe', pady=(26, 10), padx=20)

        self.tree = ttk.Treeview(self.palletFrame, show="tree")
        self.tree.grid(row=1, column=0, sticky="nsew", pady = (30, 10))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        rowheight=32,
                        font=("Comic Sans MS", 12),
                        background="#141414",
                        foreground="white",
                        fieldbackground="#141414",  # ⭐ fundo real da área
                        # foreground="white",
                        borderwidth=2,
                        bordercolor="#141414",
                        relief="flat"
                        )
        # ⭐ cor do item selecionado
        style.map(
            "Treeview",
            background=[("selected", "#38c20e")],  # fundo
            foreground=[("selected", "white")]  # texto
        )



        # evento seleção
        self.tree.bind("<<TreeviewSelect>>", self.on_click)

        style.configure(
            "Vertical.TScrollbar",
            # gripcount=0,
            background="#141414",
            darkcolor="#141414",
            lightcolor="#141414",
            troughcolor="#38c20e",
            bordercolor="#141414",
            arrowcolor="#38c20e",
            width=6
        )
        style.map(
            "Vertical.TScrollbar",
            background=[("active", "#141414")]
        )
        scrollbar = ttk.Scrollbar(
            self.palletFrame,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar",

        )
        # scrollbar = ttk.Scrollbar(self.palletFrame, orient="vertical", command=self.tree.yview, style="Scrollbar")
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.grid(row=1, column=1, sticky="nswe", pady=(30, 10))
        # self.tree.grid(row=1, column=0, sticky="nsew")



        # self.loadImagesDir()
        self.folder_walker()

        self.miniMap = ctk.CTkFrame(self.palletFrame)
        self.miniMap.grid(row=2, column=0, sticky='nswe', padx=(10, 0), pady=(0, 10))

        self.mini_sateliteMap = MiniSateliteMap(self.miniMap)

    def getMiniMap(self):
        return self.mini_sateliteMap

    def folder_walker(self):
        path = r"C:\JM-Image Analyzer"

        nodes = {path: ""}

        for root, dirs, files in os.walk(path):

            parent = nodes[root]

            is_last = len(dirs) == 0

            icon = "" if is_last else "📂"

            node = self.tree.insert(
                parent,
                "end",
                text=f"{icon} {os.path.basename(root)}",
                values=(root,),
                open=False
            )

            nodes[root] = node

            for d in dirs:
                full_path = os.path.join(root, d)
                nodes[full_path] = node

    def on_click(self, event):

        item = self.tree.focus()
        if not item:
            return

        path = self.tree.item(item, "values")[0]

        print("Selecionado:", path)

        if self.on_folder_selected:
            self.on_folder_selected(path)
