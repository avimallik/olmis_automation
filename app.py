from flask import Flask, request, jsonify, render_template, flash, redirect, url_for


from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json

app = Flask(__name__)
app.secret_key = 'dev_1234567890'

# MySQL config - change user/password as needed
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'olmis_db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    cur = mysql.connection.cursor()

    # Fetch dropdown options
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()

    cur.execute("SELECT id, name_country FROM tbl_country")
    countries = cur.fetchall()

    cur.execute("SELECT id, name_member_of_bar_association FROM tbl_member_of_bar_association")
    bar_associations = cur.fetchall()

    if request.method == 'POST':
        form = request.form
        photo = request.files.get('photo_filename')
        photo_filename = None
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo_filename = datetime.now().strftime('%Y%m%d%H%M%S_') + filename
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

        # Get division, branch, area details by their IDs
        division_id = form.get('division')
        branch_id = form.get('branch')
        area_id = form.get('area')

        cur.execute("SELECT division_name, division_code FROM tbl_division WHERE division_id = %s", (division_id,))
        div = cur.fetchone() or ('', '')
        division_name, division_code = div

        cur.execute("SELECT branch_name, branch_code FROM tbl_branch WHERE branch_id = %s", (branch_id,))
        br = cur.fetchone() or ('', '')
        branch_name, branch_code = br

        cur.execute("SELECT area_name, area_code FROM tbl_area WHERE area_id = %s", (area_id,))
        ar = cur.fetchone() or ('', '')
        area_name, area_code = ar

        # Now insert all fields into tbl_laywer_register
        cur.execute("""
        INSERT INTO tbl_laywer_register (
            branch_name, branch_code, area_name, area_code, division_name, division_code,
            country, name_english, name_bangla, bar_council_passing_year, bar_council_certificate_no, year_permission_practice_high_court,
            year_permission_practice_appellate, bar_association_membership_no, member_of_bar_association, bar_at_law,
            address_present_english, address_present_bangla, address_permanent_english, address_permanent_bangla,
            address_court_chamber_english, address_court_chamber_bangla, address_personal_chamber_english, address_personal_chamber_bangla, 
            email, mobile, nid, experiences, other_academic_qualifications, passport_no, passport_expiry_date, overseas_national_id, 
            diploma_or_professional_degree, other_training, date_of_birth, highest_education, photo_filename,
            codice_fiscale, document_branch_inward_no, document_ho_inward_no, application_session
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            branch_name, branch_code, area_name, area_code, division_name, division_code, 
            form.get('country'),
            form.get('name_english'),
            form.get('name_bangla'),
            form.get('bar_council_passing_year'),
            form.get('bar_council_certificate_no'),
            form.get('year_permission_practice_high_court'),
            form.get('year_permission_practice_appellate'),
            form.get('bar_association_membership_no'),
            form.get('member_of_bar_association'),
            form.get('bar_at_law'), 
            form.get('address_present_english'),
            form.get('address_present_bangla'),
            form.get('address_permanent_english'),
            form.get('address_permanent_bangla'),
            form.get('address_court_chamber_english'),
            form.get('address_court_chamber_bangla'),
            form.get('address_personal_chamber_english'),
            form.get('address_personal_chamber_bangla'),
            form.get('email'),
            form.get('mobile'),
            form.get('nid'),
            form.get('experiences'),
            form.get('other_academic_qualifications'),
            form.get('passport_no'),
            form.get('passport_expiry_date'),
            form.get('overseas_national_id'),
            form.get('diploma_or_professional_degree'),
            form.get('other_training'),
            form.get('date_of_birth'),
            form.get('highest_education'),
            photo_filename,
            form.get('codice_fiscale'),
            form.get('document_branch_inward_no'),
            form.get('document_ho_inward_no'),
            form.get('application_session'),
        ))
        mysql.connection.commit()
        flash('Registration Successful!', 'success')
        return redirect('/register')

    cur.close()
    return render_template('register.html',
                           divisions=divisions,
                           countries=countries,
                           bar_associations=bar_associations)

# AJAX endpoints
@app.route('/get_branches/<int:division_id>')
def get_branches(division_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT branch_id, branch_name, branch_code FROM tbl_branch WHERE division_id=%s", (division_id,))
    data = [{"id": row[0], "name_code": f"{row[1]} ({row[2]})"} for row in cur.fetchall()]
    cur.close()
    return {"branches": data}

@app.route('/get_areas/<int:division_id>/<int:branch_id>')
def get_areas(division_id, branch_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT area_id, area_name, area_code FROM tbl_area WHERE division_id=%s AND branch_id=%s", (division_id, branch_id))
    data = [{"id": row[0], "name_code": f"{row[1]} ({row[2]})"} for row in cur.fetchall()]
    cur.close()
    return {"areas": data}

if __name__ == "__main__":
    app.run(debug=True)