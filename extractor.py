from PIL import Image 
import numpy as np
import sys  


def extract_palette(image_path):
    img = Image.open(image_path)
    
   
    img = img.resize((100, 100))
    
  
    img = img.convert('RGB')

    pixel_data = np.array(img)
    
 
    pixels = pixel_data.reshape(-1, 3)
    
    print(f"Total pixels to analyze: {len(pixels)}")
    return pixels

def main():
    print("Environment check: Success!")
    extract_palette("image1.png")
    

if __name__ == "__main__":
    main()