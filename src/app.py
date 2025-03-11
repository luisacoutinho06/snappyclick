import customtkinter as ctk
from tkinter import Menu
import config
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.docs_save import DocsSavesPage 
from pages.about import AboutPage 


ctk.set_appearance_mode(config.DEFAULT_THEME)
ctk.set_default_color_theme("dark-blue")

class SnappyClickApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_NAME)
        self.geometry('{}x{}'.format(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT))
        self.minsize(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT)

        # Menu bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        # Adding menu options
        self.menu_bar.add_command(label="Home", command=lambda: self.show_screen("home"))
        self.menu_bar.add_command(label="Docs", command=lambda: self.show_screen("docs_saves"))
        self.menu_bar.add_command(label="Settings", command=lambda: self.show_screen("config"))
        self.menu_bar.add_command(label="About", command=lambda: self.show_screen("about"))
        self.menu_bar.add_separator()
        self.menu_bar.add_command(label="Exit", command=self.quit)

        # Creating a container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # Creating a frame to swap as screens
        self.screen_frame = ctk.CTkFrame(self.container)
        self.screen_frame.pack(side="top", fill="both", expand=True)  # Ensuring this takes the remaining space

        # Dictionary to store the screens
        self.screens = {}

        # Initializing the Home Screen
        self.show_screen("home")
        
    def show_screen(self, screen_name):
        """ Switches between application screens. """
        for widget in self.screen_frame.winfo_children():
            widget.destroy()
        
        # Going to the new screen
        if screen_name == "home":
            self.screens[screen_name] = HomePage(self.screen_frame)
        elif screen_name == "docs_saves":
            self.screens[screen_name] = DocsSavesPage(self.screen_frame)
        elif screen_name == "config":
            self.screens[screen_name] = SettingsPage(self.screen_frame)
        elif screen_name == "about":
            self.screens[screen_name] = AboutPage(self.screen_frame)
        
        # Exibindo a nova tela
        self.screens[screen_name].pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = SnappyClickApp()
    app.mainloop()
