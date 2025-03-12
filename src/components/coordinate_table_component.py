import customtkinter as ctk
import tkinter.messagebox as messagebox
from CTkMessagebox import CTkMessagebox

class CoordinateTable(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the table
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(padx=10, pady=10)

        # Coordinates data
        self.coordinates = ["(10,10)", "(20,20)", "(30,30)", "(40,40)", "(50,50)", "(60,60)", "(70,70)"]

        # Create the headers manually using CTkLabels
        self.create_headers()

        # Add rows
        for i, coord in enumerate(self.coordinates, start=1):
            self.add_row(coord, i)

    def create_headers(self):
        # Create the header row manually
        header_label_1 = ctk.CTkLabel(self.table_frame, text="Coordinate", width=20)
        header_label_1.grid(row=0, column=0, padx=2, pady=2)
        
        header_label_2 = ctk.CTkLabel(self.table_frame, text="Edit", width=5)
        header_label_2.grid(row=0, column=1, padx=2, pady=2)
        
        header_label_3 = ctk.CTkLabel(self.table_frame, text="Delete", width=5)
        header_label_3.grid(row=0, column=2, padx=2, pady=2)

    def add_row(self, coord, row_num):
        edit_icon = "Edit" 
        delete_icon = "Delete"

        # Create labels for the coordinate value, and buttons for Edit and Delete
        coord_label = ctk.CTkLabel(self.table_frame, text=coord)
        coord_label.grid(row=row_num, column=0, padx=2, pady=2)
        
        # Edit button with emoji
        edit_button = ctk.CTkButton(self.table_frame, text=edit_icon, command=lambda: self.edit_row(row_num), width=20, height=20, fg_color="green")
        edit_button.grid(row=row_num, column=1, padx=2, pady=2)
        
        # Delete button with emoji
        delete_button = ctk.CTkButton(self.table_frame, text=delete_icon, command=lambda: self.delete_row(row_num), width=20, height=20, fg_color="red")
        delete_button.grid(row=row_num, column=2, padx=2, pady=2)

    def edit_row(self, row_num):
        new_value = ctk.CTkInputDialog(text=f"Edit coordinate {self.coordinates[row_num-1]}:", title="Edit Coordinate").get_input()
        if new_value:
            self.coordinates[row_num-1] = new_value
            # Update the label of the corresponding row
            self.table_frame.grid_slaves(row=row_num, column=0)[0].configure(text=new_value)
            
    def delete_row(self, row_num):
        # Using CTkMessagebox to confirm deletion
        response = CTkMessagebox(title="Confirm Deletion", 
                                 message="Are you sure you want to delete this coordinate?", 
                                 icon="warning", 
                                 option_1="Cancel", 
                                 option_2="No", 
                                 option_3="Yes").get()

        if response == "Yes":
            # Delete the coordinate from the list
            del self.coordinates[row_num - 1]
            # Reorganize the remaining rows
            for widget in self.table_frame.grid_slaves():
                widget.grid_forget()  # Remove the widgets from the grid without destroying them
            
            # Add the remaining rows back to the table
            for i, coord in enumerate(self.coordinates, start=1):
                self.add_row(coord, i)
                
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Coordinate Table")
    root.geometry("500x400")
    app = CoordinateTable(master=root)
    app.mainloop()