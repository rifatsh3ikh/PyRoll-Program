import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.iconbitmap("logo.ico") 
root.geometry("500x400")
root.title("PyRoller")
root.geometry("400x400")

def roll():
    number = random.randint(1, 6)
    
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂", 
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    dice_label.configure(text=dice_faces[number])
    result_text.configure(text=f"You rolled {number}!")

dice_label = ctk.CTkLabel(root, text="🎲", font=("Arial", 120))
dice_label.pack(pady=40)

result_text = ctk.CTkLabel(root, text="Roll Now!", font=("Arial", 20))
result_text.pack(pady=10)

roll_button = ctk.CTkButton(root, text="Roll Dice", command=roll, 
                            corner_radius=10, hover_color="#246ab1")
roll_button.pack(pady=20)
root.mainloop()

