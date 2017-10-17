import os
import rocksdb
import subprocess
from random import *
from flask import Flask, request, jsonify


app = Flask(__name__)

# Instantiate rocksdb
db = rocksdb.DB("script.db", rocksdb.Options(create_if_missing=True))
	
@app.route('/api/v1/scripts', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      
      #checks for the current row in DB to create a sequnece of keys
      num = db.get_property(b"rocksdb.estimate-num-keys")
      
      #increment keys to increment the sequence starting from 123456 
      keys = 123456 + int(num)
      keys = keys + 1
      
      #create a package structure on server to upload the file
      keys=str(keys)
      UPLOAD_FOLDER = './tmp/'
      UPLOAD_FOLDER = UPLOAD_FOLDER + keys + '/'
      os.makedirs(UPLOAD_FOLDER)
      app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
      
      #upload the file in the package structure
      filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
      f.save(filepath)
      
      #Save the path of file against the generated key
      db.put(bytes(keys, 'utf-8'),  bytes(filepath, 'utf-8'))
      
      #Create the JSON response and set status code
      response = jsonify(scriptid = keys)
      response.status_code = 201
      return response


@app.route('/api/v1/scripts/<id>')
def script(id):
   path = db.get(bytes(id, 'utf-8'))
   
   #Path recovered from db 
   path=path.decode("utf-8") 
   
   #file run as a subprocess
   p = subprocess.Popen(["python3.6", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   output, err = p.communicate()
   
   #output from subprocess
   outputstr=output.decode("utf-8") 
   outputstr = outputstr.rstrip('\n')
   
   #creating json response
   response = jsonify(outputstr)
   response.status_code = 200
   response.mimetype='application/json'
   return response

		
if __name__ == '__main__':
   app.run('0.0.0.0',5000)
