import vk_api
# сообщество


def info_class():
    token = "test"
    admin_user_id=test
    vk_session = vk_api.VkApi(token=token)
    plan = u'Занимаемся Вт, Чт и Пт с 19:30. Занятия идут 1.5 часа'
    place = u'Адрес бла-бла'
    lat=55.653663
    long=37.620861
    price = u'Еще не решено'
    contacts = u'Вот прямо так и сказала'
    greeting = [u'Привет', u'Добрый день', u'Здравствуйте', u'Добрый вечер', u'Hi', u'привет']
    admin_ts = 0
    plan_picture = 'photo-178073199_456239019'


try:
    vk_session.auth(reauth=True,token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)




from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
