import os
import shutil

def copiar_pdfs(input_dir: str, output_dir: str):
    
    # Garante que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Percorre todas as subpastas e arquivos da pasta de entrada
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.pdf'):  # Garante que é um PDF (case-insensitive)
                caminho_origem = os.path.join(root, file)
                caminho_destino = os.path.join(output_dir, file)

                # Se já existir um arquivo com o mesmo nome, cria uma cópia numerada
                base, ext = os.path.splitext(file)
                contador = 1
                while os.path.exists(caminho_destino):
                    novo_nome = f"{base}_{contador}{ext}"
                    caminho_destino = os.path.join(output_dir, novo_nome)
                    contador += 1

                shutil.copy2(caminho_origem, caminho_destino)
                print(f"Copiado: {caminho_origem} → {caminho_destino}")

    print("Cópia concluída!")
    
input_dir = "C:/Users/Lafise/Zotero/storage"
output_dir = "D:/Backup - Articles - Zotero"
copiar_pdfs(input_dir, output_dir)