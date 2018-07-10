INSERT INTO leagues (name) VALUES ("nfl"), ("nba");
INSERT INTO teams (name, league_id) VALUES ("Pittsburgh Steelers",1), ("New England Patriots",1),("Los Angeles Lakers",2),("Golden State Warriors",2);
INSERT INTO players (name, team_id) VALUES ("Le'Veon Bell", 1), ("Tom Brady",2),("LeBron James",3), ("Stephen Curry", 4);
INSERT INTO games (date, location) VALUES ("2018-07-10", "Pittsburgh"), ("2018-06-10", "Los Angeles"), ("2018-05-10", "New York");
INSERT INTO team_games(team_id, game_id, score) VALUES (1, 1, 30), (2, 1, 45), (3,2,80), (4,2,100), (1,3,35),(3,3,40);
