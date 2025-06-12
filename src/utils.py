import json

def cargar_manual(ruta):
    
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def extraer_chunks(manual_data):
    chunks = []
    for capitulo in manual_data['manual']['capitulos']:
        for articulo in capitulo['articulos']:
            chunk = {
                "chunk_id": f"{articulo['metadatos']['capitulo']}_{articulo['numero']}",
                "texto": articulo['contenido'],
                "metadatos": {
                    "capitulo": articulo['metadatos']['capitulo'],
                    "articulo": articulo['numero'],
                    "tema_principal": articulo['metadatos']['tema_principal']
                }
            }
            chunks.append(chunk)
    return chunks

def limpiar_texto(texto):
    """Limpia espacios múltiples y recorta."""
    return ' '.join(texto.split())