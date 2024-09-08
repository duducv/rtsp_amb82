import cv2
import socket
import time

ssid = "Dominuz-fibra"
password = "dominuz2023"

CHANNEL = 0  
RTSP_URL = "rtsp://localhost:8554/mystream" 

def connect_wifi(ssid, password):
    print(f"Conectando à rede {ssid}...")o
    time.sleep(2)
    print(f"Conectado à rede {ssid} com sucesso.")

def start_rtsp_stream():
    cap = cv2.VideoCapture(CHANNEL)
    
    if not cap.isOpened():
        print("Não foi possível acessar a câmera.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  
    cap.set(cv2.CAP_PROP_FPS, 30) 

    print(f"Iniciando o streaming para {RTSP_URL}")

    gst_str = f"appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=2000 speed-preset=ultrafast ! rtph264pay ! udpsink host=127.0.0.1 port=5000"

    out = cv2.VideoWriter(gst_str, cv2.CAP_GSTREAMER, 0, 30, (1920, 1080), True)

    if not out.isOpened():
        print("Erro ao iniciar o pipeline GStreamer.")
        cap.release()
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar o frame.")
            break

        out.write(frame) 

        cv2.imshow("Streaming", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def print_info():
    ip = socket.gethostbyname(socket.gethostname())
    print("------------------------------")
    print("- Resumo do Streaming -")
    print("------------------------------")
    print(f"RTSP URL: rtsp://{ip}:8554/mystream")

if __name__ == "__main__":
    connect_wifi(ssid, password)
    start_rtsp_stream()
    print_info()
