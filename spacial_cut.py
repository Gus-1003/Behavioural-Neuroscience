import cv2
import os
import glob

session = "F3"

# Pastas
input_dir = f"C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/{session}/videos_cortados/*.mp4"
output_dir_horizon = f"C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/{session}/videos_horizontais/"
output_dir_verti = f"C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/{session}/videos_verticais/"

# Limites de corte
limite_video_horizon = 400
inicio_video_vert = 450

os.makedirs(output_dir_horizon, exist_ok=True)
os.makedirs(output_dir_verti, exist_ok=True)

# Itera sobre todos os vídeos na pasta
for video_path in glob.glob(input_dir):
    video_name = os.path.basename(video_path)
    print(f"Processando {video_name}...")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Erro ao abrir {video_name}")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Configura saídas
    output_h = os.path.join(output_dir_horizon, f"{video_name.replace('.mp4', '_h.mp4')}")
    output_v = os.path.join(output_dir_verti, f"{video_name.replace('.mp4', '_v.mp4')}")

    out_h = cv2.VideoWriter(output_h, fourcc, fps, (width, limite_video_horizon))
    out_v = cv2.VideoWriter(output_v, fourcc, fps, (width, height - inicio_video_vert))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Parte superior
        frame_h = frame[0:limite_video_horizon, :]
        # Parte inferior
        frame_v = frame[inicio_video_vert:height, :]

        out_h.write(frame_h)
        out_v.write(frame_v)

    cap.release()
    out_h.release()
    out_v.release()
    print(f"{video_name} dividido com sucesso!")

print("Todos os vídeos foram processados.")