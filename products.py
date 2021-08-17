products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q': #quit
        break
    price  = input('請輸入商品價格:')
    # p = []
    # p.append(name)
    # p.append(price)
    # 上面三行可縮減成 p = [name, price]
    # 再來還可以縮減成下方寫法 p 換成清單內容
    products.append([name, price])
print(products)