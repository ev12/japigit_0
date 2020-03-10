#!/usr/bin/python3
import urllib.request,json

def getStockData(stockSymbol):
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
    apikey = '&apikey=GUV66RNA99LL56XW'
    fullUrl = url+stockSymbol+apikey
    connection = urllib.request.urlopen(fullUrl)
    responseString = connection.read().decode()
    dictionary = json.loads(responseString)

    print (responseString)
    return dictionary

def main():
    file = open('japi.out','w')
    while True:
        stockSymbol = input("Enter Stock Symbol or quit to exit: ").upper()
        if stockSymbol != 'QUIT':
            stockInfo = getStockData(stockSymbol)
            stockPrice = stockInfo['Global Quote']['05. price']
            stockPrice = float(stockPrice)
            output = 'The current price of '+stockSymbol+' is: '+'${:,.2f}'.format(stockPrice)+'\n'

            file.write(output)

        else:
            print('Stock Quotes retrieved successfully!')
            print('Goodbye!')
            break
main()
