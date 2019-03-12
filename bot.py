# coding=utf-8
import vk_api

# сообщество
token = "test"
vk_session = vk_api.VkApi(token=token)
plan = 'Занимаемся Вт, Чт и Пт с 19:30. Занятия идут 1.5 часа'
place = 'Адрес бла-бла'
lat=55.653663
long=37.620861
price = 'Еще не решено'
contacts = 'Вот прямо так и сказала'



try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
admin_ts=0
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == u'Расписание':
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    attachment="photo-178073199_456239018",
                    message=plan)
        if event.text == u'Адрес проведения занятий':
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    lat=lat,
                    long=long,
                    message=place)
        if event.text == u'Стоимость занятий':
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=price)
        if event.text == u'Контакты':
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=contacts)
        if event.text == u'admin/admin':
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Привет,Настя! Что желаешь поменять?')
                print (longpoll.ts)
                admin_ts = longpoll.ts
        if event.text.split(':')[0] == u'Поменять расписание':
            if not admin_ts or event.user_id != test:
                continue
            if event.from_user:
                plan = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять адрес':
            if not admin_ts or event.user_id != test:
                continue
            if event.from_user:
                place = event.text.split(':')[1]
                lat = None
                long = None
                vk.messages.send(  # Отправляем сообщение
                    user_id=test,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять стоимость':
            if not admin_ts or event.user_id != test:
                continue
            if event.from_user:
                price = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=test,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять контакты':
            if not admin_ts or event.user_id != test:
                continue
            if event.from_user:
                contacts = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=test,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)

