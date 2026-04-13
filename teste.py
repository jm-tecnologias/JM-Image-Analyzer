import customtkinter as ctk
from model.SplashScreen import SplashScreen
from main import App

ctk.set_appearance_mode("dark")


class Main(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.withdraw()  # esconder janela principal

        # splash
        self.splash = SplashScreen(self)

        # simular carregamento
        self.after(2500, self.start_app)

    def start_app(self):
        self.splash.destroy()

        self.app = App()
        self.deiconify()  # mostrar app


if __name__ == "__main__":
    main = Main()
    main.mainloop()