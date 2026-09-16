from pathlib import Path

print("anisIA v0.1")

project_path = input("Ruta del proyecto: ")

project = Path(project_path)

extensions = [".py", ".js", ".jsx", ".ts", ".tsx"]


def scan_repository(project):
    for item in project.rglob("*"):
        if item.is_dir():
            print(f"📁 {item}")
        elif item.is_file() and item.suffix in extensions:
            print(f"📄 {item}")


if project.exists():
    print("✅ Proyecto encontrado")

    print("\nContenido del proyecto:")

    scan_repository(project)
else:
    print("❌ El proyecto no existe")
