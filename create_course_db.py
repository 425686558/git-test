from course_dao import *

path = 'student_database.db'

course_dao = CourseDAO(path)

course_dao.create_table_CourseTable()

course_dao.destroy_table()
