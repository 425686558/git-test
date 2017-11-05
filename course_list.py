from tkinter import *
from course_table import *
from course_dao import *

class CourseList(Frame):
    def __init__(self, options, parent = None):
        Frame.__init__(self, parent)
        self.pack(expand = YES, fill = BOTH)
        self.make_widgets()
        self.show_data_list(options)

    def handle_list(self,event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.run_command(label)

    def make_widgets(self):
        sbar = Scrollbar(self)
        list = Listbox(self, relief = SUNKEN)
        sbar.config(command = list.yview)
        list.config(yscollcommand = sbar.set)
        sbar.pack(side = RIGHT, fill = Y)
        list.pack(side = LEFT, expand = YES, fill = BOTH)
        self.listbox = list

    def show_data_list(self, options):
        pos = 0
        for crs in options:
            self.listbox.insert(pos,str(crs))
            pos += 1

    def run_command(self, selection):
        print('You selected:', selection)

if __name__ == '__main__':
    course = []
    for i in range(20):
        course = Course()
        course.course_id = i
        course.course_title = str(i)