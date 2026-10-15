"""SESSION 14 - Full Pandas Mini Project (Case Study From Syllabus)"""
import pandas as pd
import numpy as np

# ==========================================
# Task 1: Load IPL Dataset
# ==========================================
try:
    ipl_df = pd.read_csv("ipl_matches.csv")
except FileNotFoundError:
    data = {
        "match_id": [1, 2, 3, 4, 5],
        "season": [2022, 2022, 2023, 2023, 2023],
        "team1": ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Delhi Capitals"],
        "team2": ["Mumbai Indians", "Chennai Super Kings", "Delhi Capitals", "Royal Challengers Bangalore", "Kolkata Knight Riders"],
        "winner": ["Chennai Super Kings", None, "Royal Challengers Bangalore", "Kolkata Knight Riders", None],
        "win_by_runs": [20, 0, 0, 15, 0],
        "win_by_wickets": [0, 6, 5, 0, 4]
    }
    ipl_df = pd.DataFrame(data)

print("--- Task 1: First 5 Rows of IPL DataFrame ---")
print(ipl_df.head())
print("\n" + "="*50 + "\n")


# ==========================================
# Task 2: Clean the DataFrame
# ==========================================
ipl_df = ipl_df.dropna(subset=["winner"]).reset_index(drop=True)

print("--- Task 2: DataFrame After Cleaning Null Winners ---")
print(ipl_df.head())
print("\n" + "="*50 + "\n")


# ==========================================
# Task 3: Transform with 'match_margin_type'
# ==========================================
conditions = [
    ipl_df['win_by_runs'] > 0,
    ipl_df['win_by_wickets'] > 0
]
choices = ['Runs', 'Wickets']
ipl_df['match_margin_type'] = np.select(conditions, choices, default='Tie/No Result')

print("--- Task 3: Transformed DataFrame with Match Margin Type ---")
print(ipl_df[['match_id', 'winner', 'win_by_runs', 'win_by_wickets', 'match_margin_type']])
print("\n" + "="*50 + "\n")


# ==========================================
# Task 4: Merge with Team Home Cities
# ==========================================
teams_data = {
    "team_name": [
        "Chennai Super Kings", 
        "Mumbai Indians", 
        "Royal Challengers Bangalore", 
        "Kolkata Knight Riders", 
        "Delhi Capitals"
    ],
    "home_city": ["Chennai", "Mumbai", "Bengaluru", "Kolkata", "Delhi"]
}
teams_df = pd.DataFrame(teams_data)

ipl_df = pd.merge(ipl_df, teams_df, left_on='team1', right_on='team_name', how='left')
ipl_df = ipl_df.rename(columns={'home_city': 'team1_home_city'}).drop(columns=['team_name'])

ipl_df = pd.merge(ipl_df, teams_df, left_on='team2', right_on='team_name', how='left')
ipl_df = ipl_df.rename(columns={'home_city': 'team2_home_city'}).drop(columns=['team_name'])

print("--- Task 4: DataFrame After Merging Home Cities ---")
print(ipl_df[['match_id', 'team1', 'team1_home_city', 'team2', 'team2_home_city', 'winner']])
print("\n" + "="*50 + "\n")


# ==========================================
# Task 5: Pivot Table & Insights
# ==========================================
pivot_wins = ipl_df.pivot_table(
    index='winner', 
    columns='season', 
    values='match_id', 
    aggfunc='count', 
    fill_value=0
)

print("--- Task 5: Pivot Table of Wins by Team per Season ---")
print(pivot_wins)
print("\n--- Top 3 Teams with Most Wins in Any Single Season ---")

unstacked_wins = pivot_wins.unstack().reset_index()
unstacked_wins.columns = ['season', 'team', 'total_wins']
top_seasons = unstacked_wins.sort_values(by='total_wins', ascending=False).head(3)

print(top_seasons)
