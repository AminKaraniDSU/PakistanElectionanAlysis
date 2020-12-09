import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)
import numpy as np
import matplotlib.pyplot as plt

seat_changes = pd.read_csv('2013-2018 Seat Changes in NA.csv')
df_2013 = pd.read_csv('National Assembly 2013.csv', encoding='unicode_escape',index_col=0)
df_2018 = pd.read_csv('NA-Results2018 Ver 2.csv',  encoding='unicode_escape',index_col=0)

# print(seat_changes.head(5))
# print(df_2013.head(5))
# print(df_2018.head(5))

df_groupby_ConstituencyTitle_13 = df_2013.groupby('ConstituencyTitle')
dict=[]
for name, dataframe in df_groupby_ConstituencyTitle_13:
    new_series=(dataframe.loc[dataframe['Votes'].idxmax()]).tolist()
    dict.append(new_series)
result_2013 = pd.DataFrame(dict,columns=df_2013.columns)

df_groupby_ConstituencyTitle_18 = df_2018.groupby('Constituency_Title')
dict2=[]
for name, dataframe in df_groupby_ConstituencyTitle_18:
    new_series=(dataframe.loc[dataframe['Votes'].idxmax()]).tolist()
    dict2.append(new_series)
result_2018 = pd.DataFrame(dict2,columns=df_2018.columns)

# print(result_2013)
# print(result_2018)

seat_changes['2018 Seat Number'].replace( { r"NA-0{1,2}" : 'NA-' }, inplace= True, regex = True)
seat_changes['2013 Seat Number'].replace( { r"NA-0{1,2}" : 'NA-' }, inplace= True, regex = True)


temp_df = pd.merge(left=result_2013, right=seat_changes, left_on='ConstituencyTitle', right_on='2013 Seat Number', how='outer')
new_df = pd.merge(left=temp_df, right=result_2018, left_on='2018 Seat Number', right_on='Constituency_Title', how='outer', suffixes=('_2013','_2018'))
new_df.set_index('Seat Name', inplace=True)
print('Party winners in 2013 and 2018')
print((new_df[['2013 Seat Number','2018 Seat Number','Party','Part']]))
print('Turnout in 2013 and 2018')
# print((new_df[['2013 Seat Number','2018 Seat Number','Turnout_2013','Turnout_2018']]))
print(new_df.columns)

party_seat_2013 = new_df.Party.value_counts()
party_seat_2019 = new_df.Part.value_counts()
party_seat = pd.concat([party_seat_2013,party_seat_2019],axis=1,sort=False)
party_seat.fillna(0, inplace=True)
party_seat = party_seat.fillna(0.0).astype(int)
print(party_seat)







n_groups = len(party_seat)
means_frank = (party_seat.Party)
means_guido = party_seat.Part
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, means_frank, bar_width,alpha=opacity,color='b',label='2013')
rects2 = plt.bar(index + bar_width, means_guido, bar_width,alpha=opacity,color='g',label='2018')
plt.xlabel('Party')
plt.ylabel('No of Seats')
plt.title('Election 2018')

# label = frequency_2.tolist()
for i in range(len(means_frank)):
    plt.text(x = (i) , y = means_frank[i]+1, s = means_frank[i], size = 6)
    plt.text(x = (i+.25) , y = means_guido[i]+1, s = means_guido[i], size = 6)
plt.xticks(index + bar_width, party_seat.index)
plt.legend()
plt.tight_layout()
plt.show()