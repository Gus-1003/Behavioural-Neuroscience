import cv2
import os
import matplotlib.pyplot as plt

# Caminho do vídeo
video_path = "C:/Users/Lafise/Documents/orientando - Gustavo/Fadiga Cre/F3/videos_cortados/R4_Fadiga3_cortado.mp4"

# Frame que você quer extrair (por exemplo o frame 1000)
frame_number = 1000

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

# Ir até o frame desejado
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
ret, frame = cap.read()
if not ret:
    print("Não conseguiu ler o frame")
    exit()

# Converter de BGR para RGB para o Matplotlib
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Plotar com eixos para ver coordenadas
plt.figure(figsize=(10, 6))
plt.imshow(frame_rgb)
plt.title(f"Frame {frame_number}")
plt.xlabel("Eixo X (largura)")
plt.ylabel("Eixo Y (altura)")
plt.grid(False)  # você pode ativar se quiser
plt.show()

# Se quiser salvar o frame
cv2.imwrite("frame_exemplo.png", frame)

cap.release()