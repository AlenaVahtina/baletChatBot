# coding=utf-8
from vk_api.upload import VkUpload
from connect import *

upload_url = None

upload = vk_api.VkUpload(vk_session)
upload.story(
    'balteR3.png',
    'photo',
    group_id='178073199')
