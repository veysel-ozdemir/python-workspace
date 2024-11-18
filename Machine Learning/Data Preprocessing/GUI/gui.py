import tkinter as tk
from tkinter import filedialog, messagebox
from dataset_encoding_functions import encode_with_missing_values


class DatasetEncoderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dataset Encoder")
        self.geometry("800x400")
        self.center_window()

        # Upload Dataset Button
        self.upload_button = tk.Button(
            self, text="Upload Dataset", command=self.upload_dataset
        )
        self.upload_button.pack(pady=20)

        # Store the dataset and encoded dataset
        self.dataset = []
        self.target_variable = tk.StringVar()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get the window width and height
        window_width = 800
        window_height = 400

        # Calculate position x, y to center the window
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the window position
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    def upload_dataset(self):
        # Open file dialog to upload the dataset
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")]
        )

        if file_path:
            try:
                with open(file_path, "r") as file:
                    reader = file.readlines()
                    self.dataset = [row for row in reader]

                messagebox.showinfo("Success", "Dataset uploaded successfully!")

                # Show the target variable input field
                self.show_target_variable_input()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")

    def show_target_variable_input(self):
        # Target variable label and entry
        target_label = tk.Label(self, text="Enter Target Variable Name:")
        target_label.pack(pady=5)

        self.target_entry = tk.Entry(self, textvariable=self.target_variable)
        self.target_entry.pack(pady=5)

        # Show the "Encode Dataset" button
        self.show_encode_button()

    def show_encode_button(self):
        # Create and show the "Encode Dataset" button below the target variable input
        self.encode_button = tk.Button(
            self, text="Encode Dataset", command=self.encode_and_display_dataset
        )
        self.encode_button.pack(pady=10)

    def encode_and_display_dataset(self):
        # Check if the target variable field is empty
        if not self.target_variable.get().strip():
            messagebox.showerror("Input Error", "Target Variable Name cannot be empty.")
            return

        if self.dataset:
            # Encode the dataset using the provided function
            encoded_dataset = encode_with_missing_values(
                self.dataset, self.target_variable.get()
            )

            # Clear previous view and display the encoded dataset in a grid
            self.show_encoded_dataset(encoded_dataset)

    def show_encoded_dataset(self, encoded_dataset):
        # Remove previous grid if exists
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        # Create a frame to hold the grid
        frame = tk.Frame(self)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Display encoded dataset in a grid
        for i, row in enumerate(encoded_dataset):
            for j, value in enumerate(row):
                label = tk.Label(
                    frame, text=value, borderwidth=1, relief="solid", width=15
                )
                label.grid(row=i, column=j, padx=1, pady=1)


if __name__ == "__main__":
    app = DatasetEncoderApp()
    app.mainloop()
