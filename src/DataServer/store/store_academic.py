__author__ = 'CaoYe'
# -*- coding: utf-8 -*-
from store import *
from Assistant.config import *
import glob
from PIL import Image


class store_academic(store):
    def user_update(self, user):
        User.objects(user_id=self.user_id).update(
            set__timetable=user.timetable,
            set__person_info=user.person_info
        )

    def image_handle(self):
        ima = Image.open(old_img_root + self.user_id + '.jpg')
        imb = ima.resize((243, 300))
        imc = Image.new("RGB", (540, 300), 'white')
        imc.paste(imb, (149, 0, 392, 300))
        imc.save(new_img_root + self.user_id + '.jpg')

    def academic_store(self):
        try:
            academic = hunter_academic(self.username, self.password)
            basic = academic.getBasicInfo()
            #get person_info
            person_test = academic.getPersonInfo(self.user_id)
            count = 0
            while len(person_test) == 0 and count < 20:
                count += 1
                person_test = academic.getPersonInfo(self.user_id)
            person = person_test[0]
            self.image_handle()
            #get timetable
            course_list = academic.getCourseInfo()
            count = 0
            while len(course_list) == 0 and count < 50:
                count += 1
                course_list = academic.getCourseInfo()
            course_test = course_list[0]
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
                person_info=person_info
            )
            self.user_update(user)
            return True
        except Exception, e:
            self.user_delete()
            return False