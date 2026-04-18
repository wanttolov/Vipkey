import sys
import os
from PIL import Image

def create_ico(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return
    img = Image.open(src_path).convert("RGBA")
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    images = [img.resize(s, Image.Resampling.LANCZOS) for s in sizes[1:]]
    base_img = img.resize(sizes[0], Image.Resampling.LANCZOS)
    base_img.save(dest_path, format='ICO', sizes=sizes, append_images=images)
    print(f"Created {dest_path}")

if __name__ == "__main__":
    app_icon = r"c:\Users\x99\Desktop\NexusKey-Main\ICON APP.png"
    main_res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources"
    
    # 1. Main Program Icon
    create_ico(app_icon, f"{main_res_dir}\\icon.ico")
