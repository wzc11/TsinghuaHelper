__author__ = 'CaoYe'
from store import *


class store_academic(store):
    def user_update(self, user):
        user_list = User.objects(user_id=self.user_id)
        try:
            user_old = user_list.next()
            User.objects(user_id=self.user_id).update(
                set__course_info=user.course_info,
                set__learn_info=user.learn_info
            )
        except Exception, e:
            user.save()

    def academic_store(self):
        try:
            academic = hunter_academic('caoy11', 'memory2011')
            person = academic.getPersonInfo()[0]
            basic = academic.getBasicInfo()
            course_list = academic.getCourseInfo()
            person_info = PersonInfo(
                major=person['专业'.decode('UTF-8')],
                is_at_school=person['是否在校'.decode('UTF-8')],
                is_minor=person['是否辅修'.decode('UTF-8')],
                is_second_degree=person['第二学位否'.decode('UTF-8')],
                student_number=person['学号'.decode('UTF-8')],
                phone=person['联系电话手机'.decode('UTF-8')],
                identification=person['身份证号'.decode('UTF-8')],
                charge_type=person['收费类别'.decode('UTF-8')],
                is_register=person['是否有学籍'.decode('UTF-8')],
                nation=person['民族'.decode('UTF-8')],
                real_name=person['姓名'.decode('UTF-8')],
                teach_class=person['教学班'.decode('UTF-8')],
                department=person['院（系，所）'.decode('UTF-8')],
                birth_date=person['出生日期'.decode('UTF-8')],
                sex=person['性别'.decode('UTF-8')],
                email=person['常用电子邮箱'.decode('UTF-8')],
                graduate_date=person['毕业日期'.decode('UTF-8')]
            )
            timetable = []
            for course in course_list:
                course_single = SingleCourse(
                    revenue=course['revenue'],
                    teacher=course['teacher'],
                    caption=course['caption'],
                    time=course['time'],
                    duration=course['duration'],
                    type=course['type'],
                    day=course['day']
                )
                timetable.append(course_single)
            user = User(
                timetable=timetable,
                personal_info=person_info
            )
            self.user_update(user)
            return True
        except Exception, e:
            return False