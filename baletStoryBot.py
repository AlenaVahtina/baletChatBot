# coding=utf-8
from vk_api.upload import VkUpload
from connect import *
import  sched, time

upload_url = None
s = sched.scheduler(time.time, time.sleep)


def create_story(file_name='balteR3.png'):
    upload = vk_api.VkUpload(vk_session)
    upload.story(
        file_name,
        'photo',
        group_id='178073199')

def its_time_create_story():
    s.enter(10, 1, create_story())
    s.run()
