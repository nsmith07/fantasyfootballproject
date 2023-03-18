import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk



df = pd.read_csv('fantasyfootball.csv')
df_2 = pd.read_csv('fantasyfootballrank.csv')



final_df = pd.merge(df, df_2, on = "Player", how = "inner")
final_df = final_df.drop(['Fmb','FL','2PM' ,'2PP', 'DKPt' , 'FDPt' , 'VBD' , 'PosRank' , 'OvRank' , '-9999', 'Team' , 'Position', 'Min' , 'Max','Rk', 'RK', ], axis=1)
final_df = final_df.rename(columns={'Tm': 'Team', 'FantPos': 'Position', 'Yds': 'PassingYds','TD.3': 'AllTD', 'Att': 'PassAtt', 'Yds.2': 'RecYds', 'TD.2': 'RecTD','TD.1':'RushTD','TD':'PassTD','Att.1': 'RushAtt', 'Yd.1':'RushYds','PPR': 'FantasyPoints', 'AVG': 'AverageDraftPosition','Yds.1': 'RushYds'})



rb_df = final_df[final_df['Position'] == 'RB']
qb_df = final_df[final_df['Position'] == 'QB']
wr_df = final_df[final_df['Position'] == 'WR']
te_df = final_df[final_df['Position'] == 'TE']



rushing_column = ['RushAtt', 'RushYds', 'Y/A', 'RushTD', 'AllTD']
recieving_column = ['Tgt', 'Rec', 'RecYds', 'Y/R', 'RecTD']
passing_column = ['Cmp', 'PassAtt', 'PassingYds', 'PassTD', 'Int']


def transform_columns(df, new_column):
    df = df[['Player', 'Position', 'Team', 'G', 'GS','FantasyPoints', 'Age', 'AverageDraftPosition'] + new_column]
    return df

rb_df = transform_columns(rb_df, rushing_column+recieving_column)
wr_df = transform_columns(wr_df, recieving_column+rushing_column)
qb_df = transform_columns(qb_df, passing_column+rushing_column)
te_df = transform_columns(te_df, recieving_column+rushing_column)





rb_df['FantasyPoints/GM'] = rb_df['FantasyPoints']/rb_df['G']
rb_df['FantasyPoints/GM'] = rb_df['FantasyPoints/GM'].apply(lambda x: round(x, 2))

rb_df['Usage/GM'] = (rb_df['RushAtt'] + rb_df['Tgt'])/rb_df['G']
rb_df['Usage/GM'] = rb_df['Usage/GM'].apply(lambda x: round(x, 2))


wr_df['FantasyPoints/GM'] = wr_df['FantasyPoints']/wr_df['G']
wr_df['FantasyPoints/GM'] = wr_df['FantasyPoints/GM'].apply(lambda x: round(x, 2))

wr_df['Usage/GM'] = (wr_df['RushAtt'] + wr_df['Tgt'])/wr_df['G']
wr_df['Usage/GM'] = wr_df['Usage/GM'].apply(lambda x: round(x, 2))

te_df['FantasyPoints/GM'] = te_df['FantasyPoints']/te_df['G']
te_df['FantasyPoints/GM'] = te_df['FantasyPoints/GM'].apply(lambda x: round(x, 2))

te_df['Usage/GM'] = (te_df['RushAtt'] + te_df['Tgt'])/te_df['G']
te_df['Usage/GM'] = te_df['Usage/GM'].apply(lambda x: round(x, 2))

qb_df['FantasyPoints/GM'] = qb_df['FantasyPoints']/qb_df['G']
qb_df['FantasyPoints/GM'] = qb_df['FantasyPoints/GM'].apply(lambda x: round(x, 2))

qb_df['Usage/GM'] = (qb_df['RushAtt'] + qb_df['PassAtt'])/rb_df['G']
qb_df['Usage/GM'] = qb_df['Usage/GM'].apply(lambda x: round(x, 2))

df_merged = pd.concat([rb_df, qb_df, wr_df, te_df], ignore_index=True, sort=False)




sns.set_style("whitegrid")
sns.set_palette("bright")
g = sns.relplot(data=df_merged, x='AverageDraftPosition', y='FantasyPoints/GM', hue='Position')


g.fig.suptitle('Average Draft Position vs. Fantasy Points per Game by Position', fontsize=14)
g.set_axis_labels('Average Draft Position', 'Fantasy Points per Game')

plt.show()




