class Candidate:
    def __init__(self,candidate_id, candidate_name , question_marks ):
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.question_marks = question_marks
        self.result = None
        self.average = 0
    def findselect(self):
        sum = 0
        for i in self.question_marks:
            sum+=i
        if sum>=7.5:
            self.result = True
        else:
            self.result = False
        return self.result
 
student1 = Candidate(101, "sarthak", [3,3,3,3,3])
student2 = Candidate(102, "shre", [0,2,1,2,2])
print(student1.findselect())
print(student2.findselect())
student2.avg=sum(student2.question_marks)/len(student2.question_marks)
print(student2.avg)