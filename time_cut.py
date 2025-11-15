import cv2
import pandas as pd
import os

data = {
    "Ratos": ["R2_Fadiga3", "R3_Fadiga3", "R4_Fadiga3", "R5_Fadiga3", "R6_Fadiga3", "R7_Fadiga3", "R8_Fadiga3", "R9_Fadiga3"],
    "Inicio": [1909, 1577, 1203, 1147, 935, 1816, 1135, 7967],
    "Fim": [68206, 73854, 52585, 53325, 46863, 77695, 57493, 69931]
}

df = pd.DataFrame(data)

# Pasta onde estão os vídeos
input_dir = "C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/F3/"
output_dir = "C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/F3/videos_cortados/"
os.makedirs(output_dir, exist_ok=True)

for _, row in df.iterrows():
    rato = row["Ratos"]
    start_frame = row["Inicio"]
    end_frame = row["Fim"]

    input_video = os.path.join(input_dir, f"{rato}.mp4")
    output_path = os.path.join(output_dir, f"{rato}_cortado.mp4")

    cap = cv2.VideoCapture(input_video)
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo {input_video}")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)  # pega o FPS real do vídeo
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
                print(f"{rato}: {int(progresso)}% concluído", end='\r')

        current_frame += 1

    cap.release()
    out.release()
    print(f"{rato} cortado com sucesso!                     ")