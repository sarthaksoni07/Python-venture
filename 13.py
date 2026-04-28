class Football:
    def __init__(self, player_id, player_name, match_goals):
        self.player_id = player_id
        self.player_name = player_name
        self.match_goals = match_goals
        self.qualified = False
    def findQualification(self):
        total = sum(self.match_goals)
        avg = total/5
        if avg>=3:
            self.qualified = True
        return self.qualified

pl1 = Football(1, "sarthak" , [3,3,3,3,3]) 
pl2 = Football(2, "rahul" , [2,2,2,2,2]) 
print(pl1.findQualification())
print(pl2.findQualification())