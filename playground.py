# import pandas as pd
# import yaml
# import io
# import datetime

#
# atup = ('a',1)
# print(atup[0])
#
# adict ={'a': 1, 'b': 2, 'c': 3}
# print(len(adict))

alist = ['a','b','c']

blist = alist.copy()

blist.append('d')

print(alist)

# file = open("225171.yaml", 'r')
#
# sample_data = yaml.load(file)
#
#
#
# print(list(sample_data))
#
# print(len(sample_data['innings']))
# innings_sequence = list(sample_data['innings'][0])[0]
#
# print(innings_sequence)
# innings_data = sample_data['innings'][0][innings_sequence]
#
# innings_deliveries = innings_data['deliveries'][7]
#
# print(innings_deliveries)
#
# print(list(innings_data))

# record = {"matchID": "", "city": "", "player_of_match":"","teamA": "", "teamB": "", "date": datetime.date(1, 1, 1), "gender": "", "winner": "", "margin": 0, "runs/wickets": 0, "player_of_match": "","toss_winner": "", "toss_decision": "", "venue": "", 'India_match': 0}
#
# record['player_of_match'] = info_data['player_of_match'][0]
# record['city'] = info_data['city']
# record['date'] = info_data['dates'][0]
# record['gender'] = info_data['gender']
# record['winner'] = info_data['outcome']['winner']
# record['runs/wickets'] = list(info_data['outcome']['by'].keys())[0]
# record["margin"] = info_data['outcome']['by'][record['runs/wickets']]
# record['teamA'] = info_data['teams'][0]
# record['teamB'] = info_data['teams'][1]
# record['toss_winner'] = info_data['toss']['winner']
# record['toss_decision'] = info_data['toss']['decision']
# record['venue'] = info_data['venue']
#
# print(record)
#
#
# print(sample_data)
# info_data = sample_data['info']
#
# print(info_data)
# df_data = pd.DataFrame.from_dict(info_data)
#
# df_data = pd.DataFrame.from_dict(info_data, orient= 'index').T
# df_data.to_excel("dataframe sample.xlsx")
#
# print(list(info_data['outcome']['by'].keys())[0])