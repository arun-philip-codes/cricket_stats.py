class CricketStats:
    def __init__(self):
        self.matches = []
        self.players = {}
    
    def add_match_result(self, opponent, result, runs_scored, runs_conceded):
        match = {
            'date': datetime.now().isoformat(),
            'opponent': opponent,
            'result': result,
            'runs_scored': runs_scored,
            'runs_conceded': runs_conceded,
            'venue': 'Pala Cricket Ground'
        }
        self.matches.append(match)
    
    def player_performance(self, player_name, runs, wickets):
        if player_name not in self.players:
            self.players[player_name] = {'total_runs': 0, 'total_wickets': 0}
        
        self.players[player_name]['total_runs'] += runs
        self.players[player_name]['total_wickets'] += wickets
    
    def team_average(self):
        if not self.matches:
            return 0
        total_runs = sum(match['runs_scored'] for match in self.matches)
        return total_runs / len(self.matches)
