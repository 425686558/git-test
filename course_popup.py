from tkinter import *
from sqlite3_helper import *
from course_dao import *
from course_table import *

class CoursePopupWnd(Toplevel):
    def __init__(self, course_dao, parent = None):
        Toplevel.__init__(self, parent)

        self.lbl_list = ['课程编号','课程名称']
        self.variables = []
        self.make_modal = True

        self.course_dao = course_dao
        self.make_widgets = True

    def add_course(self):
        course = Course()
        course.course_id = self.variables[0].get()
        course.course_title = self.variables[1].get()
        self.course_dao.course_add(course)

    def wnd_close(self):
        self.destroy()

    def make_widgets(self):
        frame_top = Frame(self)
        frame_bottom = Frame(self)
        frame_top.pack(side = TOP)
        frame_bottom.pack(side = BOTTOM)
        frame_left = Frame(frame_top)
        frame_right = Frame(frame_top)
        frame_left.pack(side = LEFT)
        frame_right.pack(side = RIGHT, expand = YES, fill = X)

        Button(frame_bottom, text = '添加', command = self.add_course).pack(side = LEFT)
        Button(frame_bottom, text = '关闭', command = self.wnd_close).pack(side = LEFT)

        print(self.lbl_list)

        for lbl in self.lbl_list:
            lab = Label(frame_left,width = 10, text = lbl)
            lab.pack(side = TOP)
            ent = Entry(frame_right)
            ent.pack(side = TOP, fill = X)
            var = StringVar()
            ent.config(textvariable = var)
            self.variables.append(var)
        if self.make_modal:
            self.focus_set()
            self.grab_set()
            self.wait_window()
