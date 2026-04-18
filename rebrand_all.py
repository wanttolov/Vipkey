"""
Comprehensive NexusKey -> Vipkey rebrand script.
Handles text content replacement in source files.
Does NOT rename actual filenames (like NexusKey.rc) since CMakeLists references them.
"""
import os
import re

ROOT = r"c:\Users\x99\Desktop\NexusKey-Main"

# Only process these directories (skip build/, extern/, .git/, node_modules/)
SCAN_DIRS = [
    os.path.join(ROOT, "src"),
    ROOT,  # for CMakeLists.txt and root files
]

# File extensions to process
EXTENSIONS = {
    '.cpp', '.h', '.js', '.css', '.html', '.rc', '.def', '.in',
    '.txt', '.manifest', '.json', '.md', '.toml',
}

# Files at root level to also process
ROOT_FILES = {'CMakeLists.txt', 'README.md', '.gitignore'}

# Replacements: order matters (longer/more specific first)
REPLACEMENTS = [
    # Comments and display strings
    (b'NexusKey', b'Vipkey'),
    (b'nexuskey', b'vipkey'),
    (b'NEXUSKEY', b'VIPKEY'),
    (b'Nexuskey', b'Vipkey'),
    (b'nexusKey', b'vipkey'),
]

def should_process(filepath):
    """Check if file should be processed."""
    # Skip build directory and .git
    rel = os.path.relpath(filepath, ROOT)
    parts = rel.split(os.sep)
    if any(p in ('build', 'extern', '.git', 'node_modules', '__pycache__') for p in parts):
        return False
    
    # Check extension
    _, ext = os.path.splitext(filepath)
    if ext.lower() in EXTENSIONS:
        return True
    
    # Check root files
    basename = os.path.basename(filepath)
    if basename in ROOT_FILES and os.path.dirname(filepath) == ROOT:
        return True
    
    return False

def process_file(filepath):
    """Replace NexusKey variants in file content."""
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
    except (IOError, PermissionError):
        return False
    
    original = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    
    if content != original:
        try:
            with open(filepath, 'wb') as f:
                f.write(content)
            return True
        except (IOError, PermissionError) as e:
            print(f"  ERROR writing {filepath}: {e}")
            return False
    return False

def main():
    changed_files = []
    scanned = 0
    
    for scan_dir in SCAN_DIRS:
        for dirpath, dirnames, filenames in os.walk(scan_dir):
            # Skip certain directories
            dirnames[:] = [d for d in dirnames if d not in ('build', 'extern', '.git', 'node_modules', '__pycache__')]
            
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if should_process(filepath):
                    scanned += 1
                    if process_file(filepath):
                        rel = os.path.relpath(filepath, ROOT)
                        changed_files.append(rel)
                        print(f"  CHANGED: {rel}")
    
    print(f"\n--- Summary ---")
    print(f"Scanned: {scanned} files")
    print(f"Changed: {len(changed_files)} files")
    
    if changed_files:
        print(f"\nModified files:")
        for f in sorted(changed_files):
            print(f"  {f}")

if __name__ == '__main__':
    main()
