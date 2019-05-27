# coding=utf-8
import vk_api
import re
from connect import *


admin_ts = None


def user_command(mached_str, event, admin_only, function):
    global admin_ts
    if re.match(mached_str, event.text, flags=re.IGNORECASE):
        if admin_only:
            if not admin_ts or event.user_id != info_class.admin_user_id:
                return
        if event.from_user:
            function(event)


def function_welcome(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message="Еще раз привет. Я бот. С помощью кнопок внизу ты можешь узнать расписание, стоимость, "
                "адрес или время проведения занятий. Если у тебя есть другие вопросы, можешь написать и в "
                "скором времени кто-нибудь и администраторов тебе обязательно ответит! ")
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message="Если снизу нет кнопок навигации, то, чтобы узнать информацию вы можете отправить сообщение "
                "\n 1-Адрес проведения занятий \n 2-Стоимость занятий \n 3-Контакты \n 4-Расписание \n "
                "5-Возраст занимающихся \n 6-Индивидуальные занятия ")


def function_table(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        attachment=info_class.plan_picture,
        message=info_class.plan)


def function_adress(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        lat=info_class.lat,
        long=info_class.long,
        message=info_class.place)


def function_price(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message=info_class.price)


def function_contacts(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message=info_class.contacts)


def function_age(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message="Для детских групп проходят отдельные занятия. Возраст начала занятий от 11 лет.")


def function_personal(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message="Про частные занятия можно узнать по тел.:")


def function_bye(event):
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message="Надеюсь смог помочь. Обращайся еще!")


def function_admin_login(event):
    global admin_ts
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message='Привет,Настя! Что желаешь поменять?')
    admin_ts = longpoll.ts


def function_admin_table(event):
    global admin_ts
    info_class.plan = event.text.split(':')[1]
    info_class.plan_picture = None
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message='Будет исполнено',
        ts=admin_ts)


def function_admin_place(event):
    global admin_ts
    info_class.place = event.text.split(':')[1]
    info_class.lat = None
    info_class.long = None
    vk.messages.send(
        user_id=info_class.admin_user_id,
        random_id=event.random_id,
        message='Будет исполнено',
        ts=admin_ts)


def function_admin_price(event):
    global admin_ts
    info_class.price = event.text.split(':')[1]
    vk.messages.send(
        user_id=info_class.admin_user_id,
        random_id=event.random_id,
        message='Будет исполнено',
        ts=admin_ts)


def function_admin_contacts(event):
    global admin_ts
    info_class.contacts = event.text.split(':')[1]
    vk.messages.send(
        user_id=info_class.admin_user_id,
        random_id=event.random_id,
        message='Будет исполнено',
        ts=admin_ts)


vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        user_command(u'.*(Привет|Добрый день|Здравствуйте|Добрый вечер|Hi|Хай).*', event, False, function_welcome)
        user_command(u'.*(Расписание|Когда|сколько|4).*', event, False, function_table)
        user_command(u'.*(Адрес|Где|Место|1).*', event, False, function_adress)
        user_command(u'.*(Стоимость занятий|Цена|Сколько|2|Стоимость|Оплата|Запатить).*', event, False, function_price)
        user_command(u'.*(Контакты|3|Кто).*', event, False, function_contacts)
        user_command(u'.*(Возраст|5|Дети|Возрастные категории).*', event, False, function_age)
        user_command(u'.*(Индивидуальные|6|Частные|индивидуально).*', event, False, function_personal)
        user_command(u'.*(Спасибо|пока).*', event, False, function_bye)
        user_command(u'admin/admin', event, False, function_admin_login)
        user_command(u'^Поменять расписание:.*', event, True, function_admin_table)
        user_command(u'^Поменять адрес:.*', event, True, function_admin_place)
        user_command(u'^Поменять стоимость:.*', event, True, function_admin_price)
        user_command(u'^Поменять контакты:.*', event, True, function_admin_contacts)
