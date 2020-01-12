import pandas as pd
import yaml
import io
import datetime
import os


def run():

    data_folder_path = "data\odis_sample"
    record_innings = extract_match_info()
    innings_table = pd.DataFrame(columns=list(record_innings))
    print(innings_table)

    i = 0

    for file_name in os.listdir(data_folder_path):
        file_address = os.path.join(data_folder_path, file_name)
        file = open(file_address, 'r')
        match_data = yaml.load(file)
        print(i, "  -->  ", file_name)
        match_innings = match_data['innings']





        
        record_info = extract_match_info(file_name[:-5], match_innings)
        info_table = info_table.append(record_info, ignore_index=True)
        i+=1
        if  (i == 100):
            info_table.to_excel("info_table_partial.xlsx", index=False)

    info_table.to_excel("sample_info.xlsx", index=False)

    pass


def extract_match_info(matchID="Blank", info_data="Blank"):
    record = {"matchID": "", "city": "", "teamA": "", "teamB": "", "date": datetime.date(1, 1, 1), "gender": "", "winner": "", "margin": 0, "runs/wickets": 0, "player_of_match": "","toss_winner": "", "toss_decision": "", "venue": "", 'India_match': 0}
    if info_data != "Blank":
        try:
            record['gender'] = info_data['gender']
            record['player_of_match'] = info_data['player_of_match'][0]
            print(info_data['player_of_match'][0])
            record['city'] = info_data['city']
            record['venue'] = info_data['venue']
        except KeyError:
            pass
        record['date'] = info_data['dates'][0]
        try:
            record['winner'] = info_data['outcome']['winner']
            record['runs/wickets'] = list(info_data['outcome']['by'].keys())[0]
            record["margin"] = info_data['outcome']['by'][record['runs/wickets']]
        except KeyError:
            record['winner'] = "No Result"
        record['teamA'] = info_data['teams'][0]
        record['teamB'] = info_data['teams'][1]
        record['toss_winner'] = info_data['toss']['winner']
        record['toss_decision'] = info_data['toss']['decision']
        record['matchID'] = matchID
        if record["teamA"] == "India" or record['teamB'] == 'India':
            record['India_match'] = 1
    return record


def extract_deliveries_info(matchID="Blank", deliveries_data="Blank"):
    record = {"matchID": "", "team": "", "team_opposition": "", "innings": 0, "over": 0, "ball": 0, "over_ball": "", "batsman": "",
              "non_striker": "", "bowler": "", "extra": False, "extra_type": "", "extra_runs": 0, "wicket": False,
              "wicket_type": "", "wicket_batsman": "", "runs": 0, "total_ball_runs": 0, "total_innings_runs": 0}
    if deliveries_data != "Blank":
        try:
            record['gender'] = deliveries_data['gender']
            record['player_of_match'] = deliveries_data['player_of_match'][0]
            print(deliveries_data['player_of_match'][0])
            record['city'] = deliveries_data['city']
            record['venue'] = deliveries_data['venue']
        except KeyError:
            pass
        record['date'] = deliveries_data['dates'][0]
        try:
            record['winner'] = deliveries_data['outcome']['winner']
            record['runs/wickets'] = list(deliveries_data['outcome']['by'].keys())[0]
            record["margin"] = deliveries_data['outcome']['by'][record['runs/wickets']]
        except KeyError:
            record['winner'] = "No Result"
        record['teamA'] = deliveries_data['teams'][0]
        record['teamB'] = deliveries_data['teams'][1]
        record['toss_winner'] = deliveries_data['toss']['winner']
        record['toss_decision'] = deliveries_data['toss']['decision']
        record['matchID'] = matchID
        if record["teamA"] == "India" or record['teamB'] == 'India':
            record['India_match'] = 1
    return record


if __name__ == '__main__':
    run()