# src/test_query.py

from retriever import buscar_similares

if __name__ == "__main__":
    pregunta = "¿Qué beneficios puedo tener por participar en concursos?"
    resultados = buscar_similares(pregunta)

    print("🔍 Resultados de búsqueda:")
    for i, res in enumerate(resultados):
        print(f"\nResultado {i+1}:")
        print("ID:", res["chunk_id"])
        print("Texto:", res["texto"])
        print("Metadatos:", res["metadatos"])
        print("Distancia:", res["distancia"])
        print("-" * 50)