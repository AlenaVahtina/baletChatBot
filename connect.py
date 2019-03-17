import vk_api
# сообщество
token = "c92688cab7bb7e6c3840dd82483adc3b19698f0d2ccd6433b61832136b48cd6328eae24f6662320f9fce9"
admin_user_id=39002348
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
