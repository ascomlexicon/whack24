import pandas as pd
import matplotlib.pyplot as plt
from preparation import create_dataframe, clean_dataframe
import query as q
import numpy as np
import benchmark as bench

seasonColours = ["red", "yellow", "green", "blue"]
donutColors = ["green", "red"]
barWidth = 0.25


def main():
    df = clean_dataframe(create_dataframe('assets/dataset.csv'))

    graphShotsOnTargBreakdown(df)



#plots graph of total goals per season. Requires dataframe containing seasons and goals
#tip : use getGoalsScoredBySeason query in query.py
def graphGoalsBySeason(dataframe):
    agg_goals = aggregateSum(dataframe, 'season_name')
    agg_goals_list = agg_goals['goals_scored'].tolist()

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_goals_list, color=seasonColours)

    plt.title("Shots per Season")

    plt.show()


#plots graph of total shots per season. Requires dataframe containing seasons and shots
#tip : use getShotsPerSeason query in query.py
def graphShotsPerSeason(dataframe):

    agg_shots = aggregateSum(dataframe, 'season_name')
    agg_shots_list = agg_shots['shots'].tolist()

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_shots_list, color=seasonColours)

    plt.title("Shots per Season")

    plt.show()

#plots graph of total shots on target per season. Requires dataframe containing seasons and shots on target
#tip : use getShotsTargPerSeason query in query.py
def graphShotsTargPerSeason(dataframe):

    agg_shots = aggregateSum(dataframe, 'season_name')
    agg_shots_list = agg_shots['shots_on_target'].tolist()

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_shots_list, color=seasonColours)

    plt.title("Shots on Target per Season")

    plt.show()

#plots graph of goals conceded per season. Requires dataframe containing seasons and shots on target
#tip : use getGoalsConcPerSeason query in query.py
def graphGoalsConcededPerSeason(dataframe):

    agg_goals = aggregateSum(dataframe, 'season_name')
    agg_goals_list = agg_goals['goals_conceded']

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_goals_list, color=seasonColours)

    plt.title("Goals Conceded per Season")

    plt.show()

#plots graph of total passes per season. Requires dataframe containing seasons and shots on target
#tip : use getPassesBySeason query in query.py
def graphPassesPerSeason(dataframe):

    agg_passes = aggregateSum(dataframe, 'season_name')
    agg_passes_list = agg_passes['passes'].tolist()

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_passes_list, color=seasonColours)

    plt.title("Number of Passes per Season")

    plt.show()

#plots graph of total completed passes into box per season. Requires dataframe containing seasons and shots on target
#tip : use getPassesInBoxBySeason query in query.py
def graphBoxPassesPerSeason(dataframe):

    agg_passes = aggregateSum(dataframe, 'season_name')
    agg_passes_list = agg_passes['completed_passes_into_the_box'].tolist()
    
    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_passes_list, color=seasonColours)

    plt.title("Passes Into Box per Season")

    plt.show()

#plots graph of total completed passes into box per season. Requires dataframe containing seasons and shots on target
#tip : use getTacklesPerSeason query in query.py
def graphTacklesPerSeason(dataframe):

    agg_tackles = aggregateSum(dataframe, 'season_name')
    agg_tackles_list = agg_tackles['tackles'].tolist()

    fig, ax = plt.subplots()
    ax.bar(formatSeasons(dataframe), agg_tackles_list, color=seasonColours)

    plt.title("Tackles per Season")

    plt.show()

#plots graph of match outcomes per season. Requires dataframe containing seasons and shots on target
#tip : use graphWinStats query in query.py
def graphWinStats(dataframe):

    agg_outcomes = getWinStats(dataframe)
    outcome_types = ['lost', 'won', 'draw']
    bar_colours = ['red', 'green', 'yellow']

    fig, ax = plt.subplots()
    ax.bar(outcome_types, agg_outcomes, label=outcome_types, color=bar_colours)

    plt.title("Overall Match Outcomes")

    plt.show()

#returns a donut chart of the goals scored and goals conceded per match
def donutGoalsPerMatch(dataframe, matchid):
    goals = list(q.getGoalStatsFromMatch(dataframe, matchid))
    label = ['Goals Scored', 'Goals Conceded']

    print(goals)

    plt.pie(goals, labels=label)
    circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(circle)  

    plt.title("Goals Scored vs Goals Conceded") 

    plt.show()

