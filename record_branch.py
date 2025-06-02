from flask import Blueprint, render_template, request, redirect, url_for, flash

record_branch_bp = Blueprint('record_branch', __name__, url_prefix='/branch')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

# List and Add Branch
@record_branch_bp.route('/', methods=['GET', 'POST'])
def record_branch():
    cur = mysql.connection.cursor()
    # Get all divisions for dropdown
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()

    if request.method == 'POST':
        division_id = request.form['division_id']
        branch_name = request.form['branch_name']
        branch_code = request.form['branch_code']
        cur.execute(
            "INSERT INTO tbl_branch (division_id, branch_name, branch_code) VALUES (%s, %s, %s)",
            (division_id, branch_name, branch_code)
        )
        mysql.connection.commit()
        flash('Branch added successfully!', 'success')
        return redirect(url_for('record_branch.record_branch'))

    # Join branch and division tables for display
    cur.execute("""
        SELECT b.branch_id, b.branch_name, b.branch_code, d.division_name, d.division_code
        FROM tbl_branch b
        JOIN tbl_division d ON b.division_id = d.division_id
    """)
    branches = cur.fetchall()
    cur.close()
    return render_template('record_branch.html', branches=branches, divisions=divisions)

# Edit Branch
@record_branch_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_branch(id):
    cur = mysql.connection.cursor()
    # Get all divisions for dropdown
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()
    if request.method == 'POST':
        division_id = request.form['division_id']
        branch_name = request.form['branch_name']
        branch_code = request.form['branch_code']
        cur.execute(
            "UPDATE tbl_branch SET division_id=%s, branch_name=%s, branch_code=%s WHERE branch_id=%s",
            (division_id, branch_name, branch_code, id)
        )
        mysql.connection.commit()
        flash('Branch updated successfully!', 'success')
        return redirect(url_for('record_branch.record_branch'))
    # Get branch data
    cur.execute("SELECT branch_id, division_id, branch_name, branch_code FROM tbl_branch WHERE branch_id=%s", (id,))
    branch = cur.fetchone()
    cur.close()
    return render_template('edit_branch.html', branch=branch, divisions=divisions)

# Delete Branch
# @record_branch_bp.route('/delete/<int:id>', methods=['POST'])
# def delete_branch(id):
#     cur = mysql.connection.cursor()
#     # Check if this branch is referenced in tbl_area
#     cur.execute("SELECT COUNT(*) FROM tbl_area WHERE branch_id=%s", (id,))
#     in_use = cur.fetchone()[0]
#     if in_use > 0:
#         flash('Cannot delete branch: it is assigned to one or more areas.', 'danger')
#         cur.close()
#         return redirect(url_for('record_branch.record_branch'))
#     # If not in use, proceed to delete
#     cur.execute("DELETE FROM tbl_branch WHERE branch_id=%s", (id,))
#     mysql.connection.commit()
#     cur.close()
#     flash('Branch deleted successfully!', 'success')
#     return redirect(url_for('record_branch.record_branch'))

@record_branch_bp.route('/delete/<int:id>', methods=['POST'])
def delete_branch(id):
    cur = mysql.connection.cursor()
    # Get the names of areas that use this branch
    cur.execute("SELECT area_name FROM tbl_area WHERE branch_id=%s", (id,))
    blocking_areas = cur.fetchall()
    if blocking_areas:
        area_list = ', '.join([a[0] for a in blocking_areas])
        flash(f'Cannot delete branch. It is assigned to area(s): {area_list}', 'danger')
        cur.close()
        return redirect(url_for('record_branch.record_branch'))
    # If not in use, proceed to delete
    cur.execute("DELETE FROM tbl_branch WHERE branch_id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Branch deleted successfully!', 'success')
    return redirect(url_for('record_branch.record_branch'))


