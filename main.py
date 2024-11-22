import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Resize the image to fit in the window
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        file_path_label.config(text=f"File: {file_path}")
        
        # Display some information in the text box
        output_text.delete("1.0", tk.END)  # Clear previous text
        output_text.insert(tk.END, f"Image uploaded successfully!\n")
        output_text.insert(tk.END, f"File Path: {file_path}\n")
        output_text.insert(tk.END, f"Image Size: {img.size}\n")
        output_text.insert(tk.END, f"Image Format: {img.format}\n")

# Initialize the main window
root = tk.Tk()
root.title("Image and Info Display GUI")
root.geometry("400x600")

# Upload image button
upload_button = ttk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Image display label
image_label = tk.Label(root)
image_label.pack(pady=10)

# File path label
file_path_label = tk.Label(root, text="No file selected", wraplength=300)
file_path_label.pack()

# Text box for output information
output_text = tk.Text(root, height=10, width=40, state=tk.NORMAL)
output_text.pack(pady=10)

# Run the main loop
root.mainloop()
