import customtkinter as ctk;
import styles;

class MenuComponent(ctk.CTkFrame):
    def __init__(self, master, on_select_screen):
        """
        Side menu for navigation between screens.

        :param master: Main window or frame where the menu will be inserted.
        :param on_select_screen: Function to switch between screens.
        """
        super().__init__(master, width=200, corner_radius=0);
        self.on_select_screen = on_select_screen;
        
        self.create_menu_buttons();
        
    def create_menu_buttons(self):
        """ Creating button menu"""
        
        buttons = [
            ("🏠 Home", "home"),
            ("📂 Docs Saves", "docs_saves"),
            ("⚙️ Config", "config")
        ];
        
        for i, (text, screen_name) in enumerate(buttons):
            button = ctk.CTkButton(
                self,
                text=text,
                command=lambda name=screen_name: self.on_select_screen(name),
                text_color=styles.TEXT_COLOR,
                font= (styles.FONT_FAMILY, styles.FONT_SIZE_BUTTON),
                fg_color= "#3e3e3e",
                hover_color= "#4f4f4f"
            );
            button.grid(row=0, column=i, padx=10, pady=10, sticky="ew");

        # Make the columns flexible, i.e. to occupy the available space equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)