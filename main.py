from pathlib import Path

print("anisIA v0.1")

project_path = input("Ruta del proyecto: ")

project = Path(project_path)

extensions = [".py", ".js", ".jsx", ".ts", ".tsx"]
ignored_folders = [".git", "node_modules", "dist", "build", "__pycache__"]


def scan_repository(project):
    files = []

    for item in project.rglob("*"):
        if any(folder in item.parts for folder in ignored_folders):
            continue
        if item.is_file() and item.suffix in extensions:
            files.append(item)

    return files

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


if project.exists():
    print("✅ Proyecto encontrado")

    files = scan_repository(project)

    print(f"Archivos encontrados: {len(files)}")

    for file in files:
        print(f"📄 {file}")

    if files:
        first_file = files[0]

        print("\nLeyendo primer archivo:")
        print(first_file)

        content = read_file(first_file)

        print("\nContenido:")
        print(content)
else:
    print("❌ El proyecto no existe")
