from flask import Flask, render_template, Response, request, redirect
import tensorflow as tf
import cv2
import numpy as np
from keras.preprocessing import image
import webbrowser
import cv2
import numpy as np
from scipy import stats
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')
CORS(app)
camera = cv2.VideoCapture(0)
face_haar_cascade = cv2.CascadeClassifier('./Model/haarcascade_frontalface_default.xml')
model = tf.keras.models.load_model('./Model/model_csv.h5')
label_dict = {0 : 'Angry', 1 : 'Disgust', 2 : 'Fear', 3 : 'Happiness', 4 : 'Sad', 5 : 'Surprise', 6 : 'Neutral'}
global capture
capture=0
url = 'https://open.spotify.com/embed/playlist/'
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
playlist = ''
    
def gen_frames():
    global capture
    count = 0
    final_pred = []
    while True:
        success, frame = camera.read()
        cap_img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(cap_img_gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(255,255,255),2)
            count +=1
            roi_gray = cap_img_gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48,48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            predictions = model.predict(img_pixels)
            emotion_label = np.argmax(predictions)
            emotion_prediction = label_dict[emotion_label]
            cv2.putText(frame, emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)
            final_pred.append(emotion_prediction)
            if count>=30:
                break
            test_1 = np.array(final_pred)
            mode = stats.mode(test_1)
        if success: 
            if(capture):
                capture=0
                if mode[0][0] == 'Neutral':
                    playlist = '7EClwmhqu7mg4JvUI9z5DT?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                elif mode[0][0] == 'Happiness':
                    playlist = '0jrlHA5UmxRxJjoykf7qRY?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                elif mode[0][0] == 'Angry':
                    playlist = '28UR58KCCBD9MkJmEgKQ8A?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                elif mode[0][0] == 'Sad':
                    playlist = '41sfGuPPtIZHGPMyHN6y2G?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                elif mode[0][0] == 'Disgust':
                    playlist = '1wMXcdYQ3aAt1Lp9Xd4sst?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                elif mode[0][0] == 'Fear':
                    playlist = '4pUX3ojKN2OxXP7I4Lu9ij?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
                else:
                    playlist = '4o5SxWNsTNLOi9ahHeJF8A?utm_source=generator'
                    webbrowser.get(chrome_path).open(url+playlist)
            try:
                
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass

@app.route('/')
def index():
    return redirect('/face_detection')

@app.route('/face_detection')
def face_detection():
    return render_template('face-detection.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests',methods=['POST','GET'])
def tasks():
    global camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture=1
            
    elif request.method=='GET':
        return render_template('face-detection.html')
    return render_template('face-detection.html')


cv2.destroyAllWindows()