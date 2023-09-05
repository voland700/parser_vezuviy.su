from GetContent import GetContent

#url = 'https://vezuviy.su/video/' # - Видеообзоры Везувий
#url = 'https://etna-pech.ru/video-o-produkcii/' # Видеообзоры ETNA
url = 'https://everest-pech.com/video/' # Видеообзоры Эверест

content = GetContent()
notFlattenList = []
videoPages = []
data = []
amount = 0
missingCount = 0
missing = []

breadcrumbsLinks = content.getBreadcrumbs(url)
if len(breadcrumbsLinks)>0:
    for breadcrumbLink in breadcrumbsLinks:
        try:
            onePage = content.getLinksFromOnePageOfList(breadcrumbLink)
            notFlattenList.append(onePage)
        except:
            pass

if len(notFlattenList)>0:
    for oneList in notFlattenList:
        for videoItem in oneList:
            videoPages.append(videoItem)

print('*********** ----------- ***********')

if len(videoPages) > 0:
    print(f"Получено {len(videoPages)} ссылок на страницы видеообзоров. Приступаю к парсингу контента")
    for link in videoPages:
        try:
            item = content.getVideoItem(link)
            data.append(item)
            amount+=1
            print(f"Получнео старниц: {amount}")
        except:
            missingCount += 1
            missing.append(link)
            print(f"Неудачно: {amount} страниц")

content.vieoToExel(data)

print('**************** --- END! --- ***************')

if len(videoPages) == amount:
    print('Успешно получен контент '+str(amount)+" страниц видео обзоров")
elif amount > 0 and missingCount > 0:
    print('Успешно получен контент ' + str(amount) + " страниц видео обзоров")
    print('Не получен контент по ' + str(missingCount) + "ссылкам:")
    for missingLink in missing:
        print(missingLink)
elif amount == 0:
    print('Не удачный парсинг контента, неудалось получить данные страниц')