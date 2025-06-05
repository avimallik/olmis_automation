from flask import Blueprint, render_template, request, redirect, url_for, flash

record_application_type_bp = Blueprint(
    'record_application_type', __name__, url_prefix='/application-type'
)

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

@record_application_type_bp.route('/', methods=['GET', 'POST'])
def record_application_type():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        application_type = request.form['application_type']
        status = request.form['status']
        cur.execute(
            "INSERT INTO tbl_type_of_application (application_type, status) VALUES (%s, %s)",
            (application_type, status)
        )
        mysql.connection.commit()
        flash('Application Type added successfully!', 'success')
        return redirect(url_for('record_application_type.record_application_type'))

    cur.execute("SELECT id, application_type, status FROM tbl_type_of_application")
    application_types = cur.fetchall()
    cur.close()
    return render_template(
        'record_application_type.html',
        application_types=application_types
    )

@record_application_type_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_application_type(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        application_type = request.form['application_type']
        status = request.form['status']
        cur.execute(
            "UPDATE tbl_type_of_application SET application_type=%s, status=%s WHERE id=%s",
            (application_type, status, id)
        )
        mysql.connection.commit()
        flash('Application Type updated successfully!', 'success')
        return redirect(url_for('record_application_type.record_application_type'))
    cur.execute("SELECT id, application_type, status FROM tbl_type_of_application WHERE id=%s", (id,))
    application_type = cur.fetchone()
    cur.close()
    return render_template(
        'edit_application_type.html',
        application_type=application_type
    )

@record_application_type_bp.route('/delete/<int:id>', methods=['POST'])
def delete_application_type(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_type_of_application WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Application Type deleted successfully!', 'success')
    return redirect(url_for('record_application_type.record_application_type'))
