import ast

def loadScores(file):
    scores = {}
    games = {}
    with open(file) as games_file:
        data = games_file.read().replace('\\', '')
        data = ast.literal_eval(data)
        for game in data:
            # print(game)
            teams = game[6].split()
            teams = sorted([teams[0], teams[2]])
            gameName = str(game[5] + str(teams))

            if gameName not in games:
                games[gameName] = [game[len(game)-3]]
            else:
                games[gameName].append(game[len(game)-3])
                score = str(sorted(games[gameName]))

                if score not in scores:
                    scores[score] = gameName
                elif scores[score][:10] < game[5]:
                    scores[score] = gameName
                    
    return scores, games