from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import url_for
import os
from register_route import register_bp, init_mysql
from record_division import record_division_bp, init_mysql as init_record_division_mysql

app = Flask(__name__)
app.secret_key = 'dev_1234567890'

# MySQL config - change as needed
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'olmis_db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

mysql = MySQL(app)

# Inject mysql into blueprint
init_mysql(mysql)
init_record_division_mysql(mysql)

@app.route('/')
def home():
    return render_template('index.html')

# Register blueprint
app.register_blueprint(register_bp)
app.register_blueprint(record_division_bp)

if __name__ == "__main__":
    app.run(debug=True)
