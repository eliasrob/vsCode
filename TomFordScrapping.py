import requests, bs4

res = requests.get('https://www.smartbuyglasses.com/designer-sunglasses/Tom-Ford/')

soup = bs4.BeautifulSoup(res.text, 'html.parser')



def getGlassesContainer:
    # find each sunglass container
    containers = soup.findAll("div", {"class":"proCell proCell_click grid-pro-cell"})

    container = containers[0]
    containerInfo = container.find("li", {"class":"proInfoN"})
    productBrand = containerInfo.a.p.text
    productName = containerInfo.a.span.text


    # get the prices , usually there's 2 prices, original and doscounted
    productPrices = containerInfo.find("p", {"class":"discount-cnt"}).text

    # always get the last price, specially if there is an original price 
    # and  discounted price, split the dollarsign and take the last item
    productFinalPrice = productPrices.split('$')[-1:]

    createGlassesCSV(productBrand, productName, productFinalPrice)




def createGlassesCSV(brand, name, price):
    CVSName = brand+" List of Items"+".csv"
    open(CVSName, "wb")