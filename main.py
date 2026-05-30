from src.data.scrape import clean_match_results
from src.analysis.stats import calculate_all_teams
from src.data.export import save_team_stats


if __name__ == "__main__":
    df = clean_match_results()
    team_stats = calculate_all_teams(df)
    save_team_stats(team_stats)