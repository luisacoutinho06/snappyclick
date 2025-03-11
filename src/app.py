import customtkinter as ctk
import json
import os
from tkinter import Menu
import config
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.docs_save import DocsSavesPage 
from pages.about import AboutPage 

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config", "settings.json")
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
               
        # Adding the 'Change Theme' submenu
        self.theme_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Change Theme", menu=self.theme_menu)

        # Adding theme options
        self.theme_menu.add_command(label="System", command=lambda: self.set_theme("system"))
        self.theme_menu.add_command(label="Dark", command=lambda: self.set_theme("dark"))
        self.theme_menu.add_command(label="Light", command=lambda: self.set_theme("light"))

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
        self.load_theme()
        
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
        
        self.screens[screen_name].pack(fill="both", expand=True)

    def load_theme(self):
        """Loads the theme saved in JSON."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                settings = json.load(file)
                theme = settings.get("theme", "system")
        else:
            theme = "system"

        self.set_theme(theme)
        
    def save_theme(self, theme):
        """Saves the chosen theme in JSON."""
        with open(CONFIG_FILE, "w") as file:
            json.dump({"theme": theme}, file)

    def set_theme(self, theme):
        """Sets the theme and saves the user's choice."""
        ctk.set_appearance_mode(theme)
        self.update_theme_menu(theme.capitalize())
        self.save_theme(theme)

    def update_theme_menu(self, selected_theme):
        """Updates the menu to show the selected option with a dot."""
        for i in range(self.theme_menu.index("end") + 1):
            label = self.theme_menu.entrycget(i, "label")
            if selected_theme in label:
                self.theme_menu.entryconfig(i, label="• " + label.lstrip("• "))
            else:
                self.theme_menu.entryconfig(i, label=label.lstrip("• "))

if __name__ == "__main__":
    app = SnappyClickApp()
    app.mainloop()
