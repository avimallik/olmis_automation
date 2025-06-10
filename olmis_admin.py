from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import hashlib

olmis_admin_bp = Blueprint('olmis_admin', __name__, url_prefix='')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

@olmis_admin_bp.route('/olmisAdmin', methods=['GET', 'POST'])
def login():
    if 'admin_logged_in' in session and session['admin_logged_in']:
        return redirect(url_for('record_register.record_register'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        md5_password = hashlib.md5(password.encode()).hexdigest()

        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM tbl_admin WHERE username=%s AND password=%s", (username, md5_password))
        admin = cur.fetchone()
        cur.close()
        if admin:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect(url_for('record_register.record_register'))
        else:
            flash("Invalid username or password", "danger")
            return render_template('olmis_admin.html')
    return render_template('olmis_admin.html')

@olmis_admin_bp.route('/olmisLogout')
def logout():
    session.clear()
    return redirect(url_for('olmis_admin.login'))
