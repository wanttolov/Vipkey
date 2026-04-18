import sys
from PIL import Image, ImageEnhance, ImageOps

def create_color_icon(src_path, dest_path):
    img = Image.open(src_path).convert("RGBA")
    # Resize to have multiple layers for ICO
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    img.save(dest_path, format='ICO', sizes=sizes)

def create_mono_icon(src_path, dest_path, is_white):
    img = Image.open(src_path).convert("RGBA")
    
    # Extract alpha
    alpha = img.split()[-1]
    
    # Convert image to grayscale to preserve the 3D shading
    grayscale = img.convert("L")
    
    # Adjust contrast to make the 3D effect pop in monochrome
    enhancer = ImageEnhance.Contrast(grayscale)
    grayscale = enhancer.enhance(1.5)
    
    if is_white:
        # Dark mode taskbar uses white icons, so we want the base to be bright, and shadows slightly darker
        # We can map black->white and keep shading? Actually white mode should be mostly white.
        # But if it's 3D, we need some contrast.
        # A simple trick: map it to a scale of 0.5 to 1.0 (light gray to white)
        def map_white(x):
            return int(x * 0.5 + 127)
        colored = grayscale.point(map_white).convert("RGB")
    else:
        # Light mode taskbar uses black icons
        # Map to a scale of 0.0 to 0.5 (black to dark gray)
        def map_black(x):
            return int(x * 0.5)
        colored = grayscale.point(map_black).convert("RGB")
        
    # Re-apply alpha channel
    r, g, b = colored.split()
    final_img = Image.merge("RGBA", (r, g, b, alpha))
    
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    final_img.save(dest_path, format='ICO', sizes=sizes)

if __name__ == "__main__":
    e_src = r"C:\Users\x99\.gemini\antigravity\brain\3d321b4f-d34e-4704-8ed3-1cd15e63d5c7\notion_e_1776429637534.png"
    v_src = r"C:\Users\x99\.gemini\antigravity\brain\3d321b4f-d34e-4704-8ed3-1cd15e63d5c7\notion_v_1776429651270.png"
    
    res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources\status"
    main_res_dir = r"c:\Users\x99\Desktop\NexusKey-Main\src\app\resources"
    
    # 1. Main App Icon
    create_color_icon(v_src, f"{main_res_dir}\\icon.ico")
    
    # 2. Color Status Icons
    create_color_icon(e_src, f"{res_dir}\\StatusEng.ico")
    create_color_icon(v_src, f"{res_dir}\\StatusViet.ico")
    
    # 3. White Icons for Dark Mode Taskbar
    create_mono_icon(e_src, f"{res_dir}\\StatusEng10.ico", is_white=True)
    create_mono_icon(v_src, f"{res_dir}\\StatusViet10.ico", is_white=True)
    
    # 4. Black Icons for Light Mode Taskbar
    create_mono_icon(e_src, f"{res_dir}\\StatusEngBlack.ico", is_white=False)
    create_mono_icon(v_src, f"{res_dir}\\StatusVietBlack.ico", is_white=False)
    
    print("Done generating all 3D status icons and app icon.")
