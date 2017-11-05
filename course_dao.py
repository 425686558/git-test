from sqlite3_helper import *
from course_table import *

class CourseDAO:
    def __init__(self,dbname):
        global DB_FILE_PATH
        DB_FILE_PATH = dbname
        self.conn = get_conn(DB_FILE_PATH)

    def destroy_table(self):
        self.conn.close()

    def create_table_CourseTable(self):
        print('创建数据库表测试')
        create_table_sql = '''CREATE TABLE CourseTable (
                               course_id int(15) NOT NULL,
                               course_title varchar(10) NOT NULL,
                               PRIMARY KEY (course_id)
                            )'''
        create_table(self.conn, create_table_sql)

    def course_add(self, course_table):
        key = self.max_key()
        key = key + 1
        course_table.course_id = key
        courseList = []
        courseList.append(course_table.course_id)
        courseList.append(course_table.course_title)

        sql = '''INSERT INTO CourseTable values (?,?)'''
        sqlite_insert(self.conn, sql, courseList)

    def course_update(self,CourseTable):
        update_sql = '''UPDATE CourseTable SET
                        course_id = ?,
                        course_title = ?,
                        WHERE course_id = ?'''
        data = [CourseTable.course_id, CourseTable.course_title]
        sqlite_update(self.conn, update_sql, data)

    def course_delete_all(self):
        delete_sql = 'DELETE FROM CourseTable'
        sqlite_delete_all(self.conn, delete_sql)

    def course_delete(self,course_id):
        delete_sql = 'DELETE FROM CourseTable WHERE course_id = ?'
        data = (course_id)
        sqlite_delete(self.conn, delete_sql, data)

    def data_to_course(self,row):
        course = Course()
        course.course_id = row[0]
        course.course_title = row[1]
        return course

    def course_search_all(self):
        fetchall_sql = 'SELECT * FROM CourseTable'
        rows = sqlite_fetchall(self.conn, fetchall_sql)

    def course_search(self,course_title):
        fetch_sql = ''
        if course_title == '':
            fetch_sql = 'SELECT * FROM CourseTable'
        else:
            fetch_sql = "SELECT * FROM CourseTable WHERE course_title like '%" + course_title + "%'"
        rows = sqlite_fetchall(self.conn,fetch_sql)
        courseList = []
        for row in rows:
            course = self.data_to_course(row)
            courseList.append(course)
        return courseList

    def course_search_one(self,course_id):
        fetchone_sql = 'SELECT * FROM CourseTable'
        row = sqlite_fetchone(self.conn, fetchone_sql, data)
        course = self.data_to_course(row)
        return course

    def max_key(self):
        max_key_sql = 'SELECT max(course_id) FROM CourseTable'
        row = sqlite_fetchkey(self.conn,max_key_sql)
        if row[0] == None:
            return 0
        else:
            key = int(row[0])
            return key





