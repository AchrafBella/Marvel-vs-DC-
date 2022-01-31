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

- 01- Data Collections: this jupyter notebook include functions to help you to collect data using tweepy API using both struming mode and cursor.
- 02- Data Transmission & Preparation: this jupyter notebook include EDA after and before the prepartion of data, that help us to create a Pipeline to preprocess our data. 
- 03- Sentiment Analysis: we performed some sentiment analysis on DC & Marvels heros in both europe and USA.
- 04- Topic modeling: we have built some dataset about marvel and DC, we would like to know what kinf of topics takle these movies.
- 05- Data encryption: we used some data encryption methods to encrypt the tweets in order to send them in the web
- 06- graph analytics


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

Bar menu
![image](https://user-images.githubusercontent.com/52492864/151830784-c98ce4bb-d62d-4b8c-b04b-22f39a7aa15d.png)

- pie chart
![image](https://user-images.githubusercontent.com/52492864/151830844-f3f0413f-7ea7-4c19-82e5-0c11ad7a832a.png)

- scatter plot 
![image](https://user-images.githubusercontent.com/52492864/151830895-c6eba233-a164-46db-81e4-3983e6e9d4c2.png)


- hist plot 
![image](https://user-images.githubusercontent.com/52492864/151830923-1d71989c-26f9-4cd4-b004-0eee3b5e6ac6.png)












