import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('NA-Results2018 Ver 2.csv', index_col=0)
#print(df.head(25))

df_Constituency_Title = df.groupby('Constituency_Title')

result_list = []
for df_name, df_ct in df_Constituency_Title:
    new_series = (df_ct.loc[df_ct['Votes'].idxmax()]).tolist()
    result_list.append(new_series)
result = pd.DataFrame(result_list,columns=df.columns)
#print(result)

frequency = result.Part.value_counts()
#https://www.geo.tv/election
#print(frequency)
frequency_2 = frequency[frequency < 5].index
frequency_2 = result.Part.replace(frequency_2,'Others').value_counts()

frequency_2.plot.bar(color=['red', 'blue', 'cyan'])
plt.xticks(rotation=12)
label = frequency_2.tolist()
for i in range(len(label)):
    plt.text(x = (i+1)-1 , y = label[i]+1, s = label[i], size = 6)
plt.xlabel("Party")
plt.ylabel('Seats')
plt.title('Pakistan Election 2018')
plt.show()


df_vote = result.groupby(by='Part')
df_vote = df_vote.Votes.sum()
df_vote_2 = df_vote[df_vote > 300000].sort_values(ascending=False)
#print(df_vote)
df_vote_2.plot.bar(color=['red', 'blue', 'cyan'])
plt.xticks(rotation=12)
label = df_vote_2.tolist()
plt.xticks(rotation=15)
for i in range(len(label)):
    plt.text(x = (i+1)-1.25 , y = label[i]+1, s = label[i], size = 8)
plt.xlabel("Party")
plt.ylabel('Votes')
plt.title('Pakistan Election 2018')
plt.show()

# print(frequency)
# print(df_vote)

df_VandS = pd.concat([frequency, df_vote], axis=1,sort=False)
#print(df_VandS)



# data to plot
n_groups = len(df_VandS)
means_frank = (df_VandS.Part*85000)
means_guido = df_VandS.Votes

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.barh(index, means_frank, bar_width,alpha=opacity,color='b',label='Seats')
rects2 = plt.barh(index + bar_width, means_guido, bar_width,alpha=opacity,color='g',label='Votes')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.yticks(index + bar_width, df_VandS.index)
plt.legend()
plt.tight_layout()
plt.show()



noOfcandidate = df.Part.value_counts()
df_CandS = pd.concat([noOfcandidate, frequency], axis=1,sort=False)
df_CandS.columns = ['Can','Win']
df_CandS = df_CandS.dropna()
df_CandS.drop(['Independent'],inplace=True)
df_CandS.sort_values('Win', inplace=True, ascending=False)
print(df_CandS)








# data to plot
n_groups = len(df_CandS)
means_frank = (df_CandS.Can)
means_guido = df_CandS.Win
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, means_frank, bar_width,alpha=opacity,color='b',label='No of Candidate')
rects2 = plt.bar(index + bar_width, means_guido, bar_width,alpha=opacity,color='g',label='Winners')
plt.xlabel('Party')
plt.ylabel('No of Seats')
plt.title('Election 2018')
plt.xticks(rotation=80)
# label = frequency_2.tolist()
for i in range(len(means_frank)):
    plt.text(x = (i) , y = means_frank[i]+1, s = means_frank[i], size = 6)
    plt.text(x = (i+.25) , y = means_guido[i]+1, s = means_guido[i], size = 6)
plt.xticks(index + bar_width, df_CandS.index)
plt.legend()
plt.tight_layout()
plt.show()