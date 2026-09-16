from pathlib import Path

print("anisIA v0.1")

project_path = input("Ruta del proyecto: ")

project = Path(project_path)

if project.exists():
    print("✅ Proyecto encontrado")

    print("\nContenido del proyecto:")

    for item in project.rglob("*"):
        if item.is_dir():
            print(f"📁 {item}")
        elif item.is_file():
            print(f"📄 {item}")
else:
    print("❌ El proyecto no existe")