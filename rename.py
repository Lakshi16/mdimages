import os

folder = "book"

for f in os.listdir(folder):
    new = f.replace(" ", "_")
    if f != new:
        os.rename(os.path.join(folder, f), os.path.join(folder, new))
        print(f"{f} → {new}")
print("Done")