## rpa-python-fill-out-form
  Implementação do RPA-Python em um formulário de quanto custa no site da Conube.
 
# Dependencias a instalar no pc:
  # Caso esteja no Ubuntu:
    - Instalar o openCV:
      1º sudo apt update
      2º sudo apt install libopencv-dev python3-opencv 
      3º Verificar que foi instalado corretamente com o comando:
        - python3 -c "import cv2; print(cv2.__version__)"
        - O output tem que ser "4.2.0" ou a versão instalada.
 
    - Criar arquivo simbólico do openCV:
      - 1º Rodar o comando: "sudo ln -s /usr/lib/jni/libopencv_java<versão>.so /usr/lib/libopencv_java.so"
      
    - Instalar Tesseract
      - 1º sudo apt-get install tesseract-ocr
      - 2º Para verificar que foi instalado corretamente utilizar o comando "tesseract -v".
    
    - Instalar o php:
      - 1º sudo apt-get install apache2 php
    
    - Instalar o chrome.
      

# Como rodar:
  - 1º Deixe a resolução no full hd.
  - 2º Instale no venv o RPA-Python com "pip install rpa".
  - 3º Rodar o "main.py" com "python3 main.py".
  
# Resultados:
  Será possível ver visualmente o robo funcionando mas no fim ele sempre vai liberar um png como resultado, o nome do arquivo é "results.png".

# Observações
  - Modo headless só funciona quando se utiliza apenas o DOM.
