import customtkinter as ctk
import pyautogui
import keyboard
import threading
from components.button_component import ButtonComponent
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkInputDialog

class CoordinateTable(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=10)
        self.is_recording = False
        self.coordinates = []
        self.create_widgets()

    """ Building the front """
    def create_widgets(self):
        # Creating two buttons, one to record and one to delete everything
        buttonStart = ButtonComponent(self, text="Start record of coordinates", command=self.start_recording, color="green")
        buttonStop = ButtonComponent(self, text="Stop record of coordinates", command=self.stop_recording, color="red")
        
        buttonStart.pack(side='top', pady=10, padx=5)
        buttonStop.pack(side='top', pady=10, padx=5)
        
        # Create a frame for the table
        self.table_frame = ctk.CTkScrollableFrame(self, width=600, height=240)
        self.table_frame.pack(padx=10, pady=5)

        # Create the headers manually using CTkLabels
        self.create_headers()

        # Initialize a list to store the rows
        self.rows = []

    def create_headers(self):
        # Create the header row manually
        header_label_1 = ctk.CTkLabel(self.table_frame, text="Coordinate", width=160)
        header_label_1.grid(row=0, column=0, padx=1, pady=1)
        
        header_label_2 = ctk.CTkLabel(self.table_frame, text="Action", width=220)
        header_label_2.grid(row=0, column=1, padx=1, pady=1)
        
        header_label_3 = ctk.CTkLabel(self.table_frame, text="Edit", width=100)
        header_label_3.grid(row=0, column=2, padx=1, pady=1)
        
        header_label_4 = ctk.CTkLabel(self.table_frame, text="Delete", width=100)
        header_label_4.grid(row=0, column=3, padx=1, pady=1)

    def add_row(self, coord, row_num):
        edit_icon = "Edit" 
        delete_icon = "Delete"

        # Create labels for the coordinate value, and buttons for Edit and Delete
        coord_label = ctk.CTkLabel(self.table_frame, text=coord)
        coord_label.grid(row=row_num, column=0, padx=2, pady=2)
        
        actions = ["Select Action", "Click", "Click + Insert data"]
        action_menu = ctk.CTkOptionMenu(self.table_frame, values=actions, command=lambda action: self.handle_action(action, row_num))
        action_menu.grid(row=row_num, column=1, padx=2, pady=2)
        
        # Edit button
        edit_button = ctk.CTkButton(self.table_frame, text=edit_icon, command=lambda: self.edit_row(row_num), width=20, height=20, fg_color="#00A8FF")
        edit_button.grid(row=row_num, column=2, padx=2, pady=2)
        
        # Delete button
        delete_button = ctk.CTkButton(self.table_frame, text=delete_icon, command=lambda: self.delete_row(row_num), width=20, height=20, fg_color="red")
        delete_button.grid(row=row_num, column=3, padx=2, pady=2)

        # Store the row's widgets to re-use later
        self.rows.append((coord_label, action_menu, edit_button, delete_button))

    """ Functions of the buttons Edit and Delete """
    def edit_row(self, row_num):
        new_value = CTkInputDialog(text=f"Edit coordinate {self.coordinates[row_num-1]}:", title="Edit Coordinate").get_input()
        if new_value:
            self.coordinates[row_num-1] = new_value
            # Update the label of the corresponding row
            self.rows[row_num-1][0].configure(text=new_value)
            
    def delete_row(self, row_num):
        # Using CTkMessagebox to confirm deletion
        response = CTkMessagebox(title="Confirm Deletion", 
                                 message="Are you sure you want to delete this coordinate?", 
                                 icon="warning", 
                                 option_1="No", 
                                 option_2="Yes").get()

        if response == "Yes":
            # Delete the coordinate from the list
            del self.coordinates[row_num - 1]
            # Forget the row widgets from the grid
            for widget in self.rows[row_num-1]:
                widget.grid_forget()
            
            # Remove the row from the list
            self.rows.pop(row_num - 1)
            
            # Reorganize the rows to preserve order
            for i, (coord, row_widgets) in enumerate(zip(self.coordinates, self.rows), start=1):
                for widget in row_widgets:
                    widget.grid_forget()
                self.add_row(coord, i)

    """ Functions to record coordinates """
    def start_recording(self):
        self.is_recording = True
        self.coordinates = []  # Clear previous coordinates
        self.rows = []  # Clear the rows in the table
        print("Recording started. Press space to capture coordinates.")
        
        # Clear the table (important when restarting)
        for widget in self.table_frame.winfo_children():
            widget.grid_forget()

        # Recreate the headers and initialize the row storage
        self.create_headers()
        
        # Use a separate thread to capture coordinates
        threading.Thread(target=self.capture_coordinate, daemon=True).start()

    def stop_recording(self):
        self.is_recording = False
        print("Recording stopped.")
        
    def capture_coordinate(self):
        while self.is_recording:
            if keyboard.is_pressed('space') and self.is_recording:  # Check space key to capture coordinates
                cursor_x, cursor_y = pyautogui.position() 
                coord = f"{cursor_x}, {cursor_y}"
                self.coordinates.append(coord)
                print(f"Captured coordinate: {coord}")
                
                # Add the coordinate to the table
                self.add_row(coord, len(self.coordinates))
                
                # Scroll the table to the bottom using yview
                self.table_frame.yview_moveto(1)

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Coordinate Table")
    root.geometry("500x400")
    app = CoordinateTable(master=root)
    app.mainloop()
