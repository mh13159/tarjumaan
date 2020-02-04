from flask import *
from flask_caching import Cache
import os
import zipfile
cache = Cache()

#import SingleFileTest as SFT
import recogniser as r
app=Flask(__name__)
n_path=""
path='C:\\Users\\Areeba Shamsi\\Anaconda3\\envs\\flask-app\\Lib\\site-packages\\spyder\\utils\\help\\static\\audios\\shairi'
path1='C:\\Users\\Areeba Shamsi\\Anaconda3\\envs\\flask-app\\Lib\\site-packages\\spyder\\utils\\help\\static\\audios'
app.config['UPLOAD_PATH']=path

@app.route("/")
def upload():
    return render_template("file_upload.html")

'''
#one file upload (working)
@app.route("/success",methods=["POST"])
def success():
    f=request.files['file']
    success.file_name=f.filename
    #filename = secure_filename(file.filename)
    new_path = os.path.abspath(success.file_name)
    print(new_path)
    f.save(success.file_name)
    return render_template("success.html",name=success.file_name)
'''

'''
#folder upload-for loop not working
@app.route("/success",methods=["POST"])
def success():
    new_path=" "
    uploaded_files = request.files.getlist("file[]")
    #print(uploaded_files)
    #print("1")
    for file in uploaded_files:
        print("1")
        #print(file.path)
        #filename = secure_filename(file.filename)
        success.file_name=file.filename
        file.save(success.file_name)
        new_path = os.path.abspath(success.file_name)
        print(new_path)
    return render_template("success.html")
'''

#multiple file upload
@app.route('/success', methods=['POST'])
def success():
    uploaded_files = request.files.getlist("file[]") #select files
    filenames = [] #files 
    for file in uploaded_files: #iterate over files 
        #print("1")
        #filename = secure_filename(file.filename)
        #file.save(file.filename) #file.filename gives the name of the files
        file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
        filenames.append(file.filename) #adding names of the files in the filenames list
        new_path = os.path.abspath(file.filename)
        n_path=os.path.split(new_path)[0] #this gives path without the filename 
    print(n_path) 
    return render_template('success.html', filenames=filenames) 

'''
#for single file conversion
@app.route("/convert")
def stt():
    SFT.speechtotext(success.file_name)
    return render_template("download.html")
'''
#multiple file convert method
@app.route("/convert")
def stt():
    #print("path",n_path)
    #print("1")
    #n_path='D:\\UrduDataset\\shairi'
    #r.Recognizer(n_path,n_path)
    r.Recognizer(path,path)
    return render_template("download.html")

#single file download method
@app.route("/download")
def download():
    filename=success.file_name.split(".")[0]+".doc"
    return send_file(filename,as_attachment=True,cache_timeout=0)

'''
#download multiple files as a zipped file
@app.route('/download_all')
def download_all():
    zipf = zipfile.ZipFile('Name.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk(path):
        for file in files:
            zipf.write('path//'+file)
    zipf.close()
    return send_file('Name.zip',
            mimetype = 'zip',
            attachment_filename= 'Name.zip',
            as_attachment = True)
'''

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


    

