import tkinter as tk
from tkinter import filedialog, messagebox 
from PIL import ImageTk, Image              
from extractor import extract_palette, get_dominant_colors, rgb_to_hex

class ColorExtractorGUI: 
    def __init__(self, root):
        self.root = root
        self.root.title("Chromatica - GUI Edition")
        self.root.geometry("600x500")
        self.root.configure(bg="#fff0f5") 

        
        self.label = tk.Label(root, text="Chromatica Color Extractor", 
                              font=("Arial", 18, "bold"), bg="#fff0f5", fg="#ff69b4")
        self.label.pack(pady=20)

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.open_file,
                                    bg="#ff69b4", fg="white", font=("Arial", 12, "bold"))
        self.upload_btn.pack(pady=10)

        
        self.result_frame = tk.Frame(root, bg="#fff0f5")
        self.result_frame.pack(pady=20)

    def open_file(self):
        
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        
        if file_path:
            try:
               
                pixels = extract_palette(file_path)
                top_colors = get_dominant_colors(pixels)
                
               
                for widget in self.result_frame.winfo_children():
                    widget.destroy()

                
                for color_tuple, count in top_colors:
                    hex_val = rgb_to_hex(color_tuple)
                    
                    
                    color_box = tk.Label(self.result_frame, bg=hex_val, width=10, height=5, relief="raised")
                    color_box.pack(side=tk.LEFT, padx=5)
                    
                    
                    hex_label = tk.Label(self.result_frame, text=hex_val, bg="#fff0f5", fg="#333")
                    hex_label.pack(side=tk.LEFT)

            except Exception as e:
                
                messagebox.showerror("Error", f"Could not process image: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorExtractorGUI(root)
    root.mainloop()