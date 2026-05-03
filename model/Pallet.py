import shutil

import customtkinter as ctk
import os
from tkinter import ttk, Menu

from model.MineSateliteMap import MiniSateliteMap
from model.utils import get_base_path

BASE_DIR = get_base_path()

from pathlib import Path

# Pasta Documents do utilizador
DOCUMENTS_DIR = Path.home() / "Documents"

# Pasta da aplicação
APP_DIR = DOCUMENTS_DIR / "JM-Image-Analyzer"
APP_DIR.mkdir(parents=True, exist_ok=True)

# Subpasta File Explore
FILE_EXPLORE_DIR = APP_DIR / "File Explore"
FILE_EXPLORE_DIR.mkdir(parents=True, exist_ok=True)


class Pallet:

    def __init__(self, master, on_folder_selected):

        self.on_folder_selected = on_folder_selected

        self.selected_item = None
        # self.dataSource = {}
        self.master = master
        self.nodes = {}
        # ________________________ Pallet Side ________________________

        self.palletFrame = ctk.CTkFrame(master)
        self.palletFrame.grid(row=0, column=0, sticky='nswe')

        # coluna única expansível
        self.palletFrame.columnconfigure(0, weight=1)

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
        self.tree = ttk.Treeview(self.palletFrame, show="tree")
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(30, 10))

        self.tree.bind("<Button-3>", self.on_select_node)

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
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="nswe", pady=(30, 10))

        self.folder_walker()

        self.miniMap = ctk.CTkFrame(self.palletFrame)
        self.miniMap.grid(row=2, column=0, sticky='nswe', padx=(10, 0), pady=(0, 10))

        self.mini_sateliteMap = MiniSateliteMap(self.miniMap)

    def getMiniMap(self):
        return self.mini_sateliteMap

    def folder_walker(self):

        path = FILE_EXPLORE_DIR

        # nodes = {path: ""}
        self.nodes[path] = ""

        for root, dirs, files in os.walk(path):

            root = Path(root)  # ⭐ CORREÇÃO CRÍTICA

            # parent = nodes[root]
            parent = self.nodes[root]

            node = self.tree.insert(
                parent,
                "end",
                text=f"📂 {root.name}",
                values=(str(root),),
                open=False,
            )

            # nodes[root] = node
            self.nodes[root] = node

            for d in dirs:
                full_path = root / d
                # nodes[full_path] = node
                self.nodes[full_path] = node

    def on_select_node(self, event):

        selected = self.tree.identify_row(event.y)

        if not selected:
            return

        path = self.tree.item(selected, "values")[0]

        # self.make_dir(Path(path))
        self.menu_pop_up(path, event)

    def menu_pop_up(self, path, event):

        menu = Menu(self.tree, tearoff=False, foreground="#38c20e", background="#141414")
        menu.add_command(
            label="📁 New File Folder",
            font=('Comic Sans MS', 12),
            command=lambda: self.make_dir(path)
        )
        menu.add_separator()
        menu.add_command(
            label="✏ Rename Folder",
            font=('Comic Sans MS', 12),
            command=lambda: self.rename_dir(path)
        )
        menu.add_separator()
        menu.add_command(
            label="❌ Delete Folder",
            font=('Comic Sans MS', 12),
            command=lambda: self.delete_dir(path)
        )

        menu.post(event.x_root, event.y_root)

    def make_dir(self, path):
        dialog = ctk.CTkInputDialog(text="Enter a name", title="New Folder", font=('Comic Sans MS', 14) )
        new_dir = Path(path) / dialog.get_input()
        try:
            new_dir.mkdir(exist_ok=False)
            print("Pasta criada:", new_dir)

        except FileExistsError:
            print("A pasta já existe.")
        self.refresh_node(path)

    def rename_dir(self, path):
        path = Path(path)
        dialog = ctk.CTkInputDialog(text="Enter a name", title="Rename Folder", font=('Comic Sans MS', 14))
        new_path = path.parent / dialog.get_input()
        path.rename(new_path)
        # atualizar pasta pai
        self.refresh_node(path.parent)

    def delete_dir(self, path):
        path = Path(path)
        parent = path.parent  # ⭐ guardar antes de apagar
        shutil.rmtree(path)

        # atualizar pasta pai
        self.refresh_node(parent)

    def refresh_node(self, path):

        path = Path(path)

        node = self.nodes.get(path)

        if not node:
            return

        # remover filhos antigos
        self.tree.delete(*self.tree.get_children(node))

        # recriar apenas conteúdo da pasta
        for item in path.iterdir():

            if not item.is_dir():
                continue

            child = self.tree.insert(
                node,
                "end",
                text=f"📂{item.name}",
                values=(str(item),),
                open=True
            )
            self.nodes[item] = child

    def on_click(self, event):

        item = self.tree.focus()
        if not item:
            return

        path = self.tree.item(item, "values")[0]

        if self.on_folder_selected:
            self.on_folder_selected(path)
