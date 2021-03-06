
from getDistance import countries
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json as JSON


# test = open("news_feed/Brunei.txt","r")
# text = test.read().lower();
# fullwordlist = obo.stripNonAlphaNum(text);
# wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
#
# dictionary = obo.wordListToFreqDict(wordlist)
# sorteddict = obo.sortFreqDict(dictionary)
# for s in sorteddict: print(str(s))

tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+\'?\w*')
pos_neg_words = {}
sentiment_results = {}
text = open("stopword.txt","r")
stopwords = text.read().lower();

def get_pos_neg_words():
    pos_file = open('pos.txt', 'r', encoding="utf-8",
                    errors="ignore").readlines()
    pos = []
    for i in pos_file:
        pos += tokenizer.tokenize(i)

    for w in pos:
        pos_neg_words[w] = 'positive'

    neg_file = open('neg.txt', 'r', encoding="utf-8",
                    errors="ignore").readlines()
    neg = []
    for i in neg_file:
        neg += tokenizer.tokenize(i)

    for w1 in neg:
        pos_neg_words[w1] = 'negative'


get_pos_neg_words()

def get_word_counts():
    for country in countries:
        if country == "Kuala Lumpur":
            continue
        text = open("news_feed/" + country + ".txt",
                    encoding="utf-8", errors="ignore").readlines()
        result = {
            'positive': 0,
            'negative': 0,
            'neutral': 0,
            'positive_pct': 0,
            'negative_pct': 0,
            'neutral_pct': 0,
            'sentiment': 0,
            'words': {}
        }
        for i in text:
            word = tokenizer.tokenize(i)
            for w in word:
                w_base = w.lower()
                if w_base in stopwords or len(w_base) <= 2:
                    continue
                # word count
                if w_base in result["words"]:
                    result["words"][w_base] += 1
                else:
                    result["words"][w_base] = 1
                # sentiment analysis
                if w_base in pos_neg_words:
                    result[pos_neg_words[w_base]] += 1
                else:
                    result["neutral"] += 1
            # calculate percentage
            total_words = result["positive"] + \
                result["negative"] + result["neutral"]
            result["positive_pct"] = round(
                (result["positive"]/total_words) * 100, 2)
            result["negative_pct"] = round(
                (result["negative"]/total_words) * 100, 2)
            result["neutral_pct"] = round(
                (result["neutral"]/total_words) * 100, 2)
            if result["positive"] != 0 and result["negative"] != 0:
                result["sentiment"] = round((result["positive"] -
                                             result["negative"]) / (result["positive"] + result["negative"]) * 100, 2)
        sentiment_results[country] = result

get_word_counts()

if __name__ == '__main__':
    outfile = open('test.txt', 'w')
    print(sentiment_results, file=outfile)
    s= open('test.txt', 'r').read()
    s = s.replace('\'', '\"')

    outfile.close()
    outfile = open('test.txt','w')
    outfile.write(s)
    outfile.close()


    # with open ("wordcount/WordCount.json", "r") as read:
    #     data = JSON.load(read)
        # print(data['Singapore']['positive'])
    # list = []

    # dict = {}

    # for i in range(len(data)):
        # dict[data[i]]=data[i]['sentimental']
        # print(data[i])
    # print(dict)

