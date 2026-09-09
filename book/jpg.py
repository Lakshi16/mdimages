from PIL import Image
from pathlib import Path

# Folder containing your images
input_folder = Path(r"C:\Users\Deepthi\Internship\mdimages\mdimages\book")

# New folder for converted JPGs
output_folder = input_folder / "jpg_images"
output_folder.mkdir(exist_ok=True)

print("\n--- Existing JPG images ---")

# Display existing JPG/JPEG files
existing_jpgs = []

for file in input_folder.iterdir():
    if file.is_file() and file.suffix.lower() in {".jpg", ".jpeg"}:
        existing_jpgs.append(file.name)
        print(file.name)

if not existing_jpgs:
    print("No existing JPG images found.")

print("\n--- Converting PNG images ---")

# Convert PNG files
for file in input_folder.iterdir():

    if file.is_file() and file.suffix.lower() == ".png":
        try:
            image = Image.open(file)
            image = image.convert("RGB")

            output_file = output_folder / f"{file.stem}.jpg"

            image.save(output_file, "JPEG", quality=95)

            print(f"Converted: {file.name} -> {output_file.name}")

        except Exception as e:
            print(f"Error converting {file.name}: {e}")

print("\nDone!")