import tkinter as tk

# Function to perform a simple decryption.
def decrypt_text(text):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - 1)  # Shifting each character back by 1 ASCII value.
    return decrypted_text

# Function to handle button click and decrypt the input.
def decrypt_input():
    encrypted_text = input_entry.get()
    decrypted_text = decrypt_text(encrypted_text)
    output_label.config(text=decrypted_text)
    output_text.delete('1.0', tk.END)  # Clear the text box.
    output_text.insert(tk.END, decrypted_text)  # Insert decrypted text into the text box.

# Creating the main window.
window = tk.Tk()
window.title("Decryption Generator")

# Creating GUI components.
input_label = tk.Label(window, text="Enter text to decrypt:")
input_label.pack()

input_entry = tk.Entry(window, width=30)
input_entry.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_input)
decrypt_button.pack()

output_label = tk.Label(window, text="Decrypted Text:")
output_label.pack()

output_text = tk.Text(window, height=1, width=30)
output_text.pack()

window.mainloop()
