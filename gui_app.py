import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from extractor import extract_palette, get_dominant_colors, rgb_to_hex

class ColorExtractor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chromatica Professional")
        self.geometry("900x750")
        self.configure(bg="#F1F5F9")  

        
        self.header_frame = tk.Frame(self, bg="#F1F5F9")
        self.header_frame.pack(pady=(30, 10))

        self.title_label = tk.Label(self.header_frame, text="CHROMATICA", 
                                    font=("Segoe UI", 24, "bold"), 
                                    bg="#F1F5F9", fg="#0F172A")
        self.title_label.pack()

        self.desc_label = tk.Label(self.header_frame, text="Professional Color Palette Analysis", 
                                   font=("Segoe UI", 10), bg="#F1F5F9", fg="#64748B")
        self.desc_label.pack()

        
        self.preview_frame = tk.Frame(self, bg="#E2E8F0", width=400, height=250)
        self.preview_frame.pack_propagate(False) 
        self.preview_frame.pack(pady=20)
        
        self.image_label = tk.Label(self.preview_frame, text="No Image Selected", 
                                    bg="#E2E8F0", fg="#94A3B8", font=("Segoe UI", 9))
        self.image_label.pack(expand=True, fill="both")

        self.upload_btn = tk.Button(self, text="SELECT IMAGE", 
                                    command=self.process_image,
                                    font=("Segoe UI", 10, "bold"),
                                    bg="#0F172A", fg="white",
                                    activebackground="#334155", activeforeground="white",
                                    padx=40, pady=12, bd=0, cursor="hand2")
        self.upload_btn.pack(pady=10)

     
        # Container to hold the color cards
        self.results_container = tk.Frame(self, bg="#F1F5F9")
        self.results_container.pack(pady=30)

    def process_image(self):
        file_path = filedialog.askopenfilename(
           filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
        )
        if not file_path:
          return

        try:
          
           img = Image.open(file_path)
           img.thumbnail((380, 230)) 
           photo = ImageTk.PhotoImage(img)
           self.image_label.config(image=photo, text="")
           self.image_label.image = photo

        
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
        
        card = tk.Frame(self.results_container, bg="white", padx=15, pady=15,
                        highlightbackground="#CBD5E1", highlightthickness=1)
        card.grid(row=0, column=index, padx=12, pady=10)

    
        color_display = tk.Label(card, bg=hex_code, width=14, height=5, relief="flat")
        color_display.pack(pady=(0, 10))

        
        hex_label = tk.Label(card, text=hex_code.upper(), font=("Consolas", 12, "bold"), 
                             bg="white", fg="#1E293B")
        hex_label.pack()

        
        footer = tk.Label(card, text="PRIMARY" if index == 0 else f"ACCENT {index}", 
                          font=("Segoe UI", 7, "bold"), 
                          bg="white", fg="#94A3B8")
        footer.pack(pady=(2, 0))

if __name__ == "__main__":
    app = ColorExtractor()
    app.mainloop()