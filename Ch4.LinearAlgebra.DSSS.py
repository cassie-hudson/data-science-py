#VECTORS

#representing vectors as lists of numbers
height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]

#building arithmetic tools
#addition--zip vectors together and use list comprehension to add

v = [1, 2, 3]
w = [4, 5, 6]

def vector_add(v, w):
    '''adds corresponding elements'''
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
#subtraction
def vector_subtract(v, w):
    '''adds corresponding elements'''
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
#create a new vector whose first element is the sum of all the first element, second element sum etc., etc. (ComponentWise Sum)

def vector_sum(vectors):
    '''sums all corresponding elements'''
    result = vectors[0] #start with the first vector
    for vector in vectors[1:]: #loops over all the other vectors
        result = vector_add(result, vector) #add the vectors to the result
    return result
#ComponentWise Sum in brief using reduce

def vector_sum(vectors):
    return reduce(vector_add, vectors)

#OR

#vector_sum = partial(reduce, vector_add)

#multiply a vector by a scalar

def scalar_multiply(c, v):
    '''c is number, v is a vector'''
    return[c * v_i for v_i in v]

#compute means of a list of the same-sized vectors
def vector_mean(vectors):
    '''compute the vector whose ith element is the mean of the ith element of the input vectors'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

#dot product--sum of the componentwise product

def dot(v, w):
    '''v_1 * w_1 + v_n * w_n'''
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

#sum of squares
def sum_of_squares(v):
    '''v_1 * v_1...v_n * v_n'''
    return dot(v, v)

#magnitude

import math

def magnitude(v):
    return math.sqrt(sum(v))

#computing the distance between two vectors
def squared_distance(v, w):
    '''(v_1 - w_1) ** 2 +...(v_n - w_n) ** 2'''
    return sum_of_squares(vector_subtract(v,w))

def distance(v, w):
    math.sqrt(squared_distance(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

print vector_add(v,w), vector_subtract(v,w)

#MATRICES

#represented as lists of lists, each inner list is the same size, representing a row of the matrix
# if A is a matrix, then A[i][j] is the element in the ith row and the jth column
#begins with row and column 0 b/c python is 0 indexed
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

len(A) # # of rows
#len(A(0)) # # of columns

def shape(A):
    num_rows = len(A)
    num_cols = len(A(0)) if A else 0 # number of elements in first row
    return num_rows, num_cols

#matrix type referred to by #rowsX#cols or n x k, where each row is a vector of k length and each column is a vector of n length

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
        for A_i in A] #for the jth element of a row i, return A_i[j]

def make_matrix(num_rows, num_cols, entry_fn):
    '''returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i,j'''
    return [[entry_fn(i, j) #given i, create a list
             for j in range(num_cols)]
            for i in range(num_rows)] #create one list for each i

#5 x 5 identity matrix (1s on the diagonal, else 0)
def is_diagonal(i, j):
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

#Friendship matrix

friendships = [[0, 1 ,1, 0, 0, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 0],
               [1, 1, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1]]

#tests whether there is a connection (1) between two users
print friendships[0][2] == 1
print friendships[0][7] == 1

#those who are friends with user 5

friends_of_five = [i
                   for i, is_friend in enumerate(friendships[5])
                   if is_friend]

print friends_of_five