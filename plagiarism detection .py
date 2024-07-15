import tkinter as tk  
from tkinter import filedialog  
from difflib import SequenceMatcher  

def open_file(text_area):  
    """Opens a file dialog to select a file and displays its content in the specified text area."""  
    global file_content  
    filepath = filedialog.askopenfilename(  
        defaultextension=".txt",  
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]  
    )  
    if filepath:  
        with open(filepath, "r") as file:  
            file_content = file.read()  
        text_area.delete("1.0", tk.END)  
        text_area.insert(tk.END, file_content)  

def compare_files():  
    """Compares the content of two files and displays the plagiarism percentage."""  
    file_content1 = text_area1.get("1.0", tk.END).strip()  
    file_content2 = text_area2.get("1.0", tk.END).strip()  

    if file_content1 and file_content2:  
        similarity_ratio = SequenceMatcher(None, file_content1, file_content2).ratio()  
        plagiarism_percentage = int(similarity_ratio * 100)  
        result_label.config(text=f"Plagiarism: {plagiarism_percentage}%", fg="red")  
    else:  
        result_label.config(text="Please select two files to compare.")  

# Create the main window  
window = tk.Tk()  
window.title("Plagiarism Detector")  

# Set background color for the window  
window.configure(bg="lightblue")  

# Create labels and text areas for file selection and content display  
label1 = tk.Label(window, text="File 1:", bg="lightblue", fg="black")  
label1.grid(row=0, column=0, padx=5, pady=5)  

text_area1 = tk.Text(window, height=10, width=50, bg="white", fg="black")  
text_area1.grid(row=1, column=0, padx=5, pady=5)  

button1 = tk.Button(window, text="Open File 1", command=lambda: open_file(text_area1), bg="blue", fg="white")  
button1.grid(row=2, column=0, padx=5, pady=5)  

label2 = tk.Label(window, text="File 2:", bg="lightblue", fg="black")  
label2.grid(row=0, column=1, padx=5, pady=5)  

text_area2 = tk.Text(window, height=10, width=50, bg="white", fg="black")  
text_area2.grid(row=1, column=1, padx=5, pady=5)  

button2 = tk.Button(window, text="Open File 2", command=lambda: open_file(text_area2), bg="blue", fg="white")  
button2.grid(row=2, column=1, padx=5, pady=5)  

# Create a button to compare the files  
compare_button = tk.Button(window, text="Compare Files", command=compare_files, bg="green", fg="white")  
compare_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)  

# Create a label to display the plagiarism percentage  
result_label = tk.Label(window, text="", bg="lightblue")  
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)  

window.mainloop()
