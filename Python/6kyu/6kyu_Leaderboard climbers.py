def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, move = change.split(' ')
        for i in range(len(leaderboard)):
            if leaderboard[i] == name:
                leaderboard.insert(i - int(move), leaderboard.pop(i))
                break
    return leaderboard
