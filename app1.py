from flask import *
from flask import render_template
from flask import Flask
from flask import send_file
from flask import request
from flask_caching import Cache
import os
import zipfile
cache = Cache()

import audiocheck as au
import recogniser as r

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
app=Flask(__name__)

path="F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\static\\Files\\Audios"
path1="F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\static\\Files\\Results"
path2="F:\\FinalSemester\\FYP_2_Deploymenty\\New folder\\project_updated_6thFeb\\static\\Files"

app.config['UPLOAD_PATH']=path

@app.route("/")
def getstarted(methods=['POST','GET']):
    return render_template("backup_index1.html")

@app.route("/upload")
def upload():
    return render_template("backup_index1.html")

@app.route('/success', methods=['POST'])
def success():
    uploaded_files = request.files.getlist("file[]")
    filenames = [] 
    i=1
    if ((len(os.listdir(path))>=1)):
        i= int(os.listdir(path)[len(os.listdir(path))-1])+1
    for file in uploaded_files:
        f = str(file)
        f= f[15:len(f)-19]
        os.mkdir(path+"\\"+str(i))
        file.save(os.path.join(app.config['UPLOAD_PATH']+"\\"+str(i), file.filename))
        filenames.append(file.filename)
        new_path = os.path.abspath(file.filename)
        i+=1
    return render_template("backup_index1.html") 

@app.route("/audiocheck" ,methods=['POST','GET'])
def audiocheck():
    i=1
    d = path+"\\"+str(i)
    if ((len(os.listdir(path))>1)):
        d = path+"\\"+str(int(os.listdir(path)[len(os.listdir(path))-1]))
    result = au.audioCheck(d)
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
