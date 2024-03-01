import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from calendar import month_name
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)



# Clean data
df = df[(df["value"]<df["value"].quantile(0.975))
& (df["value"]>df["value"].quantile(0.025) )]


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots()
    axes.plot(df, 'r')
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    
    #print(df_bar.columns)
    # Draw bar plot
    
    months_names = month_name[1:]
    #print(df_bar.head())
    #months = pd.DatetimeIndex(df_bar["date"]).month
    #print(months_names)
    df_bar['months'] = pd.Categorical(df_bar.index.strftime('%B'), categories = months_names, ordered=True)
    dfp = pd.pivot_table(data=df_bar, index=df_bar.index.year, columns='months', values='value')
    #print(dfp.head())
    fig, ax = plt.subplots()
    dfp.plot(kind='bar',  ylabel='Average Page Views', xlabel='Years', ax=ax)
    ax.legend()
    plt.tight_layout()
    #x = np.arange(len(months))
    #width = 0.25
    #y = df_bar["value"].values

    
    # fig, axes = plt.subplots()
    
    # axes.bar(dfp["date"], dfp.values, width=0.5, color="orange")
    # axes.set_title("Yearly freeCodeCamp Forum Page Views 5/2016-12/2019")
    #ax.set_xlabel("Years ")
    # axes.set_ylabel("Average Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
