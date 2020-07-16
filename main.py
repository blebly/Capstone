import copy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime, date, time
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout


class WindowManager(ScreenManager):
    pass


class StartScreen(Screen):
    pass


class IslandScreen(Screen):
    pass


class Island3Screen(Screen):
    pass


class SurveyScreen(Screen):
    checkbox1 = ObjectProperty(None)
    checkbox2 = ObjectProperty(None)
    checkbox3 = ObjectProperty(None)
    checkbox4 = ObjectProperty(None)
    checkbox5 = ObjectProperty(None)
    contentTitle = ObjectProperty(None)
    contentImage = ObjectProperty(None)
    surveyNext = ObjectProperty(None)
    surveyBefore = ObjectProperty(None)
    count = 0
    surveyResult = {}
    CF123survey = ("CF1", "CF2", "CF3")

    def check(self):
        if self.contentTitle.source == F4_titleImage[0]:
            if self.checkbox1.active == True:
                self.surveyResult[self.CF123survey[0]] = 1
            elif self.checkbox2.active == True:
                self.surveyResult[self.CF123survey[0]] = 2
            elif self.checkbox3.active == True:
                self.surveyResult[self.CF123survey[0]] = 3
            elif self.checkbox4.active == True:
                self.surveyResult[self.CF123survey[0]] = 4
            else:
                self.surveyResult[self.CF123survey[0]] = 5

        if self.contentTitle.source == F4_titleImage[1]:

            if self.checkbox1.active == True:
                self.surveyResult[self.CF123survey[1]] = 1
            elif self.checkbox2.active == True:
                self.surveyResult[self.CF123survey[1]] = 2
            elif self.checkbox3.active == True:
                self.surveyResult[self.CF123survey[1]] = 3
            elif self.checkbox4.active == True:
                self.surveyResult[self.CF123survey[1]] = 4
            else:
                self.surveyResult[self.CF123survey[1]] = 5

        if self.contentTitle.source == F4_titleImage[2]:

            if self.checkbox1.active == True:
                self.surveyResult[self.CF123survey[2]] = 1
            elif self.checkbox2.active == True:
                self.surveyResult[self.CF123survey[2]] = 2
            elif self.checkbox3.active == True:
                self.surveyResult[self.CF123survey[2]] = 3
            elif self.checkbox4.active == True:
                self.surveyResult[self.CF123survey[2]] = 4
            else:
                self.surveyResult[self.CF123survey[2]] = 5

        print(self.surveyResult)
        return self.surveyResult

    def next(self):
        self.surveyBefore.background_normal = "image/surveyBefore.png"
        self.count += 1
        self.contentTitle.source = F4_titleImage[self.count]
        self.contentImage.source = F4_studyImage[self.count]

        self.checkbox1.active = False
        self.checkbox2.active = False
        self.checkbox3.active = False
        self.checkbox4.active = False
        self.checkbox5.active = False

        if self.count == 2:
            self.surveyNext.background_normal = "image/hide.png"

    def back(self):
        self.surveyNext.background_normal = "image/surveyNext.png"
        self.count -= 1
        self.contentTitle.source = F4_titleImage[self.count]
        self.contentImage.source = F4_studyImage[self.count]

        if self.count == 0:
            self.surveyBefore.background_normal = "image/hide.png"


F4_titleImage = ["image/titleF4_1black.png", "image/titleF4_2black.png", "image/titleF4_3black.png"]
F4_studyImage = ["image/F4_1_study.png", "image/F4_2_study1-2.png", "image/F4_3_study1-3.png"]


class F4Screen(Screen):
    pass


class F5Screen(Screen):
    pass


class StudyorProblemScreen(Screen):
    pass


class StudyScreen(Screen):
    pass


class ProblemScreen(Screen):
    pass


import json

# pb DB 중 CF4 가져오기
with open("pb.json", "r") as pb_json:
    pb_python = json.load(pb_json)
    CF1pb = pb_python['Cland']['CF'][0]['problem']


class ProblemWindow(Screen):
    pass


