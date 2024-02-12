from flask import Flask, render_template, send_file
from picamera import PiCamera
import time

app = Flask(__name__)
camera = PiCamera()

@app.route('/')
def index():
    # Capturar una imagen con la cámara
    image_path = capture_image()
    
    # Renderizar la plantilla HTML con la imagen
    return render_template('index.html', image_path=image_path)

@app.route('/image')
def get_image():
    # Devolver la imagen capturada al navegador
    return send_file('static/captured_image.jpg', mimetype='image/jpeg')

def capture_image():
    # Nombre del archivo de la imagen capturada
    image_path = 'static/captured_image.jpg'
    
    # Capturar la imagen
    camera.start_preview()
    time.sleep(2)  # Esperar para que la cámara se estabilice
    camera.capture(image_path)
    camera.stop_preview()
    
    return image_path

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
