import numpy as np
from PIL import Image

def extract_palette(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((100, 100)) 
    pixel_data = np.array(img)
    pixels = pixel_data.reshape(-1, 3)
    return pixels

def get_dominant_colors(pixels, top_n=5):
    min_dist = 80 
    
    color_counts = {}
    for p in pixels:
        color = tuple(p)
        color_counts[color] = color_counts.get(color, 0) + 1

    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    
    palette = []
    for color, count in sorted_colors:
        if len(palette) >= top_n:
            break
            
        is_distinct = True
        for existing_color, _ in palette:
            r1, g1, b1 = int(color[0]), int(color[1]), int(color[2])
            r2, g2, b2 = int(existing_color[0]), int(existing_color[1]), int(existing_color[2])
            
            r_mean = (r1 + r2) / 2
            dr = r1 - r2
            dg = g1 - g2
            db = b1 - b2
            
            dist = np.sqrt((2 + r_mean/256)*dr**2 + 4*dg**2 + (2 + (255-r_mean)/256)*db**2)
            
            if dist < min_dist:
                is_distinct = False
                break
        
        if is_distinct:
            palette.append((color, count))
            
    return palette

def rgb_to_hex(rgb_tuple):
    return '#{:02x}{:02x}{:02x}'.format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]).upper()