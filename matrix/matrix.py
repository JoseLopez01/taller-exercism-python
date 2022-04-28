class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix_string = matrix_string

    def row(self, index):
        return list(map(int, self.matrix_string.splitlines()[index - 1].split(' ')))

    def column(self, index):
        result = []
        for value in self.matrix_string.splitlines():
            if len(value.split(' ')) >= index:
                result.append(int(value.split(' ')[index - 1]))
        return result
