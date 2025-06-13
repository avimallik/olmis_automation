from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Define the blueprint for Area
record_area_bp = Blueprint('record_area', __name__, url_prefix='/area')

mysql = None

def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

# List and Add Area
@record_area_bp.route('/', methods=['GET', 'POST'])
def record_area():
    cur = mysql.connection.cursor()
    # Get all divisions for the dropdown
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()

    search = request.args.get('search', '').strip()  # Get search value from query string

    if request.method == 'POST':
        division_id = request.form['division_id']
        area_name = request.form['area_name']
        area_code = request.form['area_code']
        cur.execute(
            "INSERT INTO tbl_area (division_id, area_name, area_code) VALUES (%s, %s, %s)",
            (division_id, area_name, area_code)
        )
        mysql.connection.commit()
        flash('Area added successfully!', 'success')
        return redirect(url_for('record_area.record_area'))

    # Adjust query based on search input
    if search:
        search_pattern = f"%{search}%"
        cur.execute("""
            SELECT a.area_id, a.area_name, a.area_code, d.division_name, d.division_code
            FROM tbl_area a
            JOIN tbl_division d ON a.division_id = d.division_id
            WHERE a.area_name LIKE %s OR a.area_code LIKE %s OR d.division_name LIKE %s OR d.division_code LIKE %s
        """, (search_pattern, search_pattern, search_pattern, search_pattern))
    else:
        cur.execute("""
            SELECT a.area_id, a.area_name, a.area_code, d.division_name, d.division_code
            FROM tbl_area a
            JOIN tbl_division d ON a.division_id = d.division_id
        """)
    areas = cur.fetchall()
    cur.close()
    return render_template('record_area.html', areas=areas, divisions=divisions, search=search)

# Edit Area
@record_area_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_area(id):
    cur = mysql.connection.cursor()
    # Get all divisions for dropdown
    cur.execute("SELECT division_id, division_name, division_code FROM tbl_division")
    divisions = cur.fetchall()
    if request.method == 'POST':
        division_id = request.form['division_id']
        area_name = request.form['area_name']
        area_code = request.form['area_code']
        cur.execute(
            "UPDATE tbl_area SET division_id=%s, area_name=%s, area_code=%s WHERE area_id=%s",
            (division_id, area_name, area_code, id)
        )
        mysql.connection.commit()
        flash('Area updated successfully!', 'success')
        return redirect(url_for('record_area.record_area'))
    # Get area data
    cur.execute("SELECT area_id, division_id, area_name, area_code FROM tbl_area WHERE area_id=%s", (id,))
    area = cur.fetchone()
    cur.close()
    return render_template('edit_area.html', area=area, divisions=divisions)

# Delete Area
@record_area_bp.route('/delete/<int:id>', methods=['POST'])
def delete_area(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_area WHERE area_id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Area deleted successfully!', 'success')
    return redirect(url_for('record_area.record_area'))
