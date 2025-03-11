import customtkinter as ctk
import tkinter.messagebox as messagebox

class CoordinateTable(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.coordinate_label = ctk.CTkLabel(self, text="Coordenada", width=30, anchor="w")
        self.coordinate_label.grid(row=0, column=0)
        
        self.delete_label = ctk.CTkLabel(self, text="Deletar", width=10, anchor="w")
        self.delete_label.grid(row=0, column=1)
        
        coordinates = ["(10,20)", "(30,40)", "(50,60)"]
        for i, coord in enumerate(coordinates, start=1):
            self.add_row(coord, i)
            
    def add_row(self, coord, row_num):
        # Row for each coordinate
        coord_entry = ctk.CTkLabel(self, text=coord, width=30, anchor="w")
        coord_entry.grid(row=row_num, column=0)
        
        delete_button = ctk.CTkButton(self, text="Delete", command=lambda: self.delete_row(row_num))
        delete_button.grid(row=row_num, column=1)
        
    def delete_row(self, row_num):
        """ Handle row deletion"""
        response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this coordinate?")
        
        if response:
            for widget in self.grid_slaves(row=row_num):
                widget.destroy()
                
if __name__ == "__main__":
    root = ctk.CTk()
    app = CoordinateTable(master=root)
    app.mainloop()