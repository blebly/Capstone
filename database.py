import datetime
import json


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        self.cpt = "CF1101"
        correct = 0
        self.count = 0
        self.wrong = 0

    def load(self):
        with open(self.filename, "r") as pb_json:
            pb_python = json.load(pb_json)
            global CF1
            CF1 = pb_python['Cland']['CF'][0]


    #CF1 0000 slicing
    def changer(self, code):
        index = int(code[3:])-1
        return CF1['problem'][index]["ans"]


    def validate(self, code: object, answer: object) -> object:
        ans = self.changer(code)
        print("ans",ans, "answer",answer)
        if ans == int(answer):
            self.count += 1
            self.pass__()
            return True
        else:
            self.down__()
            return False

    def pass__(self):
        #나중에 시작 문제 default 문제의 cpt부분 가져와서 시작해도 좋을 듯
        #현재단계 받기 - CF1에서 시작 -> #101 #102 #103 순서
        print("######",self.count)
        # 연속3개이상 pass
        if self.count == 3:
            self.nextcpt()
            print("congratulation")
            return True


    def down__(self):
        self.wrong += 1
        self.count = 0
        #누적3개 틀 down
        if self.wrong == 3:
            self.downcpt()

    def nextcpt(self):
        #현재컨셉 받아와서 101 +1
        self.cpt = "CF1102"
        return self.cpt
    def downcpt(self):
        self.cpt = "CE3101"
        return self.cpt

    def random(self, cpt):
        db = []                 # make a db dict # cpt ex)"CF1101"
        print(cpt)
        for i, e in enumerate(CF1['problem']):
            if e['cpt'] == [cpt]:
                db.append(i)
        print(db)
        return(db)



    #
    # def save(self):
    #     with open(self.filename, "w") as f:
    #         for user in self.users:
    #             f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
    #
    # @staticmethod
    # def get_date():
    #     return str(datetime.datetime.now()).split(" ")[0]