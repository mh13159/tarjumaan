from flask import *
from flask import render_template
from flask import Flask
from flask import request
from flask_caching import Cache
import os
import zipfile
cache = Cache()

#import audiocheck as au
import audiocheck as au

import recogniser as r
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
app=Flask(__name__)

#path='C:\\Users\\Areeba Shamsi\\Desktop\\Flask\\static\\Files\\Audios'
#path1='C:\\Users\\Areeba Shamsi\\Desktop\\Flask\\static\\Files'
#path2='C:\\Users\\Areeba Shamsi\\Desktop\\Flask\\static'

path="D:\\Flask_20thjan\\static\\Files\\Audios"
path1="D:\\Flask_20thjan\\static\\Files\\Results"
path2="D:\\Flask_20thjan\\static\\Files"

app.config['UPLOAD_PATH']=path

@app.route("/")
def getstarted(methods=['POST','GET']):
    return render_template("backup_index1.html")

@app.route("/upload")
def upload():
    return render_template("backup_index1.html")

@app.route('/success', methods=['POST'])
def success():
    print("test")
    #id = request.form.get('submit')
    #print(id)
    #my_id = request.form.get("fileupload","")
    #print(my_id)
    uploaded_files = request.files.getlist("file[]")
    filenames = [] 
    i =1
    for file in uploaded_files:
        f = str(file)
        f= f[15:len(f)-19]
        os.mkdir(path+"\\"+str(i))
        file.save(os.path.join(app.config['UPLOAD_PATH']+"\\"+str(i), file.filename))
        filenames.append(file.filename)
        new_path = os.path.abspath(file.filename)
        i+=1
    #if request.form['fileupload'] == "upload":
     #   print("test1")
    return render_template("backup_index1.html") 

'''@app.route("/audiocheck", methods=['POST'])
def audiocheck():
    output = au.audioCheck(path)
    output = output[0]
    print(output)
    return render_template('backup_index1.html', prediction_text='audio quality is:'.format(output))
'''

@app.route("/audiocheck" ,methods=['POST','GET'])
def audiocheck():
    print("test2")
    #result = au.check('C:\\Users\\Areeba Shamsi\\Desktop\\Flask\\static\\Files\\Audios\\1\\04Faiz Ahmed Faiz - Nisar Main Teri Galiyon Kay Ae Watan By ARaziq Piracha_Male_44100_CLEAN4.flac')
    #result = au.audioCheck('C:\\Users\\Areeba Shamsi\\Desktop\\Flask\\static\\Files\\Audios\\1')
    d = path+"\\"+"1"
    result = au.audioCheck(d)
    print(result)
    return render_template("backup_index1.html",result = result[0])

@app.route("/convert", methods=['GET','POST'])
def convert():
    r.Recognizer(path,path1)
    return render_template("backup_index1.html")


@app.route('/download_all',methods=['GET'])
def download_all():
    zipf = zipfile.ZipFile('Result.zip','w', zipfile.ZIP_DEFLATED)
    for file in os.listdir(path2):
        if file.endswith(".doc"):
            zipf.write(path2+'//'+file)
    zipf.close()
    return send_file('Result.zip',
            mimetype = 'zip',
            attachment_filename= 'Result.zip',
            as_attachment = True)


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


def main():
    cache.init_app(app, config=your_cache_config)
    
    with app.app_context():
        cache.clear()
       
        
if __name__ == "__main__":
    app.run(debug=False)
    main()
