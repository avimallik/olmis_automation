from flask import Blueprint, render_template, request, flash, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename
import os

bulk_register_update_bp = Blueprint('bulk_register_update', __name__, url_prefix='/bulk_register_update')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads/excel_files'
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bulk_register_update_bp.route('/', methods=['GET', 'POST'])
def bulk_register_update():
    if request.method == 'POST':
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
                        return redirect(url_for('bulk_register_update.bulk_register_update'))

                # Insert or Update the data into the database
                cur = mysql.connection.cursor()
                for _, row in data.iterrows():
                    # Debugging: Print the row to see the data before insertion
                    print(f"Processing row: {row.to_dict()}")

                    try:
                        # Check if the record already exists
                        cur.execute("""
                            SELECT id FROM tbl_laywer_register WHERE branch_code = %s AND area_code = %s
                        """, (row['branch_code'], row['area_code']))
                        existing_record = cur.fetchone()

                        if existing_record:
                            # If the record exists, update it
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
                                row['highest_education'], row['codice_fiscale'], 
                                row['document_branch_inward_no'], row['document_ho_inward_no'], row['type_of_application'], 
                                row['application_session'], existing_record[0]
                            ))
                        else:
                            # If the record doesn't exist, insert a new one
                            cur.execute("""
                            INSERT INTO tbl_laywer_register (
                                branch_name, branch_code, area_name, area_code, 
                                division_name, division_code, country, name_english, 
                                name_bangla, bar_council_passing_year, bar_council_certificate_no, year_permission_practice_high_court, 
                                year_permission_practice_appellate, bar_association_membership_no, member_of_bar_association, bar_at_law,
                                address_present_english, address_present_bangla, address_permanent_english, 
                                address_permanent_bangla, address_court_chamber_english, address_court_chamber_bangla,
                                address_personal_chamber_english, address_personal_chamber_bangla, email, mobile, 
                                nid, experiences, other_academic_qualifications, passport_no, passport_expiry_date, 
                                overseas_national_id, diploma_or_professional_degree, other_training, date_of_birth, 
                                highest_education, codice_fiscale, document_branch_inward_no, document_ho_inward_no, 
                                type_of_application, application_session
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            row['branch_name'], row['branch_code'], row['area_name'], row['area_code'], 
                            row['division_name'], row['division_code'], row['country'], row['name_english'], 
                            row['name_bangla'], row['bar_council_passing_year'], row['bar_council_certificate_no'], 
                            row['year_permission_practice_high_court'], row['year_permission_practice_appellate'], 
                            row['bar_association_membership_no'], row['member_of_bar_association'], row['bar_at_law'],
                            row['address_present_english'], row['address_present_bangla'], row['address_permanent_english'], 
                            row['address_permanent_bangla'], row['address_court_chamber_english'], row['address_court_chamber_bangla'],
                            row['address_personal_chamber_english'], row['address_personal_chamber_bangla'], row['email'], 
                            row['mobile'], row['nid'], row['experiences'], row['other_academic_qualifications'], 
                            row['passport_no'], row['passport_expiry_date'], row['overseas_national_id'], 
                            row['diploma_or_professional_degree'], row['other_training'], row['date_of_birth'], 
                            row['highest_education'], row['codice_fiscale'], 
                            row['document_branch_inward_no'], row['document_ho_inward_no'], row['type_of_application'], 
                            row['application_session']
                        ))

                    except Exception as e:
                        # Log the error for the problematic row
                        print(f"Error processing row {row.to_dict()}: {e}")
                        flash(f"Error processing row {row.to_dict()}: {e}", 'danger')

                mysql.connection.commit()
                cur.close()

                # Fetch the records from the database to display in the table
                cur = mysql.connection.cursor()
                cur.execute("SELECT branch_name, branch_code, area_name, area_code, division_name, division_code, country, name_english, name_bangla FROM tbl_laywer_register")
                records = cur.fetchall()
                cur.close()

                flash('Data successfully uploaded and registered (or updated)!', 'success')
                return render_template('bulk_register_update.html', records=records)

            except Exception as e:
                flash(f"Error processing the file: {e}", 'danger')

        else:
            flash('Invalid file format. Please upload an Excel file.', 'danger')

    else:
        # If it's a GET request, fetch the records to display in the table
        cur = mysql.connection.cursor()
        cur.execute("SELECT branch_name, branch_code, area_name, area_code, division_name, division_code, country, name_english, name_bangla FROM tbl_laywer_register")
        records = cur.fetchall()
        cur.close()

    return render_template('bulk_register_update.html', records=records)
