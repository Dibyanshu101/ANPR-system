from flask import Flask, request, render_template
import os
import deploy 

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'media' in request.files:
            image = request.files['media']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        
        # elif 'video' in request.files:
        #     video = request.files['video']
        #     video.save(os.path.join(app.config['UPLOAD_FOLDER'], video.filename))
        
        # return render_template('display.html', image=image.filename)
        deploy.process(vid_path=os.path.join(app.config['UPLOAD_FOLDER'], image.filename),vid_out=os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4'))
        return render_template('index.html', image=image.filename)
        

if __name__ == '__main__':
    app.run(debug=True)
    
