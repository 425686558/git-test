class Course:
    def __init__(self):
        self.course_id = 0
        self.course_title = ""
    def __str__(self):
        show = "%15d,%10s"%(self.course_id,self.course_title)
        return show
