import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from extractor import extract_palette, get_dominant_colors, rgb_to_hex


class ModernExtractorApp(tk.Tk):
    def __init__(self):
        super().__init__()

      
        self.title("Chromatica Professional")
        self.geometry("850x600")
        self.configure(bg="#BBE1F0")

       
        self.header_frame = tk.Frame(self, bg="#BBE1F0")
        self.header_frame.pack(pady=40)

        self.title_label = tk.Label(self.header_frame, text="CHROMATICA", 
                                    font=("Helvetica", 28, "bold"), 
                                    bg="#BBE1F0", fg="#0B2D72")
        self.title_label.pack()

        self.desc_label = tk.Label(self.header_frame, text="Image Color Analysis & Palette Generation", 
                                   font=("Helvetica", 10), bg="#BBE1F0", fg="#888")
        self.desc_label.pack()

        
        self.upload_btn = tk.Button(self, text="UPLOAD IMAGE", 
                                    command=self.process_image,
                                    font=("Helvetica", 10, "bold"),
                                    bg="#0AC4E0", fg="white",
                                    activebackground="#0B2D72", activeforeground="white",
                                    padx=30, pady=10, bd=0, cursor="hand2")
        self.upload_btn.pack(pady=10)

        
        self.results_container = tk.Frame(self, bg="#BBE1F0")
        self.results_container.pack(expand=True, fill="both", padx=50, pady=20)

    def process_image(self):
       
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        try:
        
            pixels = extract_palette(file_path)
            colors = get_dominant_colors(pixels)

            
            for widget in self.results_container.winfo_children():
                widget.destroy()

           
            for i, (color_tuple, count) in enumerate(colors):
                hex_code = rgb_to_hex(color_tuple)
                self.create_color_card(i, hex_code)

        except Exception as e:
            
            messagebox.showerror("Process Error", f"Failed to analyze image: {e}")

    def create_color_card(self, index, hex_code):
       
        card = tk.Frame(self.results_container, bg="white", padx=10, pady=15, 
                        highlightbackground="#E6E5E1", highlightthickness=2)
        card.grid(row=0, column=index, padx=10, sticky="nsew")

        # The Color Box
        color_display = tk.Label(card, bg=hex_code, width=12, height=6)
        color_display.pack(pady=(0, 10))

        
        hex_label = tk.Label(card, text=hex_code, font=("Courier", 11, "bold"), 
                             bg="white", fg="#333")
        hex_label.pack()

        
        copy_hint = tk.Label(card, text="Dominant Color", font=("Helvetica", 7), 
                             bg="white", fg="#AAA")
        copy_hint.pack()

if __name__ == "__main__":
    app = ModernExtractorApp()
    app.mainloop()