# src/retriever.py

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Rutas fijas (ajusta si tu estructura cambia)
CHUNKS_PATH = "data/chunks.npy"        # Opcional, si guardas los chunks serializados
EMBEDDINGS_PATH = "embeddings/embeddings.npy"
INDEX_PATH = "embeddings/faiss_index.index"

# Cargar manual y chunks (si no están serializados)
from utils import cargar_manual, extraer_chunks
manual_data = cargar_manual("data/manual.json")
chunks = extraer_chunks(manual_data)

# Cargar modelo de embeddings
model = SentenceTransformer('BAAI/bge-base-en-v1.5')

# Cargar embeddings y FAISS index
embeddings_np = np.load(EMBEDDINGS_PATH)
index = faiss.read_index(INDEX_PATH)

def buscar_similares(pregunta, k=1):
    """
    Busca los artículos más similares a la pregunta.
    
    Args:
        pregunta (str): Pregunta del usuario.
        k (int): Número de resultados a devolver.
    
    Returns:
        List[Dict]: Lista con los artículos encontrados.
    """
    query_embedding = model.encode([pregunta]).astype('float32')
    distancias, indices = index.search(query_embedding, k)

    resultados = []
    for i in range(k):
        idx = indices[0][i]
        resultados.append({
            "chunk_id": chunks[idx]["chunk_id"],
            "texto": chunks[idx]["texto"],
            "metadatos": chunks[idx]["metadatos"],
            "distancia": float(distancias[0][i])
        })
    return resultados