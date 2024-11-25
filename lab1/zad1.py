import os

def counter(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"Liczba plików: {len(files)}")

def tree(directory, indent=0):
        print(" " * indent + f"└──{os.path.basename(directory)}")
        indent += 4  # Zwiększeie wcięcia

        entries = os.listdir(directory)
        for i, entry in enumerate(entries):
            path = os.path.join(directory, entry)
            if os.path.isdir(path): #jeśli to folder to "wchodzi do środka"
                tree(path, indent)
            else:
                prefix = "└──" if i == len(entries) - 1 else "├──"
                print(" " * indent + f"{prefix}{entry}")

path = "C:/Users/lukas/Downloads"
tree(path)
counter(path)
