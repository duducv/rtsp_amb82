# rtsp_amb82

# **RTSP Video Streaming usando Python com OpenCV e GStreamer**

## **Descrição do Projeto**

Este projeto faz parte de uma atividade de extensão para a faculdade, focada no **desenvolvimento de uma câmera intraoral** utilizando a placa **Realtek AMB82** para transmissão de vídeo via **RTSP**. O objetivo é testar a viabilidade técnica da transmissão de vídeo em tempo real, que será usada para melhorar diagnósticos odontológicos, aumentar a conversão de orçamentos em tratamentos aprovados, e facilitar a documentação dos diagnósticos nas clínicas geridas pela **Dominuz**, uma holding com mais de 10 clínicas odontológicas e médicas.

Neste protótipo, usamos **Python**, **OpenCV**, e **GStreamer** para capturar e transmitir o vídeo em tempo real através de um servidor RTSP.

## **Objetivos do Projeto**

1. **Prototipar a câmera intraoral** utilizando a placa Realtek AMB82 para capturar e transmitir vídeo via RTSP.
2. **Melhorar a qualidade do diagnóstico odontológico** nas clínicas geridas pela Dominuz, utilizando a câmera intraoral para capturar imagens detalhadas em tempo real.
3. **Facilitar a conversão de orçamentos** em tratamentos, melhorando a clareza e precisão das imagens apresentadas aos pacientes.
4. **Documentar os diagnósticos odontológicos** de forma mais eficiente e clara, utilizando a câmera para registrar os casos clínicos.

## **Tecnologias Utilizadas**

- **Python 3.8+**
- **OpenCV** para captura de vídeo.
- **GStreamer** para transmissão RTSP.
- **Realtek AMB82** como plataforma de prototipagem de hardware (substituída por simulação no software).
- **Linux** como ambiente de desenvolvimento.

## **Pré-requisitos**

1. **Python** instalado (versão 3.8+).
2. **GStreamer** instalado no sistema. No Linux, você pode instalar com:
   ```bash
   sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
3. **OpenCV** para Python:
```bash
    pip install -r requirements.txt
4. **Execute**
   ```bash
    python rtsp_video_stream.py