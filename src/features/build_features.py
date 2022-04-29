import pandas as pd

df = pd.read_csv("/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/cleaned_data.csv")

def create_feat(df):
    #Create features in cleaned dataset
    
    #Add player game number as new column
    df.insert(len(df.columns), 'player_game_num', False)
    for i in range(1, len(df)):
        if (df['player_id']).iloc[i] == (df['player_id']).iloc[i-1]:
            df['player_game_num'].iloc[i] = (df['player_game_num'].iloc[i-1] + 1)
        else:
            df['player_game_num'].iloc[i] = 1

    #Create column to rank player position by minutes played at position
    


    