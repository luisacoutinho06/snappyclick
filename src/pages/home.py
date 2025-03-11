import customtkinter as ctk;
import styles;
from components.buttonComponent import ButtonComponent;

class HomePage(ctk.CTkFrame):
    # Initializing the constructor
    # The parent argument represents the parent element where this frame will be inserted (for example, the main window).
    def __init__(self, parent):
        # super() calls the constructor of the parent class (CTkFrame). This ensures that HomePage correctly inherits all functionality from CTkFrame.
        super().__init__(parent)
        
        label = ctk.CTkLabel(self, text="Welcome to my app!", **styles.LABEL_TITLE_STYLE);
        #button = ButtonComponent(self, text="Cancelar", command=self.on_button_click, color="grey")
        
        # Method used to add the widget to the interface and define its positioning.
        label.pack(pady=20);
        #button.pack(pady=120)

    def go_to_settings(self):
        print("Opening settings screen...");    
        
    def on_button_click(self):
        print("Button clicked!")