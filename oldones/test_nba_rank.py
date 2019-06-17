# coding: utf-8

"""deal with the west nba teams rank
"""

class Club(object):

    def __init__(self, name, rank, win, lose):

        self.name = name
        self.rank = rank
        self.score = {'win': win, 'lose': lose}

    def win(self):
        self.score['win'] += 1

    def lose(self):
        self.score['lose'] += 1

    def set_rank(self, rank):
        self.rank = 1

    def set_score(self, win, lose):
        self.score['win'] = win
        self.score['lose'] = lose


rockets = Club('火箭', 1, 64, 16)
warriers = Club('勇士', 2, 58, 23)
ktz = Club('开拓者', 3, 48, 33)
jazz = Club('jazz', 4, 47, 33)
tihu = Club('鹈鹕', 5, 47, 34)
spurs = Club('马刺', 6, 47, 34)
thunder = Club('雷霆', 7, 47, 34)
sll = Club('森林狼', 8, 47, 34)
juejin = Club('掘金', 9, 46, 35)

# 无关球队
lakers = Club('湖人', 11, 34, 46)
king = Club('国王', 12, 26, 55)
huixiong = Club('灰熊', 14, 22, 59)


def compete(game, res):
    c1, c2 = game
    if res:
        c1.win()
        c2.lose()
    else:
        c2.win()
        c1.lose()

def get_agenda():
    game_4_11 = [(warriers, jazz), (rockets, lakers)]
    game_4_12 = [(juejin, sll), (spurs, tihu), (huixiong, thunder), (jazz, ktz), (rockets, king)]
    return game_4_11+game_4_12

team_ranks = []

def gen_res(games):
    pass

def get_rank(*args):
    i = 1
    args = list(args)
    while len(team_ranks) != 12:
        max_win = 0
        team = None
        max_index = 0
        for index, item in enumerate(args):
            if item.score['win'] > max_win:
                max_win = item.score['win']
                team = item
                max_index = index
        item.rank = i
        i += 1
        team_ranks.append(team)
        args.pop(max_index)

    for team in team_ranks[:9]:
        print "%s %d胜 %d负 %d" % (team.name, team.score['win'], team.score['lose'], team.rank)


def main():
    # 获取比赛日程
    games = get_agenda()
    # 预测比赛可能性
    # 根据每一种总的比赛可能性，生成球队战绩，并打印最终排名
    games_res = gen_res(games)
    for game_res in games_res:
        for one in game_res:
            teams, res = one
            compete(teams, res)
        get_rank(rockets, warriers, ktz, jazz, tihu, spurs, thunder, sll, juejin, lakers, king, huixiong)
    

main()










