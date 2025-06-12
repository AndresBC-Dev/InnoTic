from utils import cargar_manual, extraer_chunks, limpiar_texto

if __name__ == "__main__":
    manual_data = cargar_manual('data/manual.json')
    chunks = extraer_chunks(manual_data)

    # Limpiar texto de los chunks
    for chunk in chunks:
        chunk["texto"] = limpiar_texto(chunk["texto"])

    # Mostrar algunos ejemplos
    for c in chunks[:3]:
        print("ID:", c["chunk_id"])
        print("Texto:", c["texto"][:200] + "...")  # Solo parte del texto
        print("Metadatos:", c["metadatos"])
        print("-" * 50)