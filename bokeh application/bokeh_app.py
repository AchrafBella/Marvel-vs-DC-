from bokeh.layouts import layout, column
from sentiments import sentiments_analysis, bokeh_polarity, bokeh_pie_char, pol, sub, hist_plot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc
import pandas as pd

# importing data
marvel_usa = pd.read_pickle('marvel_data_usa.txt_df.pkl')
marvel_europe = pd.read_pickle('marvel_data_europe.txt_df.pkl')
DC_usa = pd.read_pickle('DC_data_usa.txt_df.pkl')
DC_europe = pd.read_pickle('DC_data_europe.txt_df.pkl')

for df in [marvel_europe, marvel_usa, DC_europe, DC_usa]:
    df['polarity'] = df['cleaned_tweet'].apply(pol)
    df['subjectivity'] = df['cleaned_tweet'].apply(sub)
    pass
pass

# pie chart plots
p1 = bokeh_pie_char(sentiments_analysis(marvel_europe.cleaned_tweet),'marvel', 'europe')
p2 = bokeh_pie_char(sentiments_analysis(marvel_usa.cleaned_tweet), 'marvel', 'USA')
p3 = bokeh_pie_char(sentiments_analysis(DC_europe.cleaned_tweet),  'DC', 'marvel')
p4 = bokeh_pie_char(sentiments_analysis(DC_usa.cleaned_tweet),'DC', 'USA')

# scatter plots
p5 = bokeh_polarity(marvel_europe)
p6 = bokeh_polarity(marvel_usa)
p7 = bokeh_polarity(DC_europe)
p8 = bokeh_polarity(DC_usa)

# hist plots
p9 = hist_plot(marvel_europe, 'marvel', 'europe')
p10 = hist_plot(marvel_usa, 'marvel', 'USA')
p11 = hist_plot(DC_europe, 'DC', 'marvel')
p12 = hist_plot(DC_usa, 'DC', 'USA')

# layout
l1 = layout([column([p1, p2, p3, p4 ])], sizing_mode='fixed')
l2 = layout([column([ p5, p6, p7, p8])], sizing_mode='fixed')
l3 = layout([column([p9, p10, p11, p12 ])], sizing_mode='fixed')

tab1 = Panel(child=l1,title="Sentiment Analysis on Marvel VS DC in europe & USA")
tab2 = Panel(child=l2,title="polarity scatter plot on Marvel VS DC in europe & USA")
tab3 = Panel(child=l3,title="polarity histogram on marvel vs DC in europe & USA")

tabs = Tabs(tabs=[ tab1, tab2, tab3])

curdoc().add_root(tabs)
