from django.shortcuts import render
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from test_app.form import MarketDataForm
from test_app.models import MarketData


# так быть не должно, логика должна быть отдельно, это место только для отображения
# для уточнения этого вопроса посмотри тот видос про это дело
def get_yf_data(name):
    ticker = yf.Ticker(name)
    hist = ticker.history(interval="1d", start="2020-01-01")

    time = [str(row[0]) for row in hist.itertuples(index=True)]
    open_value = [row['Open'] for index, row in hist.iterrows()]
    close_value = [row['Close'] for index, row in hist.iterrows()]

    data = list(map(list, zip(time, open_value, close_value)))
    [i.insert(0, name) for i in data]
    return data


def create_data(data):
    # print(*data, sep='\n')
    for i in data:
        x = MarketData(ticker=i[0], data=i[1], open_value=i[2], close_value=i[3])
        x.save()


def index_page(request):
    source = None
    context = {'title': "testTitle", 'form': MarketDataForm()}

    if request.method == 'POST':
        if 'enter' in request.POST:
            print(request.POST)
            all_data = get_yf_data(request.POST['ticker'])
            create_data(all_data)

            data_point = [i[1] for i in all_data]
            open_value = [i[2] for i in all_data]
            close_value = [i[3] for i in all_data]

            plt.plot(open_value)
            plt.plot(close_value)
            # plt.show()
            plt.savefig(f'static/test4.png')
            plt.close()

    return render(request, "index.html", context)



