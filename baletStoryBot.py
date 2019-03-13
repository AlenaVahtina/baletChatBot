# coding=utf-8

import vk_api
from vk_api.upload import VkUpload

token = "d8cc20fa7265bf8db6c873e363f4cc2dbb53eb555a1bf457be9642faaba0f024e0f2fc4c65030fa55210a"
vk_session = vk_api.VkApi(token=token)
plan = 'Занимаемся Вт, Чт и Пт с 19:30. Занятия идут 1.5 часа'
place = 'Адрес бла-бла'
price = 'Еще не решено'
contacts = 'Вот прямо так и сказала'
upload_url = None

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

stories = VkUpload.story(vk_session)

upload_url = stories.getPhotoUploadServer(add_to_news=1)



