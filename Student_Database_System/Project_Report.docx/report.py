# Generate a full PDF project report for the Student Database System using reportlab (platypus)

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors

file_path = "/mnt/data/Student_Database_System_Project_Report.pdf"

styles = getSampleStyleSheet()
elements = []

# Title Page
elements.append(Paragraph("STUDENT DATABASE SYSTEM USING SQL", styles['Title']))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Mini Project Report", styles['Heading2']))
elements.append(Spacer(1, 40))
elements.append(Paragraph("Submitted by: Neha Muddanal", styles['Normal']))
elements.append(Paragraph("Course: Data Analyst / Computer Science", styles['Normal']))
elements.append(Paragraph("Submission Year: 2026", styles['Normal']))
elements.append(Spacer(1, 200))
elements.append(Paragraph("Project Topic: Student Database System", styles['Heading3']))
elements.append(PageBreak())

# Introduction
elements.append(Paragraph("1. Introduction", styles['Heading2']))
intro = """
The Student Database System is a database project developed using SQL to manage student information efficiently.
This system stores student personal details, courses, grades, and attendance records in a structured format.
It helps administrators easily add new students, update grades, track attendance, and generate reports.
"""
elements.append(Paragraph(intro, styles['BodyText']))
elements.append(Spacer(1, 12))

# Objectives
elements.append(Paragraph("2. Objectives", styles['Heading2']))
objectives = """
• Store student information in a structured database.<br/>
• Manage course details and student enrollment.<br/>
• Record and update student grades.<br/>
• Maintain attendance records.<br/>
• Generate reports for academic analysis.
"""
elements.append(Paragraph(objectives, styles['BodyText']))
elements.append(Spacer(1, 12))

# Tools
elements.append(Paragraph("3. Tools and Technologies Used", styles['Heading2']))
tools = """
• MySQL / MySQL Workbench<br/>
• Structured Query Language (SQL)<br/>
• Computer System
"""
elements.append(Paragraph(tools, styles['BodyText']))
elements.append(Spacer(1, 12))

# Database Tables
elements.append(Paragraph("4. Database Design", styles['Heading2']))
table_data = [
["Table Name","Description"],
["Students","Stores student personal information"],
["Courses","Stores course details"],
["Grades","Stores marks obtained by students"],
["Attendance","Stores attendance records"]
]

table = Table(table_data)
table.setStyle([
("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
("GRID",(0,0),(-1,-1),1,colors.black)
])
elements.append(table)
elements.append(Spacer(1, 20))

# SQL Queries
elements.append(Paragraph("5. Important SQL Queries", styles['Heading2']))
sql_text = """
Create Database:<br/>
CREATE DATABASE StudentDB;<br/><br/>

Create Students Table:<br/>
CREATE TABLE Students (
student_id INT PRIMARY KEY,
name VARCHAR(50),
gender VARCHAR(10),
department VARCHAR(50),
address VARCHAR(100),
phone VARCHAR(15)
);<br/><br/>

Insert Student Data:<br/>
INSERT INTO Students VALUES (1,'Rahul','Male','Computer Science','Pune','9876543210');<br/><br/>

Average Marks Query:<br/>
SELECT student_id, AVG(marks) FROM Grades GROUP BY student_id;
"""
elements.append(Paragraph(sql_text, styles['BodyText']))
elements.append(Spacer(1, 20))

# Features
elements.append(Paragraph("6. Key Features", styles['Heading2']))
features = """
• Add new student records<br/>
• Update student grades<br/>
• Track attendance records<br/>
• Calculate average marks<br/>
• Generate performance reports
"""
elements.append(Paragraph(features, styles['BodyText']))
elements.append(Spacer(1, 12))

# Conclusion
elements.append(Paragraph("7. Conclusion", styles['Heading2']))
conclusion = """
The Student Database System helps manage academic information efficiently using SQL queries.
It allows easy storage, retrieval, and analysis of student data. This project demonstrates how
database management systems can be used in educational institutions to maintain accurate records.
"""
elements.append(Paragraph(conclusion, styles['BodyText']))

doc = SimpleDocTemplate(file_path, pagesize=A4)
doc.build(elements)

file_path