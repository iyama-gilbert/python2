# DICTIONARIES
# creating and using dictionary
# dictionary methods and operations
"""
summary
dictionary can be.
-ordered
-mutable
-indexed by keeys
"""

# example 1: creating dictionary
# create a dictionary for software engineering student with the keys as name,  age ,
#  technology of interest,course, yeasr of study. put your own details

student_dict={
    'name':'iyama',
    'age':'30',
    'technology':'AI and ML',
'course':'BSE',
    'year_of_study':'year3',
    }
print(student_dict['age'])
student_dict['technology']='web developmemt'
student_dict['age']=56
print(student_dict)


# example2: adding keys and values 
student_dict['email']='yamexgilbs@gmail.com'
print(student_dict)

# removing keys and values from dictionary
del student_dict['email']
print(student_dict)

