-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2025 at 06:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `olmis_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin`
--

CREATE TABLE `tbl_admin` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_admin`
--

INSERT INTO `tbl_admin` (`id`, `username`, `password`) VALUES
(1, 'armavi', '25d55ad283aa400af464c76d713c07ad'),
(2, 'armavi', '25d55ad283aa400af464c76d713c07ad');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_area`
--

CREATE TABLE `tbl_area` (
  `area_id` int(11) NOT NULL,
  `division_id` int(100) NOT NULL,
  `area_name` varchar(100) DEFAULT NULL,
  `area_code` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_area`
--

INSERT INTO `tbl_area` (`area_id`, `division_id`, `area_name`, `area_code`) VALUES
(13, 7, 'Munshiganj', 'MUN111'),
(15, 8, 'Rangamati', 'RAG22');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_branch`
--

CREATE TABLE `tbl_branch` (
  `branch_id` int(11) NOT NULL,
  `division_id` int(100) NOT NULL,
  `area_id` int(100) NOT NULL,
  `branch_name` varchar(100) DEFAULT NULL,
  `branch_code` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_branch`
--

INSERT INTO `tbl_branch` (`branch_id`, `division_id`, `area_id`, `branch_name`, `branch_code`) VALUES
(11, 7, 13, 'Mawa', 'SHK122');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_country`
--

CREATE TABLE `tbl_country` (
  `id` int(11) NOT NULL,
  `name_country` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_country`
--

INSERT INTO `tbl_country` (`id`, `name_country`) VALUES
(1, 'Bangladesh'),
(2, 'India'),
(3, 'Hunululu');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_division`
--

CREATE TABLE `tbl_division` (
  `division_id` int(11) NOT NULL,
  `division_name` varchar(100) DEFAULT NULL,
  `division_code` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_division`
--

INSERT INTO `tbl_division` (`division_id`, `division_name`, `division_code`) VALUES
(7, 'Dhaka', 'DHK'),
(8, 'Chattogram', 'CTG');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_laywer_register`
--

CREATE TABLE `tbl_laywer_register` (
  `id` int(11) NOT NULL,
  `branch_name` varchar(100) DEFAULT NULL,
  `branch_code` varchar(100) DEFAULT NULL,
  `area_name` varchar(100) DEFAULT NULL,
  `area_code` varchar(100) DEFAULT NULL,
  `division_name` varchar(100) DEFAULT NULL,
  `division_code` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `name_english` varchar(150) DEFAULT NULL,
  `name_bangla` varchar(150) DEFAULT NULL,
  `bar_council_passing_year` varchar(100) DEFAULT NULL,
  `bar_council_certificate_no` varchar(100) DEFAULT NULL,
  `year_permission_practice_high_court` varchar(100) DEFAULT NULL,
  `year_permission_practice_appellate` varchar(100) DEFAULT NULL,
  `bar_association_membership_no` varchar(500) DEFAULT NULL,
  `member_of_bar_association` varchar(100) DEFAULT NULL,
  `bar_at_law` varchar(150) DEFAULT NULL,
  `address_present_english` text DEFAULT NULL,
  `address_present_bangla` text DEFAULT NULL,
  `address_permanent_english` text DEFAULT NULL,
  `address_permanent_bangla` text DEFAULT NULL,
  `address_court_chamber_english` text DEFAULT NULL,
  `address_court_chamber_bangla` text DEFAULT NULL,
  `address_personal_chamber_english` text DEFAULT NULL,
  `address_personal_chamber_bangla` text DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `nid` varchar(100) DEFAULT NULL,
  `experiences` text DEFAULT NULL,
  `other_academic_qualifications` text DEFAULT NULL,
  `passport_no` varchar(100) DEFAULT NULL,
  `passport_expiry_date` date DEFAULT NULL,
  `overseas_national_id` varchar(100) DEFAULT NULL,
  `diploma_or_professional_degree` text DEFAULT NULL,
  `other_training` text DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `highest_education` varchar(100) DEFAULT NULL,
  `photo_filename` varchar(255) DEFAULT NULL,
  `codice_fiscale` varchar(100) DEFAULT NULL,
  `document_branch_inward_no` varchar(100) DEFAULT NULL,
  `document_ho_inward_no` varchar(100) DEFAULT NULL,
  `type_of_application` varchar(100) NOT NULL,
  `application_session` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_laywer_register`
--

INSERT INTO `tbl_laywer_register` (`id`, `branch_name`, `branch_code`, `area_name`, `area_code`, `division_name`, `division_code`, `country`, `name_english`, `name_bangla`, `bar_council_passing_year`, `bar_council_certificate_no`, `year_permission_practice_high_court`, `year_permission_practice_appellate`, `bar_association_membership_no`, `member_of_bar_association`, `bar_at_law`, `address_present_english`, `address_present_bangla`, `address_permanent_english`, `address_permanent_bangla`, `address_court_chamber_english`, `address_court_chamber_bangla`, `address_personal_chamber_english`, `address_personal_chamber_bangla`, `email`, `mobile`, `nid`, `experiences`, `other_academic_qualifications`, `passport_no`, `passport_expiry_date`, `overseas_national_id`, `diploma_or_professional_degree`, `other_training`, `date_of_birth`, `highest_education`, `photo_filename`, `codice_fiscale`, `document_branch_inward_no`, `document_ho_inward_no`, `type_of_application`, `application_session`) VALUES
(80, 'Sheikher Tek', 'SHK122', 'Munshiganj', 'MUN111', 'Dhaka', 'DHK', 'India', 'Kibo Shannon', 'Imogene Morris', '2018', 'Commodo et et esse r', '1999', '1975', 'Ullam et quia consec', 'BAR 1112', 'Eligendi id enim ve', 'Excepteur aperiam as', 'Aut corrupti quis v', 'Voluptatem Pariatur', 'Hic velit dolorum cu', 'Minim reprehenderit', 'Dolore deserunt omni', 'Ad ex magnam id quae', 'Et neque est amet ', 'cimahypomo@mailinator.com', 'Excepturi non id dic', 'Eos et in possimus', 'Qui pariatur Assume', 'Id asperiores amet ', 'Omnis aut sit Nam d', '1980-07-02', 'Voluptate qui ad per', 'At ut in aliqua Nem', 'Sunt quo aut quia et', '2019-07-11', 'Anim atque earum ea ', NULL, 'Perspiciatis repudi', 'Enim ut magnam imped', 'Nulla rem adipisci s', 'New', '2021-11-25'),
(81, 'Branch 1', 'B001', 'Area 1', 'A001', 'Division 1', 'D001', 'Bangladesh', 'John Doe', 'জন ডো', '2015', 'BC12345', '2016', '2017', 'BM123', 'ABA', 'Yes', 'Present Address 1', 'বর্তমান ঠিকানা ১', 'Permanent Address 1', 'স্থায়ী ঠিকানা ১', 'Court Address 1', 'আদালতের ঠিকানা ১', 'Personal Chamber 1', 'ব্যক্তিগত চেম্বার ১', 'john@example.com', '8801712345678', '123456789', '5 years', 'M.A', 'P1234567', '2025-12-31', 'ON123', 'MBA', 'Training 1', '1990-01-01', 'PhD', NULL, 'CF123', 'IN123', 'HO123', 'New', '1978-02-14'),
(82, 'Branch 2', 'B002', 'Area 2', 'A002', 'Division 2', 'D002', 'Bangladesh', 'Jane Smith', 'জেন স্মিথ', '2016', 'BC12346', '2017', '2018', 'BM124', 'CBA', 'No', 'Present Address 2', 'বর্তমান ঠিকানা ২', 'Permanent Address 2', 'স্থায়ী ঠিকানা ২', 'Court Address 2', 'আদালতের ঠিকানা ২', 'Personal Chamber 2', 'ব্যক্তিগত চেম্বার ২', 'jane@example.com', '8801712345679', '987654321', '6 years', 'M.Sc', 'P1234568', '2026-12-31', 'ON124', 'M.Sc', 'Training 2', '1989-05-12', 'Masters', NULL, 'CF124', 'IN124', 'HO124', 'Renewal', '1978-02-14'),
(83, 'Branch 12', 'B003', 'Area 3', 'A003', 'Division 3', 'D003', 'Bangladesh', 'Alice Brown', 'এলিস ব্রাউন', '2017', 'BC12347', '2018', '2019', 'BM125', 'MBA', 'Yes', 'Present Address 3', 'বর্তমান ঠিকানা ৩', 'Permanent Address 3', 'স্থায়ী ঠিকানা ৩', 'Court Address 3', 'আদালতের ঠিকানা ৩', 'Personal Chamber 3', 'ব্যক্তিগত চেম্বার ৩', 'alice@example.com', '8801712345680', '112233445', '7 years', 'B.A', 'P1234569', '2027-12-31', 'ON125', 'LLB', 'Training 3', '1985-07-22', 'Bachelors', NULL, 'CF125', 'IN125', 'HO125', 'Update', '1978-02-14');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_member_of_bar_association`
--

CREATE TABLE `tbl_member_of_bar_association` (
  `id` int(11) NOT NULL,
  `name_member_of_bar_association` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_member_of_bar_association`
--

INSERT INTO `tbl_member_of_bar_association` (`id`, `name_member_of_bar_association`) VALUES
(1, 'BAR 1110'),
(2, 'BAR 1112'),
(5, 'BAR 1111');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_type_of_application`
--

CREATE TABLE `tbl_type_of_application` (
  `id` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `application_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_type_of_application`
--

INSERT INTO `tbl_type_of_application` (`id`, `status`, `application_type`) VALUES
(5, 'Active', 'New');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_area`
--
ALTER TABLE `tbl_area`
  ADD PRIMARY KEY (`area_id`);

--
-- Indexes for table `tbl_branch`
--
ALTER TABLE `tbl_branch`
  ADD PRIMARY KEY (`branch_id`);

--
-- Indexes for table `tbl_country`
--
ALTER TABLE `tbl_country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_division`
--
ALTER TABLE `tbl_division`
  ADD PRIMARY KEY (`division_id`);

--
-- Indexes for table `tbl_laywer_register`
--
ALTER TABLE `tbl_laywer_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_member_of_bar_association`
--
ALTER TABLE `tbl_member_of_bar_association`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_type_of_application`
--
ALTER TABLE `tbl_type_of_application`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_area`
--
ALTER TABLE `tbl_area`
  MODIFY `area_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `tbl_branch`
--
ALTER TABLE `tbl_branch`
  MODIFY `branch_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `tbl_country`
--
ALTER TABLE `tbl_country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_division`
--
ALTER TABLE `tbl_division`
  MODIFY `division_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_laywer_register`
--
ALTER TABLE `tbl_laywer_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `tbl_member_of_bar_association`
--
ALTER TABLE `tbl_member_of_bar_association`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_type_of_application`
--
ALTER TABLE `tbl_type_of_application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
