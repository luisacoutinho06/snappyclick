import customtkinter as ctk;
import config;
from components.menu_component import MenuComponent;
from pages.home import HomePage;
from pages.settings import SettingsPage
from pages.docs_save import DocsSavesPage 

ctk.set_appearance_mode(config.DEFAULT_THEME);
ctk.set_default_color_theme("dark-blue");

class SnappyClickApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_NAME);
        self.geometry('{}x{}'.format(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT));
        self.minsize(config.WINDOW_SIZE_WIDTH, config.WINDOW_SIZE_HEIGHT);

        # Creating a container
        self.container = ctk.CTkFrame(self);
        self.container.pack(fill="both", expand=True);
        
        # Creating the menu for the navigation
        self.menu = MenuComponent(self, self.show_screen);
        self.menu.pack(side="top", fill="x");
        
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
            widget.destroy();
        
        # Going to the new screen
        if screen_name == "home":
            self.screens[screen_name] = HomePage(self.screen_frame)
        elif screen_name == "docs_saves":
            self.screens[screen_name] = DocsSavesPage(self.screen_frame)
        elif screen_name == "config":
            self.screens[screen_name] = SettingsPage(self.screen_frame)
        
        # Exibindo a nova tela
        self.screens[screen_name].pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = SnappyClickApp();
    app.mainloop();
    