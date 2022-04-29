import pandas as pd

df = pd.read_csv('/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/ready_data.csv')

def minute_table(df):
    #Create table used for minute prediction
    df = df[['game_date', 'starter', 'did_not_play', 'game_id_player_id', 'player_id', 'did_not_play', 'minutes', 'player_game_num', 'is_inactive']]

    #Create feature pred_min
    df['pred_min'] = df['minutes']

    df_out = df
    df_out.to_csv('/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/minute_data.csv', index = False)

minute_table(df)

def inactives(df):
    #Create table of inactive players and position
    df = df['player_id', 'is_inactive']
    df = df[df['is_inactive'] == 1]