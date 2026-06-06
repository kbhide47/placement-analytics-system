# placement-analytics-system
Placement Analytics System for managing student placement records and generating recruitment insights using Python and SQL.
# Placement Analytics System

## Overview

Placement Analytics System is a database-driven application developed to manage student placement records and generate meaningful insights from placement data. The system helps track student placements, company recruitment statistics, salary packages, and branch-wise placement performance.

The project is designed to simplify placement data management and support data-driven decision-making through analytical reports.

---

## Features

### Student Management
- Add new student records
- Update student details
- View student information
- Delete student records

### Company Management
- Add recruiting companies
- Store package details
- View company information

### Placement Tracking
- Record placed students
- Map students to recruiting companies
- Maintain placement history

### Analytics & Reporting
- Calculate placement percentage
- Identify highest package offered
- Calculate average package
- Generate branch-wise placement statistics
- Identify top recruiting companies
- Generate placement summary reports

---

## Technologies Used

- Python
- MySQL
- SQL
- MySQL Connector for Python

---

## Database Design

The system consists of three main tables:

### Students
Stores student information including:
- Student ID
- Name
- Branch
- CGPA

### Companies
Stores company details including:
- Company ID
- Company Name
- Package Offered

### Placements
Stores placement records including:
- Placement ID
- Student ID
- Company ID
- Placement Year

---

## Key SQL Concepts Implemented

- Joins
- Aggregate Functions
- GROUP BY
- ORDER BY
- COUNT()
- AVG()
- MAX()
- Foreign Keys
- Primary Keys
- Relational Database Design

---

## Sample Insights Generated

- Total number of students placed
- Overall placement percentage
- Highest salary package
- Average salary package
- Branch-wise placement performance
- Top recruiting companies

Example Report:

Placement Percentage : 85%

Highest Package : 18 LPA

Average Package : 7.4 LPA

Top Recruiter : TCS

Best Performing Branch : ENTC

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Database design and normalization
- SQL query optimization
- Data analysis and reporting
- Python-MySQL integration
- Problem-solving using structured data
- Building menu-driven applications

---

## Future Enhancements

- Graphical User Interface (GUI)
- Data visualization dashboards
- Export reports to Excel/PDF
- Placement prediction using Machine Learning
- Web-based deployment

---

## Screenshot

### Main Menu

![Main Menu](screenshots/main_menu.png)

## Author

Kasturi Bhide

Electronics and Telecommunication Engineering Student

Interested in Python, SQL, Data Analytics, and Software Development.
