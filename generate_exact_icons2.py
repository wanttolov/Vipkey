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
    v_light = r"c:\Users\x99\Desktop\NexusKey-Main\vietLogo.png"      # Light taskbar V
    v_dark = r"c:\Users\x99\Desktop\NexusKey-Main\icondark.png"         # Dark taskbar V
    e_light = r"c:\Users\x99\Desktop\NexusKey-Main\engLogo.png"       # Light taskbar E
    e_dark = r"c:\Users\x99\Desktop\NexusKey-Main\englogoDark.png"      # Dark taskbar E
    
    res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources\status"
    main_res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources"
    
    # 1. Main Program Icon
    create_ico(v_light, f"{main_res_dir}\\icon.ico")
    
    # 2. Light Mode Taskbar uses "Black" suffix (idi_viet_on_black)
    create_ico(v_light, f"{res_dir}\\StatusVietBlack.ico")
    create_ico(e_light, f"{res_dir}\\StatusEngBlack.ico")
    
    # 3. Dark Mode Taskbar uses "10" suffix (idi_viet_on_white)
    create_ico(v_dark, f"{res_dir}\\StatusViet10.ico")
    create_ico(e_dark, f"{res_dir}\\StatusEng10.ico")
    
    # 4. Fallbacks for standard "Color" requests
    create_ico(v_light, f"{res_dir}\\StatusViet.ico")
    create_ico(e_light, f"{res_dir}\\StatusEng.ico")
