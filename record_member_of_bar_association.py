from flask import Blueprint, render_template, request, redirect, url_for, flash

record_member_of_bar_association_bp = Blueprint(
    'record_member_of_bar_association', __name__, url_prefix='/member-of-bar-association'
)

mysql = None
def init_mysql(mysql_obj):
    global mysql
    mysql = mysql_obj

# List and Add Member
@record_member_of_bar_association_bp.route('/', methods=['GET', 'POST'])
def record_member_of_bar_association():
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        name = request.form['name_member_of_bar_association']
        cur.execute(
            "INSERT INTO tbl_member_of_bar_association (name_member_of_bar_association) VALUES (%s)",
            (name,)
        )
        mysql.connection.commit()
        flash('Member added successfully!', 'success')
        return redirect(url_for('record_member_of_bar_association.record_member_of_bar_association'))

    cur.execute("SELECT id, name_member_of_bar_association FROM tbl_member_of_bar_association")
    members = cur.fetchall()
    cur.close()
    return render_template(
        'record_member_of_bar_association.html',
        members=members
    )

# Edit Member
@record_member_of_bar_association_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_member_of_bar_association(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name_member_of_bar_association']
        cur.execute(
            "UPDATE tbl_member_of_bar_association SET name_member_of_bar_association=%s WHERE id=%s",
            (name, id)
        )
        mysql.connection.commit()
        flash('Member updated successfully!', 'success')
        return redirect(url_for('record_member_of_bar_association.record_member_of_bar_association'))
    cur.execute("SELECT id, name_member_of_bar_association FROM tbl_member_of_bar_association WHERE id=%s", (id,))
    member = cur.fetchone()
    cur.close()
    return render_template(
        'edit_member_of_bar_association.html',
        member=member
    )

# Delete Member
@record_member_of_bar_association_bp.route('/delete/<int:id>', methods=['POST'])
def delete_member_of_bar_association(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_member_of_bar_association WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Member deleted successfully!', 'success')
    return redirect(url_for('record_member_of_bar_association.record_member_of_bar_association'))
