import requests, xlwt
url = "https://technopoint.ru/catalog/recipe/e351231ca6161134/2020-goda/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }
r = requests.get(url, headers = headers, timeout=(10,10))
text = r.text
prev_index=0
wb = xlwt.Workbook()
ws = wb.add_sheet('Items')
ws.write(0, 1, 'Наименование')
ws.write(0, 2, 'Код товара')
ws.write(0, 3, 'Цена')
ws.write(0, 4, 'Ссылка на картинку')
for i in range(10):
    name_zone=text.find('data-role="clamped-link" data-lines-to-clamp="2"',prev_index,len(text))
    name_zone2=text.find('<',name_zone)
    name=text[name_zone+49:name_zone2]
    name=name.replace('&quot;','"')
    code_zone=text.find('span data-product-param="code">',prev_index,len(text))
    code_zone2=text.find('<',code_zone)
    code=text[code_zone+31:code_zone2]
    link_zone=text.find('<div class="product-info__title-link"><a class="ui-link" href="',prev_index,len(text))
    link_zone2=text.find('data-role="clamped-link" data-lines-to-clamp="2"',link_zone)
    prev_index=name_zone2
    link='https://technopoint.ru/'+text[link_zone+64:link_zone2-2]
    r2 = requests.get(link, headers = headers, timeout=(10,10))
    phone = r2.text
    price_zone=phone.find('data-price-value="')
    price_zone2=phone.find('>',price_zone)
    price=phone[price_zone+18:price_zone2-1]
    price=list(price)
    price.insert(-3, ' ') 
    price=''.join(price)
    pic_zone=phone.find('<div class="img ">')
    pic_zone2=phone.find('" class=',pic_zone)
    pic=phone[pic_zone+34:pic_zone2]
    ws.write(i+1, 0, str(i+1)+'.')
    ws.write(i+1, 1, name)
    ws.write(i+1, 2, code)
    ws.write(i+1, 3, price)
    ws.write(i+1, 4, pic)
wb.save('Phones.xls')

