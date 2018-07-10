def select_name_of_player_with_shortest_name():
    return """
            SELECT name AS name_length
            FROM players
            ORDER BY LENGTH(name) ASC
            LIMIT 1;
            """

def select_all_new_york_players_names():
    return """
            SELECT players.name
            FROM players
            JOIN teams
            ON players.team_id = teams.id
            WHERE teams.name LIKE 'New York%';
            """

def select_team_name_and_total_goals_scored_for_new_york_rangers():
    return """
            SELECT teams.name, SUM(team_games.score)
            FROM teams
            JOIN team_games
            ON teams.id = team_games.team_id
            GROUP BY teams.name
            HAVING teams.name = "New York Rangers";
            """

def select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl():
    return """
            SELECT games.date, games.info, teams.name, team_games.score
            FROM games
            JOIN team_games
            ON games.id = team_games.game_id
            JOIN teams
            ON team_games.team_id = teams.id
            JOIN leagues
            ON teams.league_id = leagues.id
            WHERE leagues.name = "NHL";
            """

def select_date_info_and_total_points_for_highest_scoring_nba_game():
    return """
            SELECT games.date, games.info, SUM(team_games.score)
            FROM games
            JOIN team_games
            ON games.id = team_games.game_id
            JOIN teams
            ON team_games.team_id = teams.id
            JOIN leagues
            ON teams.league_id = leagues.id
            GROUP BY (games.id)
            HAVING leagues.name = "NBA"
            ORDER BY team_games.score DESC
            LIMIT 1;
            """
