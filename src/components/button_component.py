import customtkinter as ctk
import styles

class ButtonComponent(ctk.CTkButton):
    def __init__(self, master, text, color, command, **kwargs,):
        
        # Applying basic button styling using LABEL_STYLE
        button_style = {
            "fg_color": color,
            "font": (styles.FONT_FAMILY, styles.FONT_SIZE_BUTTON),
            "width": 200,  # Button width
            "height": 40,  # Button height
            "corner_radius": 10,  # Corner rounding
        }

        # Updating the button style with additional settings passed 
        button_style.update(kwargs);

        # Initializing the button with style and other settings
        super().__init__(master, text=text, command=command, **button_style);
