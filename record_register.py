from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
import pandas as pd
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from flask import session, redirect, url_for

record_register_bp = Blueprint('record_register', __name__, url_prefix='/lawyer-registers')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads/excel_files'
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Display all registered lawyers
@record_register_bp.route('/', methods=['GET', 'POST'])
def record_register():
    if request.method == 'POST':
        # Handle file upload and data update logic
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            try:
                # Read the uploaded Excel file
                data = pd.read_excel(filepath)

                # Handle NaN values by replacing them with empty strings
                data = data.fillna("")

                # Remove extra spaces from column names
                data.columns = data.columns.str.strip()  # Ensure there are no spaces in column names

                # Print columns to check the names
                print(f"Columns in the uploaded file: {data.columns.tolist()}")

                # Only select the required columns for insertion (excluding photo_filename)
                required_columns = [
                    'branch_name', 'branch_code', 'area_name', 'area_code',
                    'division_name', 'division_code', 'country', 'name_english', 'name_bangla',
                    'bar_council_passing_year', 'bar_council_certificate_no', 'year_permission_practice_high_court', 
                    'year_permission_practice_appellate', 'bar_association_membership_no', 'member_of_bar_association',
                    'bar_at_law', 'address_present_english', 'address_present_bangla', 'address_permanent_english', 
                    'address_permanent_bangla', 'address_court_chamber_english', 'address_court_chamber_bangla',
                    'address_personal_chamber_english', 'address_personal_chamber_bangla', 'email', 'mobile', 
                    'nid', 'experiences', 'other_academic_qualifications', 'passport_no', 'passport_expiry_date', 
                    'overseas_national_id', 'diploma_or_professional_degree', 'other_training', 'date_of_birth', 
                    'highest_education', 'codice_fiscale', 'document_branch_inward_no', 'document_ho_inward_no', 
                    'type_of_application', 'application_session'
                ]
                
                # Check if all required columns exist in the file
                for col in required_columns:
                    if col not in data.columns:
                        flash(f"Missing required column: {col}", 'danger')
                        return redirect(url_for('record_register.record_register'))

                # Insert or Update the data into the database
                cur = mysql.connection.cursor()
                for _, row in data.iterrows():
                    try:
                        # Check if the record already exists based on branch_code and area_code
                        cur.execute("""
                            SELECT id FROM tbl_laywer_register WHERE branch_code = %s AND area_code = %s
                        """, (row['branch_code'], row['area_code']))
                        existing_record = cur.fetchone()

                        if existing_record:
                            # Update existing record
                            cur.execute("""
                            UPDATE tbl_laywer_register SET
                                branch_name = %s, area_name = %s, division_name = %s, division_code = %s,
                                country = %s, name_english = %s, name_bangla = %s, bar_council_passing_year = %s,
                                bar_council_certificate_no = %s, year_permission_practice_high_court = %s,
                                year_permission_practice_appellate = %s, bar_association_membership_no = %s,
                                member_of_bar_association = %s, bar_at_law = %s, address_present_english = %s,
                                address_present_bangla = %s, address_permanent_english = %s, address_permanent_bangla = %s,
                                address_court_chamber_english = %s, address_court_chamber_bangla = %s,
                                address_personal_chamber_english = %s, address_personal_chamber_bangla = %s,
                                email = %s, mobile = %s, nid = %s, experiences = %s, other_academic_qualifications = %s,
                                passport_no = %s, passport_expiry_date = %s, overseas_national_id = %s,
                                diploma_or_professional_degree = %s, other_training = %s, date_of_birth = %s,
                                highest_education = %s, codice_fiscale = %s, document_branch_inward_no = %s,
                                document_ho_inward_no = %s, type_of_application = %s, application_session = %s
                            WHERE id = %s
                        """, (
                            row['branch_name'], row['area_name'], row['division_name'], row['division_code'],
                            row['country'], row['name_english'], row['name_bangla'], row['bar_council_passing_year'],
                            row['bar_council_certificate_no'], row['year_permission_practice_high_court'],
                            row['year_permission_practice_appellate'], row['bar_association_membership_no'],
                            row['member_of_bar_association'], row['bar_at_law'], row['address_present_english'],
                            row['address_present_bangla'], row['address_permanent_english'], row['address_permanent_bangla'],
                            row['address_court_chamber_english'], row['address_court_chamber_bangla'],
                            row['address_personal_chamber_english'], row['address_personal_chamber_bangla'],
                            row['email'], row['mobile'], row['nid'], row['experiences'], row['other_academic_qualifications'],
                            row['passport_no'], row['passport_expiry_date'], row['overseas_national_id'],
                            row['diploma_or_professional_degree'], row['other_training'], row['date_of_birth'],
                            row['highest_education'], row['codice_fiscale'], row['document_branch_inward_no'],
                            row['document_ho_inward_no'], row['type_of_application'], row['application_session'],
                            existing_record[0]  # This is the id of the existing record that you want to update
                        ))

                        else:
                            # Insert new record if it doesn't exist
                            cur.execute("""
                                INSERT INTO tbl_laywer_register (
                                    branch_name, branch_code, area_name, area_code, division_name, division_code,
                                    country, name_english, name_bangla, bar_council_passing_year, bar_council_certificate_no,
                                    year_permission_practice_high_court, year_permission_practice_appellate,
                                    bar_association_membership_no, member_of_bar_association, bar_at_law,
                                    address_present_english, address_present_bangla, address_permanent_english,
                                    address_permanent_bangla, address_court_chamber_english, address_court_chamber_bangla,
                                    address_personal_chamber_english, address_personal_chamber_bangla, email, mobile,
                                    nid, experiences, other_academic_qualifications, passport_no, passport_expiry_date,
                                    overseas_national_id, diploma_or_professional_degree, other_training, date_of_birth,
                                    highest_education, codice_fiscale, document_branch_inward_no, document_ho_inward_no,
                                    type_of_application, application_session
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                        %s, %s, %s, %s, %s)
                            """, (
                                row['branch_name'], row['branch_code'], row['area_name'], row['area_code'],
                                row['division_name'], row['division_code'], row['country'], row['name_english'],
                                row['name_bangla'], row['bar_council_passing_year'], row['bar_council_certificate_no'],
                                row['year_permission_practice_high_court'], row['year_permission_practice_appellate'],
                                row['bar_association_membership_no'], row['member_of_bar_association'], row['bar_at_law'],
                                row['address_present_english'], row['address_present_bangla'], row['address_permanent_english'],
                                row['address_permanent_bangla'], row['address_court_chamber_english'], row['address_court_chamber_bangla'],
                                row['address_personal_chamber_english'], row['address_personal_chamber_bangla'],
                                row['email'], row['mobile'], row['nid'], row['experiences'], row['other_academic_qualifications'],
                                row['passport_no'], row['passport_expiry_date'], row['overseas_national_id'],
                                row['diploma_or_professional_degree'], row['other_training'], row['date_of_birth'],
                                row['highest_education'], row['codice_fiscale'], row['document_branch_inward_no'],
                                row['document_ho_inward_no'], row['type_of_application'], row['application_session']
                            ))


                    except Exception as e:
                        # Log the error for the problematic row
                        print(f"Error processing row {row.to_dict()}: {e}")
                        flash(f"Error processing row {row.to_dict()}: {e}", 'danger')

                mysql.connection.commit()
                cur.close()

                flash('Data successfully uploaded and registered (or updated)!', 'success')
                return redirect(url_for('record_register.record_register'))

            except Exception as e:
                flash(f"Error processing the file: {e}", 'danger')

        else:
            flash('Invalid file format. Please upload an Excel file.', 'danger')

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name_english, name_bangla, division_name, branch_name, area_name, mobile, email, photo_filename FROM tbl_laywer_register ORDER BY id DESC")
    registers = cur.fetchall()
    cur.close()

    return render_template('record_register.html', registers=registers)

