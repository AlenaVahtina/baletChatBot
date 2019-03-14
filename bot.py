# coding=utf-8
import vk_api
import re
from connect import *

vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text in greeting:
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message="Еще раз привет. Я бот. С помощью кнопок внизу ты можешь узнать рассписание, стоимость,"
                            " адрес или время проведения занятий. Если у тебя есть другие вопросы, можешь написать,"
                            "и в скором времеи кто-нибудь и администараторов тебе обязательно ответит!")
        if re.match(u'.*(Расписание|Когда|сколько).*', event.text, flags=re.IGNORECASE):
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
            if not admin_ts or event.user_id != admin_user_id:
                continue
            if event.from_user:
                plan = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять адрес':
            if not admin_ts or event.user_id != admin_user_id:
                continue
            if event.from_user:
                place = event.text.split(':')[1]
                lat = None
                long = None
                vk.messages.send(  # Отправляем сообщение
                    user_id=admin_user_id,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять стоимость':
            if not admin_ts or event.user_id != admin_user_id:
                continue
            if event.from_user:
                price = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=admin_user_id,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)
        if event.text.split(':')[0] == u'Поменять контакты':
            if not admin_ts or event.user_id !=admin_user_id:
                continue
            if event.from_user:
                contacts = event.text.split(':')[1]
                vk.messages.send(  # Отправляем сообщение
                    user_id=admin_user_id,
                    random_id=event.random_id,
                    message='Будет исполнено',
                    ts=admin_ts)

