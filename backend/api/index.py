# emotion_detection_app.py
import cv2
from flask import Flask, render_template, Response, request, redirect
from emotion_detection import detect_emotion

app = Flask(__name__, template_folder='../templates')
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return redirect('/face_detection')

@app.route('/face_detection')
def face_detection():
    return render_template('face-detection.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_emotion(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global capture
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            capture = 1

    elif request.method == 'GET':
        return render_template('face-detection.html')
    return render_template('face-detection.html')

if __name__ == '__main__':
    app.run()

cv2.destroyAllWindows()
