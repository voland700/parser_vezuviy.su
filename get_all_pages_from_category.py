from GetContent import GetContent



url= input("Укажите ссылку на страницу категории товара на сайта vezuviy.su: ")

#url = "https://vezuviy.su/novinki/"
#url = "https://vezuviy.su/otopitelnoe-oborudovanie/otopitelnye-kotly/"
#url = "https://vezuviy.su/gotovim-na-vezuvii-ru/"
content = GetContent()

notFlattenList = []
productsLinks = []
data = []
amount = 0
missingCount = 0
missing = []



breadcrumbsLinks = content.getBreadcrumbs(url)
if len(breadcrumbsLinks)>0:
    for breadcrumbLink in breadcrumbsLinks:
        try:
            onePage = content.getLinksOnePage(breadcrumbLink)
            notFlattenList.append(onePage)
        except:
            pass

if len(notFlattenList)>0:
    for oneList in notFlattenList:
        for productlink in oneList:
            productsLinks.append(productlink)


print('*********** ----------- ***********')

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













print(productsLinks)