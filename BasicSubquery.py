import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

Match_Winner = pd.read_sql("""SELECT Match_Id, Match_Winner, Team_2
            AS Team_Winner
            FROM Match
            WHERE Season_Id = 6
            AND Team_Winner = (SELECT Team_1 FROM Match WHERE Season_Id = 6 LIMIT 1);""", conn)
print("Selected Match Winners Where Season_Id is 6:-")
print(Match_Winner)

high_scorers = pd.read_sql("""SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
                           FROM Batsman_Scored
            WHERE Runs_Scored > (SELECT AVG(Runs_Scored) FROM Batsman_Scored);""", conn)
print("\nBatsman Scored More Than Average Runs:-")
print(high_scorers)

team_wins = pd.read_sql("""SELECT Match_Id, Match_Winner, Team_1 AS Team_Home
            FROM Match
            WHERE Team_Home = (SELECT Team_1 FROM Match WHERE Match_Winner = Team_1 LIMIT 1);""", conn)
print("\nSelected Team Wins Where Team_Home is same as Match_Winner:-")
print(team_wins)