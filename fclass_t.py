class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_info(self):
        print '%s : %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



if __name__ == '__main__':
    std = Student('wyjh', 90)
    std.print_info()
    print std.get_grade()
