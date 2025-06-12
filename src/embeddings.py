import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from utils import cargar_manual, extraer_chunks, limpiar_texto

if __name__ == "__main__":
    # Cargar manual y generar chunks
    manual_data = cargar_manual("data/manual.json")
    chunks = extraer_chunks(manual_data)

    # Limpiar texto
    for chunk in chunks:
        chunk["texto"] = limpiar_texto(chunk["texto"])

    # Cargar modelo y generar embeddings
    model = SentenceTransformer('BAAI/bge-base-en-v1.5')
    texts = [c["texto"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings_np = np.array(embeddings).astype('float32')

    # Guardar embeddings
    np.save("embeddings/embeddings.npy", embeddings_np)

    # Crear índice FAISS
    dimension = embeddings_np.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_np)
    faiss.write_index(index, "embeddings/faiss_index.index")

    print("✅ Embeddings y FAISS index guardados")