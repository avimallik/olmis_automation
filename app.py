from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import url_for
import os
from register_route import register_bp, init_mysql
from record_division import record_division_bp, init_mysql as init_record_division_mysql
from record_branch import record_branch_bp, init_mysql as init_record_branch_mysql
from record_area import record_area_bp, init_mysql as init_record_area_mysql
from record_member_of_bar_association import record_member_of_bar_association_bp, init_mysql as init_member_of_bar_association_mysql

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
init_record_branch_mysql(mysql)
init_record_area_mysql(mysql)
init_member_of_bar_association_mysql(mysql)

@app.route('/')
def home():
    return render_template('index.html')

# blueprints
app.register_blueprint(register_bp)
app.register_blueprint(record_division_bp)
app.register_blueprint(record_branch_bp)
app.register_blueprint(record_area_bp)
app.register_blueprint(record_member_of_bar_association_bp)

if __name__ == "__main__":
    app.run(debug=True)
