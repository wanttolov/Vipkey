import os, glob

for ext in ('**/*.cpp', '**/*.h', '**/*.js'):
    for f in glob.glob('src/' + ext, recursive=True):
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            new_content = content.replace('L"NexusKey', 'L"Vipkey')
            new_content = new_content.replace('"NexusKey', '"Vipkey')
            
            # Additional UI changes just in case
            new_content = new_content.replace('Nexuskey', 'Vipkey')
            
            if content != new_content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated {f}")
        except Exception as e:
            print(f"Skipping {f} due to {e}")
