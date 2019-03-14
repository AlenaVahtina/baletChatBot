# coding=utf-8
from vk_api.upload import VkUpload
from connect import *

upload_url = None

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

stories = VkUpload.story(vk_session)

upload_url = stories.getPhotoUploadServer(add_to_news=1)



