from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import url_for
import os
from register_route import register_bp, init_mysql
from record_division import record_division_bp, init_mysql as init_record_division_mysql
from record_branch import record_branch_bp, init_mysql as init_record_branch_mysql
from record_area import record_area_bp, init_mysql as init_record_area_mysql
from record_member_of_bar_association import record_member_of_bar_association_bp, init_mysql as init_member_of_bar_association_mysql
from record_application_type import record_application_type_bp, init_mysql as init_application_type_mysql
from record_register import record_register_bp, init_mysql as init_record_register_mysql
from olmis_admin import olmis_admin_bp, init_mysql as init_admin_mysql
from record_country import record_country_bp, init_mysql as init_country_mysql
from bulk_register import bulk_register_bp, init_mysql as init_bulk_mysql
from bulk_register_update import bulk_register_update_bp, init_mysql as init_bulk_update_mysql

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
init_application_type_mysql(mysql)
init_record_register_mysql(mysql)
init_admin_mysql(mysql)
init_country_mysql(mysql)
init_bulk_mysql(mysql)
init_bulk_update_mysql(mysql)

@app.route('/')
def home():
    return render_template('index.html')

# blueprints
app.register_blueprint(register_bp)
app.register_blueprint(record_division_bp)
app.register_blueprint(record_branch_bp)
app.register_blueprint(record_area_bp)
app.register_blueprint(record_member_of_bar_association_bp)
app.register_blueprint(record_application_type_bp)
app.register_blueprint(record_register_bp)
app.register_blueprint(olmis_admin_bp)
app.register_blueprint(record_country_bp)
app.register_blueprint(bulk_register_bp)
app.register_blueprint(bulk_register_update_bp)

if __name__ == "__main__":
    app.run(debug=True)
