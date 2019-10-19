class ProgramInternalForm:

    def __init__(self):
        self.__entries = []

    def add(self, code, identification):
        self.__entries.append((code, identification))

    def __str__(self):
        s = 'Program Internal Form :\n'
        for i in range(len(self.__entries)):
            s += str(self.__entries[i][0]) + ' ' + str(self.__entries[i][1]) + '\n'
        return s
