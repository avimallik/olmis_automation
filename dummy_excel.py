import pandas as pd

# Create a DataFrame with 3 rows of data
data = {
    'branch_name': ['Branch 1', 'Branch 2', 'Branch 3'],
    'branch_code': ['B001', 'B002', 'B003'],
    'area_name': ['Area 1', 'Area 2', 'Area 3'],
    'area_code': ['A001', 'A002', 'A003'],
    'division_name': ['Division 1', 'Division 2', 'Division 3'],
    'division_code': ['D001', 'D002', 'D003'],
    'country': ['Bangladesh', 'Bangladesh', 'Bangladesh'],
    'name_english': ['John Doe', 'Jane Smith', 'Alice Brown'],
    'name_bangla': ['জন ডো', 'জেন স্মিথ', 'এলিস ব্রাউন'],
    'bar_council_passing_year': [2015, 2016, 2017],
    'bar_council_certificate_no': ['BC12345', 'BC12346', 'BC12347'],
    'year_permission_practice_high_court': [2016, 2017, 2018],
    'year_permission_practice_appellate': [2017, 2018, 2019],
    'bar_association_membership_no': ['BM123', 'BM124', 'BM125'],
    'member_of_bar_association': ['ABA', 'CBA', 'MBA'],
    'bar_at_law': ['Yes', 'No', 'Yes'],
    'address_present_english': ['Present Address 1', 'Present Address 2', 'Present Address 3'],
    'address_present_bangla': ['বর্তমান ঠিকানা ১', 'বর্তমান ঠিকানা ২', 'বর্তমান ঠিকানা ৩'],
    'address_permanent_english': ['Permanent Address 1', 'Permanent Address 2', 'Permanent Address 3'],
    'address_permanent_bangla': ['স্থায়ী ঠিকানা ১', 'স্থায়ী ঠিকানা ২', 'স্থায়ী ঠিকানা ৩'],
    'address_court_chamber_english': ['Court Address 1', 'Court Address 2', 'Court Address 3'],
    'address_court_chamber_bangla': ['আদালতের ঠিকানা ১', 'আদালতের ঠিকানা ২', 'আদালতের ঠিকানা ৩'],
    'address_personal_chamber_english': ['Personal Chamber 1', 'Personal Chamber 2', 'Personal Chamber 3'],
    'address_personal_chamber_bangla': ['ব্যক্তিগত চেম্বার ১', 'ব্যক্তিগত চেম্বার ২', 'ব্যক্তিগত চেম্বার ৩'],
    'email': ['john@example.com', 'jane@example.com', 'alice@example.com'],
    'mobile': ['8801712345678', '8801712345679', '8801712345680'],
    'nid': ['123456789', '987654321', '112233445'],
    'experiences': ['5 years', '6 years', '7 years'],
    'other_academic_qualifications': ['M.A', 'M.Sc', 'B.A'],
    'passport_no': ['P1234567', 'P1234568', 'P1234569'],
    'passport_expiry_date': ['2025-12-31', '2026-12-31', '2027-12-31'],
    'overseas_national_id': ['ON123', 'ON124', 'ON125'],
    'diploma_or_professional_degree': ['MBA', 'M.Sc', 'LLB'],
    'other_training': ['Training 1', 'Training 2', 'Training 3'],
    'date_of_birth': ['1990-01-01', '1989-05-12', '1985-07-22'],
    'highest_education': ['PhD', 'Masters', 'Bachelors'],
    'codice_fiscale': ['CF123', 'CF124', 'CF125'],
    'document_branch_inward_no': ['IN123', 'IN124', 'IN125'],
    'document_ho_inward_no': ['HO123', 'HO124', 'HO125'],
    'type_of_application': ['New', 'Renewal', 'Update'],
    'application_session': ['1978-02-14', '1978-02-14', '1978-02-14']
}

df = pd.DataFrame(data)

# Save the dataframe to an Excel file
df.to_excel('test_data.xlsx', index=False)

print("Excel file generated successfully.")