A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if

Age and marks are valid and
Marks is 65 or more
Write a python program to represent the students seeking admission in the university.

The details of student class are given below.

Class name: Student

Attributes
(private)

student_id
marks
age

 

Methods
(public)

__init__()

Create and initialize all instance variables to None

 

validate_marks()

 

If data is valid, return true. Else, return false

 

validate_age()

 

check_qualification()

Validate marks and age.

If valid, check if marks is 65 or more.
If so return true
Else return false
Else return false
 

setter methods

Include setter methods for all instance variables to set its values

 

getter methods

Include getter methods for all instance variables to get its values