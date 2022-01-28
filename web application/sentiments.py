import numpy as np
from bokeh.layouts import column, row
from textblob import TextBlob
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

from math import pi
import pandas as pd


def sentiments_analysis(tweet_data):
    """
    :param tweet_data:
    :return:
    """
    polarity = 0
    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0

    for tweet in tweet_data:
        analysis = TextBlob(tweet)
        polarity += analysis.sentiment.polarity

        if analysis.sentiment.polarity == 0:
            neutral += 0
        elif analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3:
            wpositive += 1
        elif analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6:
            positive += 1
        elif analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1:
            spositive += 1
        elif analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0:
            wnegative += 1
        elif analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3:
            negative += 1
        elif analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6:
            snegative += 1
            pass
        pass

    dict_data = {'positive': positive, 'weakly positive': wpositive, 'strong positive': spositive,
                 'negative': negative, 'weakly negative': negative, 'strong negative': snegative,
                 'neutral': neutral}
    return dict_data

pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

# function to plot the pie chart of the sentiment.
def bokeh_pie_char(sentiment_analysis, mark, zone):
    """
    :param sentiment_analysis:
    :param mark:
    :param zone:
    :return:
    """

    title = 'Pie chart of {} in {}'.format(mark, zone)
    data = pd.Series(sentiment_analysis).reset_index(name='value').rename(columns={'index': 'sentiments'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(sentiment_analysis)]
    p = figure(background_fill_color='gray', height=350, title=title, toolbar_location=None,
           tools="hover", tooltips="@sentiments: @value")
    p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='sentiments', source=data)
    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    return p

# plot the distribution of the polarity of the sentiment.
def bokeh_polarity(df):
    """

    :param df:
    :return:
    """
    p = figure(background_fill_color='gray', width=800, height=400)
    # add a circle renderer with a size, color, and alpha
    p.circle(df.polarity, df.subjectivity  , size=5, color="navy", alpha=0.5)
    p.xaxis.axis_label = '<-- Negative -------- Positive -->'
    p.yaxis.axis_label = '<-- Facts -------- Opinions -->'
    return p

# hist plots
def hist_plot(df, mark, zone):
    # Plot polarity and subjectivity histograms
    title1 = "Polarity Distribution of {} in {} ".format(mark, zone)
    title2 = "Subjectivity Distribution of {} in {} ".format(mark, zone)
    h_polar = figure(title=title1, tools="save", plot_width=500, plot_height=300)
    h_subj = figure(title=title2, tools="save", plot_width=500, plot_height=300)

    hist_polar, edges_polar = np.histogram(df['polarity'], density=True, bins=50)
    hist_subj, edges_subj = np.histogram(df['subjectivity'], density=True, bins=50)

    h_polar.quad(top=hist_polar, bottom=0, left=edges_polar[:-1], right=edges_polar[1:],
         fill_color="#036564", line_color="#033649",\
    )
    h_subj.quad(top=hist_subj, bottom=0, left=edges_subj[:-1], right=edges_subj[1:],
         fill_color="#036564", line_color="#033649",\
    )

    h_polar.legend.orientation = "top_left"
    h_polar.xaxis.axis_label = 'Polarity'
    h_polar.yaxis.axis_label = 'Dist'
    h_subj.legend.orientation = "top_left"
    h_subj.xaxis.axis_label = 'Subjectivity'
    h_subj.yaxis.axis_label = 'Dist'

    hist = column(h_polar, h_subj)

    return row(hist)
