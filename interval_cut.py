import cv2
import pandas as pd
import os

data = {
    "Ratos": ["R9_Fadiga3", "R9_Fadiga3", "R9_Fadiga3"],
    "Inicio": [1800, 6900, 20700],
    "Fim": [3600, 7860, 22500]
}

session = "F3"
rede = "verticais"

df = pd.DataFrame(data)

# Pasta onde estão os vídeos
input_dir = f"C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/{session}/videos_{rede}/"
output_dir = f"C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/janelas_treino_{rede}/"
os.makedirs(output_dir, exist_ok=True)

for i, row in df.iterrows():
    rato = row["Ratos"]
    start_frame = row["Inicio"]
    end_frame = row["Fim"]

    input_video = os.path.join(input_dir, f"{rato}.mp4")
    output_path = os.path.join(output_dir, f"{rato}_cortado_{i+1}.mp4")

    cap = cv2.VideoCapture(input_video)
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo {input_video}")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    total_frames = end_frame - start_frame + 1
    current_frame = 0

    while True:
        ret, frame = cap.read()
        if not ret or current_frame > end_frame:
            break

        if current_frame >= start_frame:
            out.write(frame)

            # Print de progresso a cada 5%
            progresso = ((current_frame - start_frame + 1) / total_frames) * 100
            if int(progresso) % 5 == 0:
                print(f"{rato} (corte {i+1}): {int(progresso)}% concluído", end='\r')

        current_frame += 1

    cap.release()
    out.release()
    print(f"{rato} (corte {i+1}) salvo em {output_path}")