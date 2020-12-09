import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.expand_frame_repr', False)
import numpy as np
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 200)
# pd.set_option('display.width', 1000)

#reading Data Frame
df = pd.read_csv('National Assembly 2013.csv', encoding='unicode_escape',index_col=0)
#print(df)

df_groupby_ConstituencyTitle = df.groupby('ConstituencyTitle')

dict=[]
winer = pd.DataFrame(index=df.columns)
for name, dataframe in df_groupby_ConstituencyTitle:
    new_series=(dataframe.loc[dataframe['Votes'].idxmax()]).tolist()
    dict.append(new_series)
winer = pd.DataFrame(dict,columns=df.columns)

fre_1 = winer.Party.value_counts()
small_party = fre_1[fre_1 < 15].index
fre2 = winer.Party.replace(small_party,'Others')
fre2 = fre2.value_counts()

fre2.plot.bar(width=.60,color=['red', 'blue', 'cyan'])
label = fre2.tolist()
plt.xticks(rotation=15)
for i in range(len(label)):
    plt.text(x = (i+1)-1 , y = label[i]+1, s = label[i], size = 6)
plt.xlabel("Party")
plt.ylabel('Seats')
plt.title('Pakistan Election 2013')
plt.show()




df_party = df.groupby('Party')
df_party_vote = df_party.Votes.sum()
print(type(df_party))

df_party_vote2 = df_party_vote[df_party_vote > 500000]
df_party_vote2.sort_values(ascending=False, inplace=True)
#print(df_party_vote.sort_values(ascending=False))



df_party_vote2.plot.bar(width=.60,color=['red', 'blue', 'cyan'])
label = df_party_vote2.tolist()
plt.xticks(rotation=15)
for i in range(len(label)):
    plt.text(x = (i+1)-1.10 , y = label[i]+3, s = label[i], size = 6)
plt.xlabel("Party")
plt.ylabel('Votes')
plt.title('Pakistan Election 2013')
plt.show()

print('Turnout')
df['Turnout'] = df['Turnout'].replace({'\s\%':'','\%':''}, regex = True)
df['Turnout'] = df['Turnout'].astype(float)


print(round(df.Turnout[df.Turnout > 0].mean(),2))



fre = df.Party.value_counts()
# small_party = fre[fre < 10].index
# fre = df.Party.replace(small_party,'Others')
# fre = fre.value_counts()
print(fre.sort_values(ascending=False))
fre = fre[:10]

fre.plot.bar(width=.60,color=['red', 'blue', 'cyan'])
label = fre.tolist()
plt.xticks(rotation=15)
for i in range(len(label)):
    plt.text(x = (i+1)-1.10 , y = label[i]+3, s = label[i], size = 6)
plt.xlabel("Party")
plt.ylabel('Candidates')
plt.title('Pakistan Election 2013')
plt.show()


df_VandS = pd.concat([fre_1, df_party_vote], axis=1,sort=False)
# print(df_VandS)



# data to plot
n_groups = len(df_VandS)
means_frank = (df_VandS.Party*65000)
means_guido = df_VandS.Votes

# create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.35
# opacity = 0.8
#
# rects1 = plt.barh(index, means_frank, bar_width,
# alpha=opacity,
# color='b',
# label='Seats')
#
# rects2 = plt.barh(index + bar_width, means_guido, bar_width,
# alpha=opacity,
# color='g',
# label='Votes')
#
# plt.xlabel('Person')
# plt.ylabel('Scores')
# plt.title('Scores by person')
# plt.yticks(index + bar_width, df_VandS.index)
# plt.legend()
#
# plt.tight_layout()
#
# print("++++++++++++++++++++++")
# print(df_VandS)
# plt.show()

