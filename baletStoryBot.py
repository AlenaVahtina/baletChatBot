# coding=utf-8
from vk_api.upload import VkUpload
from connect import *

upload_url = None
# try:
#     vk_session.authorization()
# except vk_api.AuthorizationError as error_msg:
#     print(error_msg)

upload = vk_api.VkUpload(vk_session)
upload.story(
    'balteR3.png',
    'photo',
    group_id='178073199')
