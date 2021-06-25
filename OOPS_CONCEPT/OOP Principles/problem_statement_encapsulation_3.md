# Encapsulation Problem Statement  3
### TechWorld, a technology training center, wants to allocate courses for instructors.
1. An instructor is identified by name, technology skills, experience and average feedback.
2. An instructor is allocated a course, if he/she satisfies the below two conditions:

    eligibility criteria:
        if experience is more than 3 years, average feedback should be 4.5 or more
        if experience is 3 years or less, average feedback should be 4 or more
    he/she should posses the technology skill for the course
Identify the class name and attributes from the list of options below to represent instructors.

1. check_eligibility()
2. avg_feedback
3. experience
4. instructor_name
5. allocate_course()
6. allocate_course(technolody)
7. [__init__()]
8. Instructor
9. calculate_avg_feedback()
10. technology_skill

### Write a Python program to implement the class chosen with its attributes and methods.

**Note:**

1. Consider all instance variables to be private and methods to be public
2. An instructor may have multiple technology skills, so consider instance variable technology_skill to be a list
3. check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
4. allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false
5. Perform case sensitive string comparison
6. Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.