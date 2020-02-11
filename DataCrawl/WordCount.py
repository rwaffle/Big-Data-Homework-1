import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import collections

hashtagList = []
#add in all hashtags above with the hashtag remove so we can remove that word from the list of counted words
tok = WordPunctTokenizer()
movieTitleWordsList = []
stop_words = set(stopwords.words('english'))
for z in hashtagList:
    stop_words.append(hashtagList)
movieDictionary = {}

data = pd.read_csv('C:/Users/elffa/Desktop/NewTweets/TestDates.csv', sep = '|')
movieDictionary = {col: list(data[col]) for col in data.columns}
for movie in movieDictionary:
    movieLower = movie.lower()
    title = tok.tokenize(movieLower)
    for m in title:
        movieTitleWordsList.append(m)
    countDict = {}
    tweetFile = 'C:/Users/elffa/Desktop/NewTweets/' + movie + '.xlsx'
    movieDF = pd.read_excel(tweetFile) #Doesn't seem to want to read the csv files, so if it doesn't work, they should be saved as .xlsx
    movieDF['date'] = pd.to_datetime(movieDF['date'], format = '%Y-%m-%d', errors = 'coerce')
    movieDF['date'] = movieDF['date'].dt.date
    movieDF['date'] = pd.to_datetime(movieDF['date'], format = '%Y-%m-%d')
    movieDF = movieDF.dropna()
    movieDF = movieDF.set_index(['date'])
    for a in movieDictionary[movie]:
        wordsList = []
        finalWordsList = []
        dailytweets = movieDF.loc[a]
        dailytweets = dailytweets['cleaned_tweet'].tolist()
        for i in dailytweets:
            i = str(i)
            word = i.lower().split()
            for w in word:
                wordsList.append(w)
        for w in wordsList:
            if w not in movieTitleWordsList and w not in stop_words:
                finalWordsList.append(w)
        count = collections.Counter(finalWordsList)
        countDict[a] = count
        countDF = pd.DataFrame.from_dict(countDict)
    countDF = countDF.sort_values(countDF.columns[0], ascending = False)
    countDF.to_csv('TG.csv', sep = '|')

        
