from getDistance import *
from test import sentiment_results
import matplotlib.pyplot as plt

def create_figure():
    countries_names = get_countries()
    for country in countries_names:
        if country == "Kuala Lumpur":
            continue
        labels = ['Neural Words', 'Negative Words', 'Positive Words']
        frequency = [
            sentiment_results[country]["neutral_pct"],
            sentiment_results[country]["negative_pct"],
            sentiment_results[country]["positive_pct"],
        ]
        color = ['lightcyan', 'powderblue', '#7df293']
        explode = (0.1, 0, 0.05)
        plt.pie(frequency, labels=labels, colors=color,
                startangle=90, explode=explode, autopct='%0.2f%%', shadow=True)
        plt.axis('equal')
        plt.title('Sentiment Analysis for ' + country)
        plt.savefig("wordcount/" + country + ".png")
        plt.clf()


create_figure()

