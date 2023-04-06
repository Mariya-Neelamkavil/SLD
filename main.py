from flask import *
from public import public
from admin import admin
from teachers import teachers
from students import students
from kyc import kyc
import os

app=Flask(__name__)
file_path = os.path.abspath('filename.txt')
print(file_path)

app.secret_key="Hello"
app.config["CACHE_TYPE"] = "null"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(teachers)
app.register_blueprint(students)
app.register_blueprint(kyc)
@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory('D:/MCA/SLD/files', filename)
app.run(host='0.0.0.0',port=5010,debug=True)

