def multiply(m1, m2):
    """
    Multiply m1 (matrix 1) with m2 (matrix 2). 
    The matrices are of the form:
        m1 = [[x1,x2,x3], [x4,x5,x6], [x7,x8,x9]]
        m2 = [[y1,y2,y3], [y4,y5,y6], [y7,y8,y9]]
	"""
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
	
    for i in range(len(m1)): # Rows of m1
          for j in range(len(m2[0])): # Columns of m2
               for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
    
    return result


def invert(matrix):
    """
    Invert the input matrix using the Gaussian elimination method
    """
    #TODO: Check every row for the correct amount of values
    num_col = len(matrix[0])
    num_rows = len(matrix)

    if num_col != num_rows:
         raise ValueError("Matrix is not square")

    n = len(matrix)
    
    identity_matrix = [[float(i == j) for i in range(n)] for j in range(n)]
    
    
    augmented_matrix = [matrix[i] + identity_matrix[i] for i in range(n)] # Augment the matrix with the identity matrix

    for i in range(n): # Apply Gaussian elimination to transform matrix into row echelon form
        if augmented_matrix[i][i] == 0: # Check if the diagonal element is zero
            for j in range(i+1, n): # Find a row below the current one with a non-zero element in the same column
                if augmented_matrix[j][i] != 0:
                    # Swap rows
                    augmented_matrix[i], augmented_matrix[j] = augmented_matrix[j], augmented_matrix[i]
                    break
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")
        
        # Normalize the row by dividing by the diagonal element
        diag_element = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= diag_element
        
        # Eliminate all other elements in the current column
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j][i]
                for k in range(2 * n):
                    augmented_matrix[j][k] -= ratio * augmented_matrix[i][k]
                    augmented_matrix[j][k] = round(augmented_matrix[j][k], 7) # Keep some decimal points, but drop trailing zeros

    
    inverse_matrix = [row[n:] for row in augmented_matrix] # Extract the inverse matrix (right half of the augmented matrix)
    
    return inverse_matrix


def determinant(matrix):
    """
    Recursively calculates the determinant of a square matrix.
    """
    # Base case for 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    # Perform Laplace expansion along the first row
    for col in range(len(matrix)):
        # Get the minor of the matrix[0][col]
        minor = get_minor(matrix, 0, col)
        # Calculate the cofactor and accumulate the determinant
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)
        det += cofactor
    
    return det

def get_minor(matrix, row, col):
    """
    Get the minor matrix after removing the specified row and column.
    """
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]