class MultipleChoiceScreen(Screen):
    # code: 문제코드 받기
    # answer: 사용자입력 답안
    code = CF1pb[0]['code']
    answer = ObjectProperty(None)
    tagLabel = ObjectProperty(None)
    answersheet = ObjectProperty([])
    click1 = ObjectProperty(False)
    click2 = ObjectProperty(False)
    click3 = ObjectProperty(False)
    click4 = ObjectProperty(False)
    click5 = ObjectProperty(False)
    result = ObjectProperty(None)
    rate = ObjectProperty(None)
    useHint = ObjectProperty(False)
    spendTime = ObjectProperty(None)
    dtime = 0

    # Toggle Click
    def __init__(self, **kwargs):
        super(MultipleChoiceWindow, self).__init__()
        self.count = 0
        # stopwatch start
        self.build()
        # db.random("101")

    def showhint(self):
        HintPopup().open()
        self.useHint = True

    def Totalresult(self, result):
        if self.useHint == False:
            self.useHint = 'X'
        else:
            self.useHint = 'O'
        self.answersheet.append([self.code, self.answer, result, self.useHint])
        # reset useHint
        self.useHint = False
        print(self.answersheet)

    def clicked(self, argu):
        self.answer = argu

    def check(self):
        count = 0
        for i in self.answersheet:
            if i[1] == True:
                count += 1
        return count / 5

    def build(self):
        # Start the clock
        Clock.schedule_interval(self.Callback_Clock, 1)

    def Callback_Clock(self, dt):
        self.dtime = self.dtime + 1

    def pause(self):
        Clock.unschedule(self.dtime)
        return self.dtime

    def moreProb(self):
        db101 = db.random("101")
        self.count = 0
        # (0: default pb)/ 123: provide pb - 101
        for i in range(len(db101)):
            i = i + 1
            if self.count == i:
                self.code = CF4pb[db101[i]]['code']
                self.ids.problem.source = CF4pb[db101[i]]['img']
                self.tagLabel.text = CF4pb[db101[i]]['taglabel']
                sm.current = "multiplechoice"
        # 102 pb
        db102 = db.random("102")
        self.count = 0
        for i in range(len(db102)):
            i = i + 1
            if self.count == i:
                self.code = CF4pb[db102[i]]['code']
                print(self.code)
                self.ids.problem.source = CF4pb[db102[i]]['img']
                self.tagLabel.text = CF4pb[db102[i]]['taglabel']
                sm.current = "multiplechoice"
        print("========= DONE =========")
        # The end
        if self.count == len(db102):
            self.spendTime = self.pause()
            print('---duration time---', self.spendTime)
            self.rate = self.check()
            if self.rate >= 0.8:
                sm.current = "rpass"
            else:
                sm.current = "ragain"
            self.rate = self.check() * 100
            self.save()

    # user별로 progress 저장
    def save(self):
        pack = self.answersheet
        print(pack)
        file_path = "./user1.json"
        json_data = {}
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
            print("******************************")
            print(json_data['CF'][0]['trial'])
        json_data['CF'][0]['trial'].append({
            # length list -> try +1 해야함
            # answer 모든 sheet가 들어가야할까? rate만 있으면 어때?
            "ans": pack,
            "rate": self.rate,
            "spent": self.spendTime
        })
        with open(file_path, 'w') as outfile:
            json.dump(json_data, outfile, indent=3)

    def nextBtn(self):
        self.count += 1
        if db.validate(self.code, str(self.answer)):
            self.Totalresult(True)
            self.moreProb()
        else:
            wrongAnswer()
            self.Totalresult(False)
            self.moreProb()


class ShortAnswerWindow(Screen):
    answer = ObjectProperty(None)
    code = ObjectProperty(None)

    def nextBtn(self):
        if db.validate(self.code, self.answer.text):
            print(self.code, self.answer.text)
            self.reset()
            sm.current = "multiplechoice"
        else:
            wrongAnswer()
            print(self.code, self.answer)

    def reset(self):
        self.answer.text = ""


class HintPopup(Popup):
    title = 'Hint to You'


class ResultPassWindow(Screen):
    # rate = MultipleChoiceWindow.rate
    # answersheeet = MultipleChoiceWindow.answersheet

    def __init__(self, **kwargs):
        pass
        # super(ResultPassWindow, self).__init__()
        # #rate / pb OX 표시
        # print("This One!!!")
        # print(self.rate)
        # print(self.answersheeet)


class ResultAgainWindow(Screen):
    pass


kv = Builder.load_file("ProblemUI.kv")
db = DataBase("pb.json")
sm = WindowManager()

screens = [StartScreen(name="start"), IslandScreen(name="island"), Island3Screen(name="island3"),
           SurveyScreen(name="survey"), F4Screen(name="F4"), F5Screen(name="F5"),
           StudyorProblemScreen(name="studyorproblem"), StudyScreen(name="study"),
           MultipleChoiceWindow(name="multiplechoice"), ShortAnswerWindow(name="shortanswer"),
           ResultPassWindow(name="rpass"), ResultAgainWindow(name="ragain")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "start"


def wrongAnswer():
    pop = Popup(title='Wrong Answer',
                content=Label(text='Please think once more and deeply.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
