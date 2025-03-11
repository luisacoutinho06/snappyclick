import customtkinter as ctk
from tkinter import Menu
import config
from pages.home import HomePage
from pages.settings import SettingsPage
from pages.docs_save import DocsSavesPage 
from pages.about import AboutPage 
from configs.theme_manager import *

class SnappyClickApp(ctk.CTk):
    def __init__(app):
        super().__init__()
        app.title(config.APP_NAME)
        app.geometry('{}x{}'.format(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT))
        app.minsize(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT)

        # Menu bar
        app.menu_bar = Menu(app)
        app.config(menu=app.menu_bar)

        # Adding menu options
        app.menu_bar.add_command(label="Home", command=lambda: app.show_screen("home"))
        app.menu_bar.add_command(label="Docs", command=lambda: app.show_screen("docs_saves"))
        app.menu_bar.add_command(label="Settings", command=lambda: app.show_screen("config"))
        app.menu_bar.add_command(label="About", command=lambda: app.show_screen("about"))
               
        # Adding the 'Change Theme' submenu
        app.theme_menu = Menu(app.menu_bar, tearoff=0)
        app.menu_bar.add_cascade(label="Change Theme", menu=app.theme_menu)

        # Adding theme options
        app.theme_menu.add_command(label="System", command=lambda: app.set_theme("system"))
        app.theme_menu.add_command(label="Dark", command=lambda: app.set_theme("dark"))
        app.theme_menu.add_command(label="Light", command=lambda: app.set_theme("light"))

        app.menu_bar.add_separator()
        app.menu_bar.add_command(label="Exit", command=app.quit)
        
        # Creating a container
        app.container = ctk.CTkFrame(app)
        app.container.pack(fill="both", expand=True)
        
        # Creating a frame to swap as screens
        app.screen_frame = ctk.CTkFrame(app.container)
        app.screen_frame.pack(side="top", fill="both", expand=True)  # Ensuring this takes the remaining space

        # Dictionary to store the screens
        app.screens = {}

        # Initializing the Home Screen
        app.show_screen("home")
        load_theme(app)
        
    def show_screen(app, screen_name):
        """ Switches between application screens. """
        for widget in app.screen_frame.winfo_children():
            widget.destroy()
        
        # Going to the new screen
        if screen_name == "home":
            app.screens[screen_name] = HomePage(app.screen_frame)
        elif screen_name == "docs_saves":
            app.screens[screen_name] = DocsSavesPage(app.screen_frame)
        elif screen_name == "config":
            app.screens[screen_name] = SettingsPage(app.screen_frame)
        elif screen_name == "about":
            app.screens[screen_name] = AboutPage(app.screen_frame)
        
        app.screens[screen_name].pack(fill="both", expand=True)
    
    def set_theme(app, theme):
        """Sets the theme and saves the user's choice."""
        set_theme(theme)
        update_theme_menu(app.theme_menu, theme.capitalize())

if __name__ == "__main__":
    app = SnappyClickApp()
    app.mainloop()
