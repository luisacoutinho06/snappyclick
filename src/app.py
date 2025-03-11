import customtkinter as ctk;
import config;
from pages.home import HomePage;

ctk.set_appearance_mode(config.DEFAULT_THEME);
ctk.set_default_color_theme("dark-blue");

class SnappyClickApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_NAME);
        self.geometry(config.WINDOW_SIZE);
        
        self.page = HomePage(self);
        self.page.pack(fill="both", expand=True)
        
if __name__ == "__main__":
    app = SnappyClickApp();
    app.mainloop();
    