import customtkinter as ctk
from utils.FileProcessor import FileProcessor as fp

class App:
    def __init__(self):
        self.dataSource = {}

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
        self.loadImageBtn = ctk.CTkButton(self.main_frame,
                                          text='Load Images',
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
        self.dataSource = fp().load()

        if self.dataSource:
            for widget in self.scrollPane.winfo_children():
                widget.destroy()

            for item in self.dataSource.values():
                if item.get('file') is not None:
                    ctk.CTkLabel(
                        self.scrollPane,
                        text=f'➡{item.get('file')}',
                        font=('Comic Sans MS', 16),
                        anchor='w'
                    ).pack(fill='x', padx=8, pady=2)

            if self.dataSource:
                self.lab2.configure(text=f'Src: {self.dataSource[0].get('srcPath')}')
                self.lab3.configure(text=f'File Counter:  {len(self.dataSource)-1}')
                self.lab4.configure(text='Folder Size:')
                self.lab5.configure(text='Created At:')






    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()