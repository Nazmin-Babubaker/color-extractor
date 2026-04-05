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


def get_dominant_colors(pixels, top_n=5):
    
    color_counts = {}

    for p in pixels:
        
        color = tuple(p)
        
        
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

   
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

    
    return sorted_colors[:top_n]


def rgb_to_hex(rgb_tuple):
    return '#{:02x}{:02x}{:02x}'.format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]).upper()

def main():
  pixels = extract_palette("image1.png")
  top_colors = get_dominant_colors(pixels)

  print("--- Dominant Colors (Hex) ---")
  for color, count in top_colors:
    print(f"{rgb_to_hex(color)} : appeared {count} times")


if __name__ == "__main__":
    main()