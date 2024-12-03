# Import required libraries
import tkinter as tk                  # Main GUI library
import tkinter.ttk as ttk
from tkinter import filedialog        # For opening file dialog
from tkinter import messagebox        # For showing error messages
from base64 import b64decode
from base64 import b64encode          # For encoding files to base64
# pip install pyperclip
import pyperclip                      # For copying to clipboard
from image_encoder_icon import ICON_16
from image_encoder_icon import ICON_32


class ImageEncoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Base64 Encoder")
        self.root.geometry("425x250")
        small_icon = tk.PhotoImage(data=b64decode(ICON_16))
        large_icon = tk.PhotoImage(data=b64decode(ICON_32))
        self.root.iconphoto(False, large_icon, small_icon)
        self.create_widgets()

# ----------------------- CREATE WIDGETS --------------------------------- #
    def create_widgets(self):
        # Create and configure main frame
        self.main_frame = ttk.LabelFrame(
            self.root, text="Image to Base64 Encoder")
        self.main_frame.pack(expand=True, padx=20, pady=20, fill='both')

        # Create widgets
        self.label = ttk.Label(
            self.main_frame,
            text="Select an image file to convert to base64"
        )
        self.label.grid(row=0, column=0, columnspan=2,
                        sticky="W")

        self.select_button = ttk.Button(
            self.main_frame,
            text="Select Image File",
            command=self.select_file,
            width=20
        )
        self.select_button.grid(
            row=1, column=0, columnspan=2, sticky="W")

        self.filename_label = ttk.Label(
            self.main_frame,
            text="No file selected",
            wraplength=400  # Wrap text if it exceeds 400 pixels
        )
        self.filename_label.grid(
            row=2, column=0, columnspan=2, sticky="W")

        self.status_label = ttk.Label(
            self.main_frame,
            text="",
            wraplength=400
        )
        self.status_label.grid(
            row=3, column=0, columnspan=2, sticky="W")

        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=10, pady=10, ipadx=1, ipady=1)

        self.root.bind("<Return>", self.select_file)
        self.root.bind("<Escape>", self.quit_app)

# ------------------------- SELECT FILE ---------------------------------- #
    def select_file(self):
        """
        Opens a file dialog for selecting an image file.
        Called when the select button is clicked.
        """
        # Define the file types that can be selected
        filetypes = (
            # Common image formats
            ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),
            # Option to show all files
            ('All files', '*.*')
        )

        # Open the file dialog and get selected filename
        filename = filedialog.askopenfilename(
            title='Select an image file',
            filetypes=filetypes
        )

        # If a file was selected (user didn't cancel)
        if filename:
            # Update the label to show selected filename
            self.filename_label.config(text=filename)
            # Process the selected file
            self.encode_file(filename)

# ------------------------ ENCODE FILE ----------------------------------- #
    def encode_file(self, filename):
        """
        Reads the selected file and converts it to base64.

        Args:
            filename (str): Path to the selected file
        """
        try:
            # Open the file in binary mode
            with open(filename, "rb") as f:
                # Read file content and convert to base64
                encoded = b64encode(f.read()).decode("ascii")
                # Copy the encoded string to clipboard
                pyperclip.copy(encoded)
                # Update status label to show success
                self.status_label.config(
                    text="Base64 encoded content copied to clipboard!",
                )

        except Exception as e:
            # If any error occurs during the process
            # Show error message in a popup
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            # Update status label to show error
            self.status_label.config(
                text="Error occurred while processing the file.",
                fg="red"               # Set text color to red for error
            )

    def quit_app(self):
        """Close the application"""
        self.root.destroy()


def main():
    # Create the main window
    root = tk.Tk()
    # Create an instance of our application
    app = ImageEncoderApp(root)
    # Start the application's main loop
    root.mainloop()


if __name__ == "__main__":
    main()
