import vk_api
# сообщество
token = "test"
admin_user_id=test
vk_session = vk_api.VkApi(token=token)
plan = 'Занимаемся Вт, Чт и Пт с 19:30. Занятия идут 1.5 часа'
place = 'Адрес бла-бла'
lat=55.653663
long=37.620861
price = 'Еще не решено'
contacts = 'Вот прямо так и сказала'
greeting = [u'Привет', u'Добрый день', u'Здравствуйте', u'Добрый вечер', u'Hi', u'привет']
admin_ts = 0

try:
    vk_session.auth(reauth=True,token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)




from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
