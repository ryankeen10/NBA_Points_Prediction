import pandas as pd

df_min = pd.read_csv('/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/minute_data.csv')
df_ia = pd.read_csv('/Users/ryankeen/Personal_Projects/NBA_Betting/data/cleaned/inactives_data.csv')

def pred_min(df_min, df_ia):
    df = df

    #Set rolling weights
    weights3 = np.array([.15, .3, .55])
    weights5 = np.array([.05, .1, .2, .3, .35])
    weights10 = np.array([.01, .03, .05, .07, .09, .11, .13, .15, .17, .19])

    #Initialize pred_min variable
    
