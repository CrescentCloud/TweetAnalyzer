from flask import Flask, render_template,request
import pandas as pd
import random

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze_tweet",methods = ['POST', 'GET'])
def analyze_tweet():
    text = request.form['text']
    #df = pd.read_csv("database/vaccination_all_tweets.csv")
    
    df = pd.read_csv("database/tweet.csv")

    if text!="" :
        df=df[(df["text"].str.contains(text))]
    
    rnd=random.randint(0,df.size)%13
    df=df.nlargest(rnd + 1, columns="user_favourites").tail(1)
        
    return df.to_json()

@app.route("/random_tweet",methods = ['POST', 'GET'])
def random_tweet():
    #df = pd.read_csv("database/vaccination_all_tweets.csv")
    df = pd.read_csv("database/tweet.csv")
    
    rnd=random.randint(0,df.size)%67
    df=df.nlargest(rnd + 1, columns="user_favourites").tail(5)
        
    return df.to_json()

if __name__=="__main__":
    app.run(debug=True)
