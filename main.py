import customtkinter as ctk
from utils.FileProcessor import FileProcessor as fp
import tkinter.font as tkfont
from PIL import Image
import os


class App:
    def __init__(self):
        self.dataSource = {}
        self.selected_item = None

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        self.root = ctk.CTk()
        self.root.title('JM-Image Analyzer')

        # windows size
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f'{width}x{height}')

        # main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Column Configuration
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=4)
        self.main_frame.columnconfigure(2, weight=5)
        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=1)

        # Load Images Button
        # Icon para o botao
        self.icon_load = ctk.CTkImage(
            light_image=Image.open("assets/ico.png"),
            dark_image=Image.open("assets/ico2.png"),
            size=(64, 64)  # tamanho do ícone
        )
        self.loadImageBtn = ctk.CTkButton(self.main_frame,
                                          text='Load Images',
                                          image=self.icon_load,
                                          compound='right',
                                          font=('Berlin Sans FB Demi', 32),
                                          command=self.loadImageList
                                          )
        self.loadImageBtn.grid(row=0, columnspan=3, sticky='we', padx=600)


        # ________________________ Pallet Side ________________________

        self.palletFrame = ctk.CTkFrame(self.main_frame)
        self.palletFrame.grid(row=1, column=0, sticky='nswe', padx=2)

        # coluna única expansível
        self.palletFrame.columnconfigure(0, weight=1)

        # ⭐ Header / Content / Footer layout
        self.palletFrame.rowconfigure(0, weight=0)  # title
        self.palletFrame.rowconfigure(1, weight=1)  # scroll area
        self.palletFrame.rowconfigure(2, weight=0)  # details

        # ---------- Title ----------
        self.titleLab = ctk.CTkLabel(
            self.palletFrame,
            text='Image List',
            font=('Berlin Sans FB Demi', 32)
        )

        self.titleLab.grid(row=0, column=0, sticky='we', pady=10)

        # ---------- ScrollPane for images ----------
        self.scrollPane = ctk.CTkScrollableFrame(self.palletFrame)
        self.scrollPane.grid(row=1, column=0, sticky='nswe', padx=5, pady=1)

        # ---------- Folder Details ----------
        self.palletFolderDetails = ctk.CTkFrame(self.palletFrame)
        self.palletFolderDetails.grid(row=2, column=0, sticky='we', padx=5, pady=5)


        self.lab = ctk.CTkLabel(
            self.palletFolderDetails,
            text='Site Details',
            font=('Berlin Sans FB Demi', 24)
        )
        self.lab.pack(anchor='w', fill='x')

        self.lab2 = ctk.CTkLabel(
            self.palletFolderDetails,
            text='Src:',
            font=('Comic Sans MS', 12),
            # wraplength=210, # px
            anchor='w'
        )
        self.lab2.pack(anchor='w', fill='x')

        self.lab3 = ctk.CTkLabel(
            self.palletFolderDetails,
            text='File Counter:',
            font=('Comic Sans MS', 12),
            anchor='w'
        )
        self.lab3.pack(anchor='w', fill='x')

        self.lab4 = ctk.CTkLabel(
            self.palletFolderDetails,
            text='Folder Size:',
            font=('Comic Sans MS', 12),
            anchor='w'
        )
        self.lab4.pack(anchor='w', fill='x')

        self.lab5 = ctk.CTkLabel(
            self.palletFolderDetails,
            text='Created At:',
            font=('Comic Sans MS', 12),
            anchor='w'
        )
        self.lab5.pack(anchor='w', fill='x')





        # Center
        self.center_frame = ctk.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=1, sticky='nswe')

        # Right
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.grid(row=1, column=2, sticky='nswe', padx = 2)

    def loadImageList(self):
        fp_instance = fp()
        path = fp_instance.getPath()  # Pergunta a pasta primeiro
        if not path:
            return

        # Mostrar loader
        loader = ctk.CTkLabel(self.scrollPane, text="Loading...", font=('Berlin Sans FB Demi', 20))
        loader.pack(pady=20)

        progress = ctk.CTkProgressBar(self.scrollPane, width=200)
        progress.pack(pady=10)
        progress.set(0)

        self.root.update()  # Forçar redraw para mostrar o loader antes de processar

        # Limpar dados antigos
        self.dataSource = {}
        for widget in self.scrollPane.winfo_children():
            if widget not in (loader, progress):
                widget.destroy()

        valid_extensions = ('.jpg', '.jpeg', '.png')
        self.dataSource[0] = {'srcPath': path}

        files = [f for f in os.listdir(path) if f.lower().endswith(valid_extensions)]
        total_files = len(files)

        # Carregar cada arquivo com update do progress
        for idx, file in enumerate(files, start=1):
            full_path = os.path.join(path, file)
            self.dataSource[idx] = {'absolutePath': full_path, 'file': file}

            lab = ctk.CTkLabel(
                self.scrollPane,
                text=f"➡ {file}",
                font=('Comic Sans MS', 16),
                anchor='w'
            )
            lab.pack(fill='x', padx=8, pady=2)

            lab.bind(
                "<Button-1>",
                lambda e, widget=lab, data=self.dataSource[idx]: self.on_click(e, widget, data)
            )

            progress.set(idx / total_files)  # Atualiza barra de progresso
            self.root.update()  # Redesenha a interface

        # Atualizar detalhes da pasta
        max_width = 240
        text = self.ellipsis_path(self.lab2, path, max_width)
        self.lab2.configure(text=f"Src: {text}")
        self.lab3.configure(text=f'File Counter: {total_files}')
        self.lab4.configure(text=f'Folder Size: {((fp_instance.get_folder_size(path) / 1024) / 1024):.2f}MB')
        self.lab5.configure(text=f'Created At: {fp_instance.get_creation_date(path)}')

        # Remover loader
        loader.destroy()
        progress.destroy()

    def ellipsis_path(self, widget, text, max_width):
        font = tkfont.Font(font=widget.cget("font"))

        # se couber, retorna normal
        if font.measure(text) <= max_width:
            return text

        left = 0
        right = len(text)

        while left < right:
            left_part = text[:left]
            right_part = text[len(text) - right:]
            candidate = f"{left_part}...{right_part}"

            if font.measure(candidate) <= max_width:
                return candidate

            if left <= right:
                right -= 1
            else:
                left += 1

        return "..."



    def on_click(self, event, widget, data):

        # reset item anterior
        if self.selected_item and self.selected_item.winfo_exists():
            self.selected_item.configure(fg_color="transparent")

        # destacar novo
        widget.configure(fg_color="#1f6aa5")

        self.selected_item = widget

        print(f"Selecionaste: {data.get('file')}")





    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()