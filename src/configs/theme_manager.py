import json
import os
import winreg
import customtkinter as ctk
import styles
import config

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

def load_theme(self):
    """Load the saved theme in JSON."""
    theme = "system"  # Default to system if no choice has been made
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            settings = json.load(file)
            theme = settings.get("theme", "system")
    
    set_theme(theme)
    update_theme_menu(self.theme_menu, theme.capitalize())
def save_theme(theme):
    """Saves the chosen theme in JSON."""
    with open(CONFIG_FILE, "w") as file:
        json.dump({"theme": theme}, file)
        

def set_theme(theme):
    """Sets the theme and saves the user's choice."""
    ctk.set_appearance_mode(theme)
    
    if theme.lower() == "light":
        styles.TEXT_COLOR = "#000000"
    else:
        styles.TEXT_COLOR = "#ffffff"
    
    save_theme(theme)

def update_theme_menu(menu, selected_theme):
    """Updates the menu to show the selected option with a dot."""
    for i in range(menu.index("end") + 1):
        label = menu.entrycget(i, "label")
        if selected_theme.lower() in label.lower():  # Case insensitive check
            menu.entryconfig(i, label="• " + label.lstrip("• "))
        else:
            menu.entryconfig(i, label=label.lstrip("• "))

def get_windows_theme():
    """Check your Windows theme."""
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return "Light" if value == 1 else "Dark"
    except FileNotFoundError:
        return "Unknown"
