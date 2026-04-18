import sys
from PIL import Image, ImageOps

def create_ico(img_rgba, dest_path):
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    images = []
    
    # Process 256x256 first
    base_img = img_rgba.resize(sizes[0], Image.Resampling.LANCZOS)
    
    for size in sizes[1:]:
        img_resized = img_rgba.resize(size, Image.Resampling.LANCZOS)
        images.append(img_resized)
        
    base_img.save(dest_path, format='ICO', sizes=sizes, append_images=images)


def invert_luminance(img_rgba):
    # Invert RGB but keep Alpha
    r, g, b, a = img_rgba.split()
    rgb = Image.merge('RGB', (r, g, b))
    inv_rgb = ImageOps.invert(rgb)
    r2, g2, b2 = inv_rgb.split()
    return Image.merge('RGBA', (r2, g2, b2, a))


if __name__ == "__main__":
    e_src = r"C:\Users\x99\.gemini\antigravity\brain\3d321b4f-d34e-4704-8ed3-1cd15e63d5c7\notion_e_1776429637534.png"
    v_src = r"C:\Users\x99\.gemini\antigravity\brain\3d321b4f-d34e-4704-8ed3-1cd15e63d5c7\notion_v_1776429651270.png"
    
    # Also load the notion_style_v one as a fallback check?
    style_v_src = r"C:\Users\x99\.gemini\antigravity\brain\3d321b4f-d34e-4704-8ed3-1cd15e63d5c7\notion_style_v_1776429585780.png"
    
    res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources\status"
    main_res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources"
    
    img_e = Image.open(e_src).convert("RGBA")
    img_v = Image.open(v_src).convert("RGBA")
    
    # Check if the user really meant `notion_style_v` instead of `notion_v`?
    # I'll use notion_v as assumed.
    
    # 1. Main App Icon
    create_ico(img_v, f"{main_res_dir}\\icon.ico")
    
    # 2. Color Status Icons
    create_ico(img_e, f"{res_dir}\\StatusEng.ico")
    create_ico(img_v, f"{res_dir}\\StatusViet.ico")
    
    # 3. White Icons for Dark Mode Taskbar (Usually the standard Notion logo looks great on dark)
    create_ico(img_e, f"{res_dir}\\StatusEng10.ico")
    create_ico(img_v, f"{res_dir}\\StatusViet10.ico")
    
    # 4. Black Icons for Light Mode Taskbar
    # If the original has a black border and white face, it might blend with a white taskbar
    # So we invert it for light mode!
    img_e_inv = invert_luminance(img_e)
    img_v_inv = invert_luminance(img_v)
    
    create_ico(img_e_inv, f"{res_dir}\\StatusEngBlack.ico")
    create_ico(img_v_inv, f"{res_dir}\\StatusVietBlack.ico")
    
    print("Done generating properly anti-aliased 3D icons.")
