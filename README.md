# OLMS: Online Lawyer Management System

OLMS (Online Lawyer Management System) is a modern, full-featured web application designed to streamline the management of legal professionals and organizational units such as divisions, branches, areas, and bar association members. Built using Flask (Python), MySQL, and Bootstrap, OLMS provides a clean, responsive, and user-friendly interface for legal organizations, law firms, bar associations, and administrative users.

---

## 🚀 Features

- **Division Management:** Add, edit, delete, and list divisions of the organization.
- **Branch Management:** Manage branches under each division with live search and edit/delete support.
- **Area Management:** Organize areas under branches and divisions using intuitive dropdowns and validation.
- **Member of Bar Association:** Record and manage members of bar associations in a dedicated module.
- **Lawyer Registration:** Comprehensive form with dependent dropdowns for Division, Branch, Area, Country, and Bar Association.
- **Live Table Filtering:** Instant search/filter for branches, areas, and members.
- **Responsive UI:** Clean Bootstrap 5 interface, mobile-ready, with consistent navigation.
- **Safe Data Handling:** Prevents deletion of records that are in use by dependent modules (if foreign key constraints are enabled).
- **Extensible:** Easily add more modules or integrate with external APIs (e.g., for verification or notifications).

---

## 🏗️ Technologies Used

- **Backend:** Python, Flask, flask-mysqldb
- **Database:** MySQL
- **Frontend:** HTML, Bootstrap 5, JavaScript (jQuery for dependent dropdowns)
- **Other:** Jinja2 templates, AJAX for dynamic field updates

---

## 📦 Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/olms.git
    cd olms
    ```

2. **Set Up Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create MySQL Database:**
    - Log in to MySQL and run the provided schema (see `database/schema.sql` in the repo).

5. **Configure Database Connection:**
    - In `app.py`, set your MySQL credentials:
      ```python
      app.config['MYSQL_HOST'] = 'localhost'
      app.config['MYSQL_USER'] = 'root'
      app.config['MYSQL_PASSWORD'] = ''
      app.config['MYSQL_DB'] = 'olmis_db'
      ```

6. **Run the Application:**
    ```bash
    python app.py
    ```
    - The app will run at [http://localhost:5000](http://localhost:5000) or (http://127.0.0.1:5000/)

---

## 📚 Usage

- **Divisions:** Manage organizational divisions.
- **Branches:** Manage branches under each division. Use the search box for quick filtering.
- **Areas:** Manage areas with division/branch dropdowns for proper hierarchy.
- **Member of Bar Association:** Add and manage Bar Association members.
- **Lawyer Registration:** Register new lawyers, with smart dependent dropdowns.

> **Tip:** Navigate using the top navbar. All actions (add, edit, delete) use user-friendly modals or confirmation dialogs.

---

## 📂 Project Structure
olms/
├── app.py
├── requirements.txt
├── record_division.py
├── record_branch.py
├── record_area.py
├── record_member_of_bar_association.py
├── templates/
│ ├── record_division.html
│ ├── record_branch.html
│ ├── record_area.html
│ ├── record_member_of_bar_association.html
│ └── ...
├── static/
│ ├── ...
└── database/
└── schema.sql
