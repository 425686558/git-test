import sys
from tkinter import *
from course_popup import *
from course_list import *
from sqlite3_helper import *
from course_dao import *
from tkinter.filedialog import askopenfilename

make_modal = True

def dialog():
    dlg = CoursePopupWnd(course_dao)

def course_main_wnd_search():
    course_title_input = user_input.get()
    course_list = course_dao.course_search(course_title_input)
    CourseShowWnd.show_data_list(course_list)

def course_main_wnd_close():
    course_dao.destroy()
    root.destroy()

def course_delete_all():
    course_dao.course_delete_all()

def import_data_from_file():
    filename = askopenfilename()
    print("打开了filename")

    file = open(filename, mode = 'r')
    rows = []
    for line in file:
        data = line.rstrip().split(',')
        rows.append(data)
    for rec in rows:
        print(rec)
        course = Course()
        course.course_id = int(rec[0])
        course.course_title = rec[1]
        course_dao.course_add(course)


root = Tk()
root.geometry('500x500')
path = 'student_database.db'
course_dao = CourseDAO(path)
courses = []
frame_top = Frame(root)
frame_top.pack(side = TOP)
CourseShowWnd = CourseList(courses, parent=root)
CourseShowWnd.pack(side = BOTTOM)

lab = Label(frame_top, width = 5, text = '课程名称')
ent = Entry(frame_top)
user_input = StringVar()
ent.config(textvariable = user_input)
btn_add = Button(frame_top, text = '添加', command = dialog)
btn_search = Button(frame_top, text = '检索', command = course_main_wnd_search)
btn_import = Button(frame_top, text = '导入', command = import_data_from_file)
btn_exit = Button(frame_top, text = '退出', command = course_main_wnd_close)
btn_delete_all = Button(frame_top, text = '删除所有数据', command = course_delete_all)

lab.grid(row = 0, column = 0)
ent.grid(row = 0, column = 0)
btn_search.grid(row = 1, column = 0)
btn_add.grid(row = 1, column = 1)
btn_import.grid(row = 2, column = 1)
btn_exit.grid(row = 2, column = 1)
btn_delete_all.grid(row = 3, column = 1)

root.mainloop()
