__author__ = 'CaoYe'

from store import *


class store_learn(store):
    def user_update(self, user):
        if self.user_is_exist():
            User.objects(user_id=self.user_id).update(
                set__course_info=user.course_info,
                set__learn_info=user.learn_info
            )
        else:
            user.save()

    def learn_store(self):
        try:
            learn = hunter_learn(self.username, self.password)
            info = learn.getInfo()
            course_info_list = []
            course_list = []
            for course in info:
                course_caption_list = course['caption'].split('(')
                course_caption = course_caption_list[0]
                course_special = Course(
                    caption=course_caption,
                    id=course['id'],
                    file_unread=course['file_unread'],
                    homework=course['homework'],
                    notice_unread=course['notice_unread']
                )
                course_list.append(course_special)

                course_info = learn.getSpecial(course['id'])

                notice_info = course_info['notice']
                notice_list = []
                for notice in notice_info:
                    notice_special = SpecialNotice(
                        link=notice['link'],
                        caption=notice['caption'],
                        teacher=notice['teacher'],
                        date=notice['date']
                    )
                    notice_list.append(notice_special)

                classinfo_info = course_info['classinfo']
                classinfo_list = []
                for classinfo in classinfo_info:
                    classinfo_special = SpecialClassinfo(
                        teacher_name=classinfo['teacher_name'],
                        teacher_email=classinfo['teacher_email']
                    )
                    #debuger.printer(classinfo)
                    classinfo_list.append(classinfo_special)

                files_info = course_info['files']
                files_list = []
                for files in files_info:
                    files_special = SpecialFiles(
                        link=files['link'],
                        caption=files['caption'],
                        note=files['note'],
                        size=files['size'],
                        date=files['date']
                    )
                    files_list.append(files_special)

                homework_info = course_info['homework']
                homework_list = []
                for homework in homework_info:
                    homework_special = SpecialHomework(
                        caption=homework['caption'],
                        state=homework['state'],
                        link=homework['link'],
                        date=homework['date'],
                        deadline=homework['deadline'],
                        size=homework['size']
                    )
                    homework_list.append(homework_special)

                resources_info = course_info['resources']
                resources_list = []
                for resources in resources_info:
                    resources_special = SpecialResources(
                        link=resources['link'],
                        caption=resources['caption'],
                        note=resources['note']
                    )
                    resources_list.append(resources_special)

                special_info = Special(
                    caption=course_caption,
                    notice=notice_list,
                    classinfo=classinfo_list,
                    files=files_list,
                    homework=homework_list,
                    resources=resources_list
                )
                course_info_list.append(special_info)

            user = User(
                user_name=self.username,
                user_id=self.user_id,
                use_password=self.password,
                course_info=course_list,
                learn_info=course_info_list,
            )
            self.user_update(user)
            return True
        except Exception, e:
            print Exception, e
            self.user_delete()
            return False