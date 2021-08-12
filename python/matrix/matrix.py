class Matrix:
    """"""
    def __init__(self, matrix_string):
        """Initialize the matrix string."""
        self.matrix_string = [[int(j) for j in i.split()]] for i in matrix_string.split("\n")

    def row(self, index):
        """Return a list of the rows, reading each row left-to-right 
        while moving top-to-bottom across the rows."""
        return self.matrix[index -1]


    def column(self, index):
        """Return a list of the columns, reading each column top-to-bottom 
        while moving from left-to-right."""
        return [i for i in list(zip(*self.matrix))[index -1]]
        

