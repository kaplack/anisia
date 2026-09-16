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

        files.append(item)

    return files



for file in files:
    print(f" {file}")

if project.exists():
    print("✅ Proyecto encontrado")

    files = scan_repository(project)

    print(f"Archivos encontrados: {len(files)}")

    for file in files:
        print(f"📄 {file}")
else:
    print("❌ El proyecto no existe")
