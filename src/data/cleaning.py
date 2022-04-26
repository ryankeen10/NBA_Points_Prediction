from data_import import raw_data
import pandas as pd

def clean_transform(raw_data):
    #Drop duplicates
    df = raw_data.drop_duplicates()
    
    #Change data types, column names, percentages to decimals
    df = raw_data.astype({'season': str, 'starter': str, 'did_not_play': str, 'is_inactive': str})
    df['game_date'] = pd.to_datetime(df['game_date'], infer_datetime_format = True)
    df = df.rename(columns = {'Team_efg_pct': 'Team_efg_rate', 'Team_tov_pct' : 'Team_tov_rate', 
                              'Team_orb_pct': 'Team_orb_rate', 'Opponent_efg_pct': 'Opponent_efg_rate', 
                              'Opponent_tov_pct': 'Opponent_tov_rate', 'Opponent_orb_pct': 'Opponent_orb_rate',
                             'ts_pct': 'ts_rate', 'efg_pct': 'efg_rate', 'ts_pct': 'ts_rate', 'orb_pct': 'orb_rate', 
                             'drb_pct': 'drb_rate', 'trb_pct': 'trb_rate', 'ast_pct': 'ast_rate', 
                              'stl_pct': 'stl_rate','blk_pct': 'blk_rate', 'tov_pct': 'tov_rate', 
                              'usg_pct': 'usg_rate', 'ft_pct': 'ft_rate', 'fg_pct': 'fg_rate', 'fg3_pct': 'fg3_rate'})
    df[['Team_tov_rate', 'Team_orb_rate', 'Opponent_orb_rate', 'Opponent_tov_rate', 'orb_rate', 
        'drb_rate', 'trb_rate', 'ast_rate', 'stl_rate', 'blk_rate', 'tov_rate', 'usg_rate']] = df[['Team_tov_rate', 'Team_orb_rate', 'Opponent_orb_rate', 'Opponent_tov_rate', 'orb_rate', 
        'drb_rate', 'trb_rate', 'ast_rate', 'stl_rate', 'blk_rate', 'tov_rate', 'usg_rate']]/100
    
    #Drop rows for games that went to overtime
    df = df[df['OT'] == 0]
    
    #Remove unnecessary columns
    df = df.drop(['OT', 'mp', 'double_double', 'triple_double', 'active_position_minutes', 
                   'Inactives', 'pf', 'is_inactive', 'PF%',
                    'last_60_minutes_per_game_bench', 'last_60_minutes_per_game_starting',
                    'DKP', 'FDP', 'SDP', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'ts'], axis = 1, 
                               inplace = False)
    
    #Sort by player, date
    df = df.sort_values(by = ['player_id', 'game_date'])

    #Add player game number as new column
    df.insert(len(df.columns), 'player_game_num', False)
    for i in range(1, len(df)):
        if (df['player_id']).iloc[i] == (df['player_id']).iloc[i-1]:
            df['player_game_num'].iloc[i] = (df['player_game_num'].iloc[i-1] + 1)
        else:
            df['player_game_num'].iloc[i] = 1

    #Reset index
    df.reset_index(drop = True, inplace = True)

    df_out = df
    df_out.to_csv("/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/cleaned_data.csv", index = False)

clean_transform(raw_data)

