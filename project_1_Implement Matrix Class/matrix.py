import math
from math import sqrt
import numbers

def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)

def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])
    #
    # Primary matrix math methods
    #############################
    
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        det = 0
        if self.h == 1:
            det = 1/self.g[0][0]
        else:
            judgement = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
            if judgement == 0:
                raise (ValueError, "The determinant of the matrix is zero")
            else:
                det = 1/judgement
            
        return det
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        s = 0
        result = []
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    result.append(self.g[i][j])
        s = sum(result)
        
        return s                       
                       

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        #inverse_matrix = zeroes(self.h, self.w)
        if self.h == 1:
            return [1/selg.g[0][0]]
        else:
            inverse_matrix = zeroes(self.h, self.w)
            det = Matrix.determinant(self)
            inverse_matrix.g[0][0] = det*self.g[1][1]
            inverse_matrix.g[0][1] = -det*self.g[0][1]
            inverse_matrix.g[1][0] = -det*self.g[1][0]
            inverse_matrix.g[1][1] = det*self.g[0][0]
           
            return inverse_matrix
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = zeroes(self.h, self.w)
        for j in range(self.w):
            for i in range(self.h):
                matrix_transpose.g[j][i] = self.g[i][j]
        
        return matrix_transpose

    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        """item = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                item.g[i][j] = self.g[i][j]"""
        
        return self.g[idx]

    
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrix_sum = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix_sum.g[i][j] = self.g[i][j] + other.g[i][j]
        
        return matrix_sum        
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        negative_matrix = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                negative_matrix.g[i][j] = -1 * (self.g[i][j])
    
        return negative_matrix
        
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        matrix_sub = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix_sub.g[i][j] = self.g[i][j] - other.g[i][j]
        
        return matrix_sub        

    
    def get_row(self, row_number):
       
        return self.g[row_number]
    
    
    def get_column(self, column_number):
        column = []
        for i in range(self.h):
            column.append(self[i][column_number])
        return column        

    
    def dot_product(vector_one, vector_two):
        s = 0
        for i in range(len(vector_one)):
            value_1 = vector_one[i]
            value_2 = vector_two[i]
            s += value_1 * value_2
        
        return s
    
    

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        matrix_multi = zeroes(self.h, other.w)
        
        for i in range(self.h):
            row_a = Matrix.get_row(self, i)
            for j in range(other.w):
                column_b = Matrix.get_column(other, j)
                matrix_multi.g[i][j] = Matrix.dot_product(row_a, column_b)
          
        return matrix_multi
        
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            new_matrix = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    new_matrix.g[i][j] = other * self.g[i][j]
            
        return new_matrix
            
            