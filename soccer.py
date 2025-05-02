def points(games):
    points = 0
    for i in games:
        opponent = i[2]
        team = i[0]
        if team > opponent:
            points += 3
        elif team == opponent:
            points += 1
    return points