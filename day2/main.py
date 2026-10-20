from pathlib import Path

folder = Path("test_folder")

if not folder.exists():
    folder.mkdir()
    print(f"Folder '{folder}' was created. Add some files and run again.")
else:
    for item in folder.iterdir():
        if item.is_file():
            print(f"{item.name} >> {item.suffix}")