# Edit a registered lawyer
@record_register_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_register(id):
    cur = mysql.connection.cursor()

    # Get all dropdown data
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()
    cur.execute("SELECT id, name_country FROM tbl_country")
    countries = cur.fetchall()
    cur.execute("SELECT id, name_member_of_bar_association FROM tbl_member_of_bar_association")
    bar_associations = cur.fetchall()
    cur.execute("SELECT id, application_type FROM tbl_type_of_application")
    application_types = cur.fetchall()

    # Fetch record to edit
    cur.execute("SELECT * FROM tbl_laywer_register WHERE id=%s", (id,))
    row = cur.fetchone()
    if not row:
        flash("Lawyer not found.", "danger")
        cur.close()
        return redirect(url_for('record_register.record_register'))

    columns = [col[0] for col in cur.description]
    lawyer = dict(zip(columns, row))

    # For dependent dropdowns: fetch available branches/areas
    # For dependent dropdowns: fetch available branches/areas
    cur.execute("SELECT branch_id, branch_name, branch_code FROM tbl_branch WHERE division_id=%s", (lawyer.get('division_id'),))
    branches = cur.fetchall()

    cur.execute("SELECT area_id, area_name, area_code FROM tbl_area WHERE division_id=%s", (lawyer.get('division_id'),))
    areas = cur.fetchall()


    if request.method == 'POST':
        form = request.form

        # IDs from form
        division_id = form.get('division')
        branch_id = form.get('branch')
        area_id = form.get('area')

        # Get names/codes for selected IDs
        cur.execute("SELECT division_name, division_code FROM tbl_division WHERE division_id = %s", (division_id,))
        div = cur.fetchone() or ('', '')
        division_name, division_code = div

        cur.execute("SELECT branch_name, branch_code FROM tbl_branch WHERE branch_id = %s", (branch_id,))
        br = cur.fetchone() or ('', '')
        branch_name, branch_code = br

        cur.execute("SELECT area_name, area_code FROM tbl_area WHERE area_id = %s", (area_id,))
        ar = cur.fetchone() or ('', '')
        area_name, area_code = ar

        # Handle photo update
        photo = request.files.get('photo_filename')
        photo_filename = lawyer.get('photo_filename')
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo_filename = datetime.now().strftime('%Y%m%d%H%M%S_') + filename
            photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], photo_filename))

        # Update query
        cur.execute("""
            UPDATE tbl_laywer_register SET
                division_name=%s, division_code=%s,
                branch_name=%s, branch_code=%s,
                area_name=%s, area_code=%s,
                country=%s, name_english=%s, name_bangla=%s,
                bar_council_passing_year=%s, bar_council_certificate_no=%s, year_permission_practice_high_court=%s,
                year_permission_practice_appellate=%s, bar_association_membership_no=%s, member_of_bar_association=%s, bar_at_law=%s,
                address_present_english=%s, address_present_bangla=%s, address_permanent_english=%s, address_permanent_bangla=%s,
                address_court_chamber_english=%s, address_court_chamber_bangla=%s, address_personal_chamber_english=%s, address_personal_chamber_bangla=%s,
                email=%s, mobile=%s, nid=%s, experiences=%s, other_academic_qualifications=%s,
                passport_no=%s, passport_expiry_date=%s, overseas_national_id=%s, diploma_or_professional_degree=%s,
                other_training=%s, date_of_birth=%s, highest_education=%s, photo_filename=%s,
                codice_fiscale=%s, document_branch_inward_no=%s, document_ho_inward_no=%s, type_of_application=%s, application_session=%s
            WHERE id=%s
        """, (
            division_name, division_code,
            branch_name, branch_code,
            area_name, area_code,
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
            form.get('type_of_application'),
            form.get('application_session'),
            id
        ))
        mysql.connection.commit()
        flash('Lawyer registration updated!', 'success')
        cur.close()
        return redirect(url_for('record_register.record_register'))  # Ensure this is correctly defined

    cur.close()
    return render_template('edit_register.html',
        lawyer=lawyer,
        divisions=divisions,
        countries=countries,
        bar_associations=bar_associations,
        application_types=application_types,
        branches=branches,
        areas=areas
    )


# Delete a registered lawyer
@record_register_bp.route('/delete/<int:id>', methods=['POST'])
def delete_register(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_laywer_register WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Lawyer registration deleted!', 'success')
    return redirect(url_for('record_register.record_register'))

from flask import jsonify

@record_register_bp.route('/get_areas/<int:division_id>')
def get_areas(division_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT area_id, area_name, area_code FROM tbl_area WHERE division_id = %s", (division_id,))
    areas = [{'id': row[0], 'name_code': f"{row[1]} ({row[2]})"} for row in cur.fetchall()]
    cur.close()
    return jsonify(areas)

@record_register_bp.route('/get_branches/<int:division_id>/<int:area_id>')
def get_branches(division_id, area_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT branch_id, branch_name, branch_code FROM tbl_branch WHERE division_id = %s AND area_id = %s", (division_id, area_id))
    branches = [{'id': row[0], 'name_code': f"{row[1]} ({row[2]})"} for row in cur.fetchall()]
    cur.close()
    return jsonify(branches)

@record_register_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('olmis_admin.login'))