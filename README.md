# Marvel VS DC 
--------------
 

<p align="center">
  <img src=  https://user-images.githubusercontent.com/52492864/150648002-b34191a1-c001-49d9-bb41-67c4c8508153.jpg alt="Sublime's custom image"/>
</p>


Description
-----------

The main objectif of this project is to conduct some analysis on the european and american population on how they react on MCU ( Marvel Cinematic Universe ) & DC.


Getting started
-------------
this repository includs: 

* 01- Data Collections: this jupyter notebook include functions to help you to collect data using tweepy API using both struming mode and cursor.
* 02- Data Transmission & Preparation: this jupyter notebook include EDA after and before the prepartion of data, that help us to create a Pipeline to preprocess our data. 
* 03- Sentiment Analysis: we performed some sentiment analysis on DC & Marvels heros in both europe and USA.
* 04- Topic modeling: we have built some dataset about marvel and DC, we would like to know what kinf of topics takle these movies.


Pipeline
-----------
![image](https://user-images.githubusercontent.com/52492864/150654022-f27b0244-5872-4fd6-a3f0-6ac62e2a1550.png)



Requirements
-----------
```python
 !pip install tweepy==3.9.0
 !conda install -c conda-forge wordcloud 
 !pip install textblob**
 !pip install nltk 
 !pip install bokeh 
```


Example to run: 
-----------
``` 
bokeh serve --show .\bokeh_app.py
```

Some results in Bokeh application:
-----------
