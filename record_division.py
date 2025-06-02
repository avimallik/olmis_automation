from flask import Blueprint, render_template, request, redirect, url_for, flash

record_division_bp = Blueprint('record_division', __name__, url_prefix='/division')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

@record_division_bp.route('/', methods=['GET', 'POST'])
def record_division():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['division_name']
        code = request.form['division_code']
        cur.execute("INSERT INTO tbl_division (division_name, division_code) VALUES (%s, %s)", (name, code))
        mysql.connection.commit()
        flash('Division added successfully!', 'success')
        return redirect(url_for('record_division.record_division'))
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()
    cur.close()
    return render_template('record_division.html', divisions=divisions)

@record_division_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_division(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['division_name']
        code = request.form['division_code']
        cur.execute("UPDATE tbl_division SET division_name=%s, division_code=%s WHERE division_id=%s", (name, code, id))
        mysql.connection.commit()
        flash('Division updated successfully!', 'success')
        return redirect(url_for('record_division.record_division'))
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division WHERE division_id=%s", (id,))
    division = cur.fetchone()
    cur.close()
    return render_template('edit_division.html', division=division)

# @record_division_bp.route('/delete/<int:id>', methods=['POST'])
# def delete_division(id):
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM tbl_division WHERE division_id=%s", (id,))
#     mysql.connection.commit()
#     cur.close()
#     flash('Division deleted successfully!', 'success')
#     return redirect(url_for('record_division.record_division'))

@record_division_bp.route('/delete/<int:id>', methods=['POST'])
def delete_division(id):
    cur = mysql.connection.cursor()
    # Check if any branches or areas use this division
    cur.execute("SELECT branch_name FROM tbl_branch WHERE division_id=%s", (id,))
    blocking_branches = cur.fetchall()
    cur.execute("SELECT area_name FROM tbl_area WHERE division_id=%s", (id,))
    blocking_areas = cur.fetchall()

    if blocking_branches or blocking_areas:
        msg = []
        if blocking_branches:
            branch_list = ', '.join([b[0] for b in blocking_branches])
            msg.append(f'Branches: {branch_list}')
        if blocking_areas:
            area_list = ', '.join([a[0] for a in blocking_areas])
            msg.append(f'Areas: {area_list}')
        flash(f'Cannot delete division. In use by {", ".join(msg)}', 'danger')
        cur.close()
        return redirect(url_for('record_division.record_division'))

    # Safe to delete
    cur.execute("DELETE FROM tbl_division WHERE division_id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Division deleted successfully!', 'success')
    return redirect(url_for('record_division.record_division'))

