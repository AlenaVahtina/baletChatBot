# coding=utf-8
import vk_api

# сообщество
token = "token"
vk_session = vk_api.VkApi(token=token)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == u'Расписание':
            print 'yes'
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Занимаемся Вт, Чт и Пт с 19:30. Занятия идут 1.5 часа')
        if event.text == u'Адрес проведения занятийе':
            print 'yes'
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Адрес бла-бла')
        if event.text == u'Стоимость занятий':
            print 'yes'
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Еще не решено')
        if event.text == u'Контакты':
            print 'yes'
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Вот прямо так и сказала')
