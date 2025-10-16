class Tester:
    def __init__(self, name, deadline=False):
        self.name = name
        self.deadline = deadline

    def work_hard(self):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1', deadline=False)
tester_2 = Tester(name='tester_2', deadline=True)

tester_1.work_hard()
tester_2.work_hard()