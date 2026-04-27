import tkinter as tk
from tkinter import ttk
import os


class TreeView3Level:

    def __init__(self, master):

        self.master = master

        # Treeview
        # self.tree = ttk.Treeview(master)
        self.tree = ttk.Treeview(master, show="tree")
        self.tree.pack(fill="both", expand=True)

        style = ttk.Style()

        style.configure("Treeview",
                        rowheight=32,
                        font=("Comic Sans MS", 16))

        # evento seleção
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.folder_walker()

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
                open=True
            )

            nodes[root] = node

            for d in dirs:
                nodes[os.path.join(root, d)] = node





    # Evento seleção
    def on_select(self, event):

        item = self.tree.focus()
        texto = self.tree.item(item, "values")[0]

        print("Selecionado:", texto)


# -----------------------------
# EXECUÇÃO
# -----------------------------
root = tk.Tk()
root.geometry("400x400")
root.title("TreeView 3 Níveis")

TreeView3Level(root)

root.mainloop()


# import os
#
# def listar_diretorios(raiz):
#
#     for root, dirs, files in os.walk(raiz):
#         print(root)
#         print(dirs)
#         print(files)
#         print('________________________________________')

        # for d in dirs:
        #     print("   Subdiretório:", d)

# path = r"C:\JM-Image Analyzer"
# print(list(os.walk(path)))
# listar_diretorios(r"C:\JM-Image Analyzer")