from GetContent import GetContent

content = GetContent()
url= input("Укажите ссылку на страницу товара на сайта vezuviy.su: ")
item = content.getItem(url)
data = []
data.append(item)
print('Старт парсинга')
if bool(data):
    content.getExel(data)
    print('Данные товара успешно получены')
else:
    print('Не получается получить данные товара. Проверкти указанную ссылку')
    exit()




