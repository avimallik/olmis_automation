from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Define the blueprint for Branch
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

    # Get all areas for dropdown
    cur.execute("SELECT area_id, area_name, area_code FROM tbl_area")
    areas = cur.fetchall()

    search = request.args.get('search', '').strip()  # Get search value from query string

    if request.method == 'POST':
        division_id = request.form['division_id']
        area_id = request.form['area_id']
        branch_name = request.form['branch_name']
        branch_code = request.form['branch_code']
        cur.execute(
            "INSERT INTO tbl_branch (division_id, area_id, branch_name, branch_code) VALUES (%s, %s, %s, %s)",
            (division_id, area_id, branch_name, branch_code)
        )
        mysql.connection.commit()
        flash('Branch added successfully!', 'success')
        return redirect(url_for('record_branch.record_branch'))

    # Adjust query based on search input
    if search:
        search_pattern = f"%{search}%"
        cur.execute("""
            SELECT b.branch_id, b.branch_name, b.branch_code, a.area_name, a.area_code, d.division_name, d.division_code
            FROM tbl_branch b
            JOIN tbl_area a ON b.area_id = a.area_id
            JOIN tbl_division d ON b.division_id = d.division_id
            WHERE b.branch_name LIKE %s OR b.branch_code LIKE %s OR a.area_name LIKE %s OR a.area_code LIKE %s OR d.division_name LIKE %s OR d.division_code LIKE %s
        """, (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern))
    else:
        cur.execute("""
            SELECT b.branch_id, b.branch_name, b.branch_code, a.area_name, a.area_code, d.division_name, d.division_code
            FROM tbl_branch b
            JOIN tbl_area a ON b.area_id = a.area_id
            JOIN tbl_division d ON b.division_id = d.division_id
        """)
    branches = cur.fetchall()
    cur.close()
    return render_template('record_branch.html', branches=branches, divisions=divisions, areas=areas, search=search)

# Edit Branch
@record_branch_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_branch(id):
    cur = mysql.connection.cursor()
    # Get all divisions and areas for dropdowns
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()
    cur.execute("SELECT area_id, area_name, area_code FROM tbl_area")
    areas = cur.fetchall()

    if request.method == 'POST':
        division_id = request.form['division_id']
        area_id = request.form['area_id']
        branch_name = request.form['branch_name']
        branch_code = request.form['branch_code']
        cur.execute(
            "UPDATE tbl_branch SET division_id=%s, area_id=%s, branch_name=%s, branch_code=%s WHERE branch_id=%s",
            (division_id, area_id, branch_name, branch_code, id)
        )
        mysql.connection.commit()
        flash('Branch updated successfully!', 'success')
        return redirect(url_for('record_branch.record_branch'))
    
    # Get branch data
    cur.execute("SELECT branch_id, division_id, area_id, branch_name, branch_code FROM tbl_branch WHERE branch_id=%s", (id,))
    branch = cur.fetchone()
    
    cur.close()
    return render_template('edit_branch.html', branch=branch, divisions=divisions, areas=areas)

# Delete Branch
@record_branch_bp.route('/delete/<int:id>', methods=['POST'])
def delete_branch(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_branch WHERE branch_id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Branch deleted successfully!', 'success')
    return redirect(url_for('record_branch.record_branch'))
