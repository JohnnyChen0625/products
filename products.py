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

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品，價格\n')
	for p in products:
		f.write(p[0]) + ',' + p[1] + '\n')
        # 使用逗點會在Excel中換格 在記事本也會做換行的功能
        
