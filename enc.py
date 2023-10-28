import tkinter as tk

# Function to perform a simple encryption
def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + 1)  # Shifting each character by 1 ASCII value
    return encrypted_text

# Function to handle button click and encrypt the input
def encrypt_input():
    input_text = input_entry.get()
    encrypted_text = encrypt_text(input_text)
    output_label.config(text=encrypted_text)
    output_text.delete('1.0', tk.END)  # Clear the text box
    output_text.insert(tk.END, encrypted_text)  # Insert encrypted text into the text box

# Creating the main window
window = tk.Tk()
window.title("Encryption Generator")

# Creating GUI components
input_label = tk.Label(window, text="Enter text to encrypt:")
input_label.pack()

input_entry = tk.Entry(window, width=30)
input_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_input)
encrypt_button.pack()

output_label = tk.Label(window, text="Encrypted Text:")
output_label.pack()

output_text = tk.Text(window, height=1, width=30)
output_text.pack()

# Running the main loop
window.mainloop()
