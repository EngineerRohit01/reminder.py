import tkinter as tk
from tkinter import messagebox
import time
import webbrowser

# Function to open GitHub in the default browser
def open_github():
    webbrowser.open("https://github.com")

# Function to handle the button clicks
def handle_response(response):
    if response == "yes":
        root.destroy()  # Close the popup
    else:
        root.destroy()
        time.sleep(1800)  # Wait for 30 minutes
        show_popup()  # Show the popup again

# Function to show the popup
def show_popup():
    global root
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Create a new top-level window for customization
    popup = tk.Toplevel()
    popup.title("🐱 Daily Check-in")
    popup.geometry("400x200")

    # Add the question label
    question_label = tk.Label(
        popup, 
        text="Did you write code today and make a commit on GitHub today? 🐱", 
        font=("Arial", 12), 
        wraplength=350
    )
    question_label.pack(pady=10)

    # Add the GitHub link with an arrow
    link_label = tk.Label(
        popup, 
        text="→ Go to GitHub", 
        fg="blue", 
        cursor="hand2", 
        font=("Arial", 10, "underline")
    )
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", lambda e: open_github())

    # Add Yes and No buttons
    yes_button = tk.Button(popup, text="Yes", command=lambda: handle_response("yes"))
    yes_button.pack(side="left", padx=50, pady=10)

    no_button = tk.Button(popup, text="No", command=lambda: handle_response("no"))
    no_button.pack(side="right", padx=50, pady=10)

    popup.mainloop()

# Main script execution
if __name__ == "__main__":
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
    show_popup()
