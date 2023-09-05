from GetContent import GetContent

list = """
https://vezuviy.su/gotovim-na-vezuvii-ru/chugunnyy-fantastic-grill-vezuviy-o-1000-ot-shefa/
https://vezuviy.su/gotovim-na-vezuvii-ru/kostrovye-chashi/kostrovye-chashi-iz-metalla/kostrovaya-chasha-7-russkiy-les/
https://vezuviy.su/gotovim-na-vezuvii-ru/nabor-dlya-barbekyu-gotovim-na-vezuvii-3-predmeta-wb028/
https://vezuviy.su/gotovim-na-vezuvii-ru/chugunnaya-kostrovaya-chasha-fantastic-o-1000-prestizh/
https://vezuviy.su/otopitelnoe-oborudovanie/otopitelnye-kotly/tverdotoplivnyy-kotel-vezuviy-elbrus-14/
"""

content = GetContent()


productsLinks = []
data = []
amount = 0
missingCount = 0
missing = []


lines = list.splitlines()
for line in lines:
    if bool(line):
        productsLinks.append(line.strip())

if len(productsLinks) > 0:
    print(f"Получено {len(productsLinks)} ссылок на товары. Приступаю к парсингу контента")
    for link in productsLinks:
        try:
            item = content.getItem(link)
            data.append(item)
            amount+=1
        except:
            missingCount += 1
            missing.append(link)

content.getExel(data)

print('**************** --- END! --- ***************')
if len(productsLinks) == amount:
    print('Успешно получен контент '+str(amount)+" товаров")
elif amount > 0 and missingCount > 0:
    print('Успешно получен контент ' + str(amount) + " товаров")
    print('Не получены товары по ' + str(missingCount) + "ссылкам:")
    for missingLink in missing:
        print(missingLink)
elif amount == 0:
    print('Не удачный парсинг контента, неудалось получить данные товаров')