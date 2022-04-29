from flask import Flask 
from flask import render_template,request 
import nltk 
import numpy 
import re 
import string  
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords 
from sklearn.naive_bayes import MultinomialNB from sklearn.feature_extraction.text import TfidfVectorizer 
import joblib 
from nltk.corpus import stopwords 
import tweepy 
def sentiment(ss): 
temp = re.sub('[^a-zA-Z]'," ",ss)
temp = re.sub('((www.[^s]+)|(https?://[^s]+)|(@[^s]+))',' ',ss) temp = re.sub('[0-9]+', '', ss) 
temp = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","  ",ss) 
temp = temp.lower() 
temp = temp.split() 
fs = temp 
s = [ps.lemmatize(word) for word in fs if not word in  stop_words] 
s = " ".join(s) 
l = [s] 
Xs = cv.transform(l) 
Xs 
return model.predict(Xs) 
stop_words = set(stopwords.words('english')) 
ps = nltk.WordNetLemmatizer() 
cv = joblib.load('count_vectorrization') 
model = joblib.load('final_model') 
app = Flask(__name__) 
@app.route('/',methods = ['GET','POST']) 
def home(): 
op = 1
if request.method == 'GET': 
return render_template('home.html',op = op) 
elif request.method == 'POST': 
query = request.form.get('query') 
api_key = 'KhRbm3pxnLzTJ0hkZEH7fJ0M5' 
api_key_secret =  
'1JIZBnOmG9hHQ36SzwNa3rLRIJ6Na19y5jbRbKrsOUEkHc1vU z' 
access_token = '2522843929- 
ALcPeobuJLXZ380cCewKOYDRce9OUyLZhiwjyIM' access_token_secret =  
'l18nvqC6X6zG8ZFHhst0zdlkZ4P7M3jMxSEhPIUKLHeDc' 
auth = tweepy.OAuthHandler(api_key,api_key_secret) auth.set_access_token(access_token,access_token_secret) api = tweepy.API(auth) 
cursor = tweepy.Cursor(api.search_tweets, q =query+'- filter:retweets',count = 1000,tweet_mode =  
'extended',result_type='mixed',lang='en').items(300) 
tweets = [] 
for i in cursor: 
tweets.append(i.full_text) 
sentiments = []
pos_sentiment = [] 
neg_sentiment = [] 
for tweet in tweets: 
sentiments.append(sentiment(tweet)) 
pos = neg = 0 
for i in range(len(sentiments)): 
if(sentiments[i] == [0]): 
neg+=1 
neg_sentiment.append(tweets[i]) 
else: 
pos+=1 
pos_sentiment.append(tweets[i]) 
#print(sentiments[i],tweets[i]) 
return render_template('home.html',op = op,query =  query,pos = pos, neg=  
neg,pt=pos_sentiment,nt=neg_sentiment,pl=len(pos_sentiment),n l=len(neg_sentiment)) 
@app.route('/about') 
def about(): 
op = 2 
return render_template('about.html',op = op) 
if __name__ == '__main__': 
app.run()
