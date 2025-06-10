from flask import Blueprint, render_template, request, redirect, url_for, flash

record_country_bp = Blueprint('record_country', __name__, url_prefix='/country')

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

@record_country_bp.route('/', methods=['GET', 'POST'])
def record_country():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name_country = request.form['name_country']
        cur.execute("INSERT INTO tbl_country (name_country) VALUES (%s)", (name_country,))
        mysql.connection.commit()
        flash('Country added successfully!', 'success')
        return redirect(url_for('record_country.record_country'))
    cur.execute("SELECT id, name_country FROM tbl_country")
    countries = cur.fetchall()
    cur.close()
    return render_template('record_country.html', countries=countries)

@record_country_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_country(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name_country = request.form['name_country']
        cur.execute("UPDATE tbl_country SET name_country=%s WHERE id=%s", (name_country, id))
        mysql.connection.commit()
        flash('Country updated successfully!', 'success')
        return redirect(url_for('record_country.record_country'))
    cur.execute("SELECT id, name_country FROM tbl_country WHERE id=%s", (id,))
    country = cur.fetchone()
    cur.close()
    return render_template('edit_country.html', country=country)

@record_country_bp.route('/delete/<int:id>', methods=['POST'])
def delete_country(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_country WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Country deleted successfully!', 'success')
    return redirect(url_for('record_country.record_country'))