#returns a donut chart of the shots stats
def donutShotsPerMatch(dataframe, matchid):
    shots = list(q.getShotStatsFromMatch(dataframe, matchid))
    shots[0] = shots[0] - shots[1]
    label = [shots[0], shots[1]]

    print(shots)

    plt.pie(shots, labels=label, colors=donutColors)
    circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(circle)   

    plt.title("Shots Taken vs Shots Missed")

    plt.show()


#returns a donut chart of the opposition shots stats
def donutOppShotsPerMatch(dataframe, matchid):
    shots = list(q.getShotStatsFromMatch(dataframe, matchid))
    shots[0] = shots[0] - shots[1]
    label = [shots[0], shots[1]]

    print(shots)

    plt.pie(shots, labels=label, colors=donutColors)
    circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(circle)   

    plt.title("Opposition Shots Taken vs Opposition Shots Missed")

    plt.show()


#plots grouped bar chart of min, median and max goals for a particular season
def graphGoalsBreakdown(dataframe):

    agg_goal = aggregateSum(dataframe, 'season_name')            #aggregate goals scored by season
    agg_goal_total = tuple(agg_goal['goals_scored'].tolist())

    labels = tuple(getSeasons(dataframe))
    goal_data = {}
    makeDictionary(dataframe, goal_data)

    fig, ax = plt.subplots(layout='constrained')

    ax.set_ylabel("Num. Goals")
    formatPlot(ax, goal_data, labels, formatSeasons(dataframe),"Breakdown of Goals per Season", "Num. Goals")

    plt.show()

#plots grouped bar chart of min, median and max shots on target for a particular season
def graphShotsOnTargBreakdown(dataframe):

    agg_shotTarg = aggregateSum(dataframe, 'season_name')
    agg_shotTarg_total = tuple(agg_shotTarg['goals_scored'].tolist())

    labels = tuple(getSeasons(dataframe))
    shotTarg_data = {}
    makeDictionary(dataframe, shotTarg_data)

    fig, ax = plt.subplots(layout='constrained')

    ax.set_ylabel("Num. Goals")
    formatPlot(ax, shotTarg_data, labels, formatSeasons(dataframe),"Breakdown of Shots on Target per Season", "Num. Shots on Targ.")

    plt.show()



def dateIntToString(dates):
    string_date = []
    for date in dates:
        addDate = str(date)[:2] + "/" + str(date)[2:]
        string_date.append(addDate)
    return string_date

def aggregateSum(dataframe, fieldname):
    return dataframe.groupby([fieldname]).sum()

def convertColumnNumpy(dataframe):
    return dataframe.to_numpy()

#formats season values into nice strings
def formatSeasons(dataframe):
    return dateIntToString(dataframe['season_name'].unique())

def getSeasons(dataframe):
    return (dataframe['season_name'].unique()).tolist()

def getOutcomes(dataframe):
    return dataframe['match_outcome'].unique()

def getWinStats(dataframe):
    num_wins = (dataframe['match_outcome'].value_counts()['won'])
    num_losses = (dataframe['match_outcome'].value_counts()['lost'])
    num_draws = (dataframe['match_outcome'].value_counts()['draw'])

    return [num_wins, num_losses, num_draws]

def makeDictionary(dataframe, dictionary):
    min_arr = []
    mean_arr = []
    max_arr = []
    for season in getSeasons(dataframe):
        ma, mean, mi = bench.benchmark_range_for_season(dataframe, 'goals_scored', season)
        min_arr.append(mi)
        mean_arr.append(mean)
        max_arr.append(ma)

    dictionary["Min"] = tuple(min_arr)
    dictionary["Mean"] = tuple(mean_arr)
    dictionary["Max"] = tuple(max_arr)

def formatPlot(plot, dictionary, labels, labelNames, title, ylabel):
    x = np.arange(len(labels))
    width = 0.25
    multiplier = 0
    i=0
    plot.set_title(title)
    plot.set_ylabel(ylabel)
    plot.set_xticks(x + width, labels)
    for attribute, measurement in dictionary.items():
        offset = width * multiplier
        rects = plot.bar(x + offset, measurement, width, label=labelNames[i])
        plot.bar_label(rects, padding=3)
        multiplier += 1
        i += 1

def setPlotLabels(ax, title, ylabel):
    ax.set_title = title
    ax.set_ylabel = ylabel

if __name__ == "__main__":
    main()