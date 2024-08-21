import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
from PIL import Image
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()

        # GUI Elements
        self.label = tk.Label(root, text="Image to PDF Converter", font=("Arial", 16))
        self.label.pack(pady=10)

        self.upload_button = tk.Button(root, text="Select Images", command=self.upload_images)
        self.upload_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Enter Output PDF Name:")
        self.output_label.pack(pady=10)

        self.output_entry = tk.Entry(root, textvariable=self.output_pdf_name)
        self.output_entry.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=20)

    def upload_images(self):
        file_paths = filedialog.askopenfilenames(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_paths:
            self.image_paths.extend(file_paths)
            print(f"Selected files: {self.image_paths}")

    def convert_to_pdf(self):
        if not self.image_paths:
            print("No images selected!")
            return

        if not self.output_pdf_name.get():
            print("Output PDF name is required!")
            return

        output_pdf_path = self.output_pdf_name.get() + ".pdf"

        pdf = FPDF()
        for image_path in self.image_paths:
            image = Image.open(image_path)
            pdf.add_page()
            pdf.image(image_path, 10, 10, pdf.w - 20, pdf.h - 20)
        
        pdf.output(output_pdf_path)
        print(f"PDF saved as {output_pdf_path}")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()

        
    























