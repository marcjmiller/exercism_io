class Matrix:
    def __init__(self, matrix_string):
        # self.matrix = matrix_string.splitlines()
        # for i, row in enumerate(self.matrix):
        #     self.matrix[i] = row.split(" ")
        #     for j, item in enumerate(self.matrix[i]):
        #         self.matrix[i][j] = int(item)
        #
        # condensed
        self.matrix = [
            [int(item) for item in row.split()] for row in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
