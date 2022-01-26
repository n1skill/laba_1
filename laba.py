class Empl:

    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.surname} {self.name}'



class Dept:

    def __init__(self, name_dept, empl:list):
        self.name_dept = name_dept
        self.empl = empl

    def add_empl(self, empl):
        self.empl.append(empl)

    def remove_empl(self, empl):
        self.empl.remove(empl)

    def __str__(self):
        res = '\n'.join(map(str, self.empl))
        return f'{self.name_dept}\n{res}'


empl_1 = Empl('Simon', 'Ruff', '12.01.92')
empl_2 = Empl('Tom', 'Buff', '21.03.90')
empl_3 = Empl('Lisa', 'Simpson', '01.09.96')

dep_1 = Dept('Media', [empl_1, empl_2, empl_3])

print(dep_1)
