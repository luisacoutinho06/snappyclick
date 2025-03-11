import customtkinter as ctk
import styles
from components.button_component import ButtonComponent

class SettingsPage(ctk.CTkFrame):
    # Inicializa a tela de configurações
    def __init__(self, parent):
        super().__init__(parent)
        
        label = ctk.CTkLabel(self, text="Settings", **styles.LABEL_TITLE_STYLE)
        
        # Método usado para adicionar o widget à interface
        label.pack(pady=20)  # Ajuste a distância conforme necessário
        
        # Aqui você pode adicionar mais widgets ou botões, se necessário
        # button = ButtonComponent(self, text="Cancelar", command=self.on_button_click, color="grey")
        # button.pack(pady=120)
    
    def go_to_settings(self):
        print("Abrindo a tela de configurações...")
        
    def on_button_click(self):
        print("Botão clicado!")
