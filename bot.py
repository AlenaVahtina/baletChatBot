# coding=utf-8
import vk_api
import re
from connect import *

vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if re.match(u'.*(Привет|Добрый день|Здравствуйте|Добрый вечер|Hi).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message="Еще раз привет. Я бот. С помощью кнопок внизу ты можешь узнать рассписание, стоимость,"
                            " адрес или время проведения занятий. Если у тебя есть другие вопросы, можешь написать,"
                            "и в скором времеи кто-нибудь и администараторов тебе обязательно ответит!")
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message="Если снизу нет кнопок навигации, то чтобы узнать информайию вы пожете отправить сообщение "
                            "\n 1-Адрес проведения занятий"
                            "\n 2-Стоимость занятий"
                            "\n 3-Контакты"
                            "\n 4-Расписание")
        if re.match(u'.*(Расписание|Когда|сколько|4).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    attachment="photo-178073199_456239019",
                    message=plan)
        if re.match(u'.*(Адрес|Где|Место|1).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    lat=lat,
                    long=long,
                    message=place)
        if re.match(u'.*(Стоимость занятий|Цена|Сколько|2|Стоимость|Оплата|Запатить).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=price)
        if re.match(u'.*(Контакты|3|Кто).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=contacts)
        if re.match(u'.*(Спасибо|пока).*', event.text, flags=re.IGNORECASE):
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message="Надеюсь смог помочь. Обращайся еще!")
        if event.text == u'admin/admin':
            if event.from_user:
                vk.messages.send(
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

