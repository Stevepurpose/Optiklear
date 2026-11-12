from math import cos, radians, sin

# A is a transformation matrix
def matvec_multiply(A, x):
    b = [ sum (x[j] * A[i][j] for j in range(len(x)))for i in range(len(A))]
    return b

# u is a vector
def horizontal_shear2D(u, k):
    # k is shear factor, u is vector
    A = [[1, k], [0, 1]] # A is horizontal shear matrix
    b =  matvec_multiply(A, u)
    return b
#print(horizontal_shear2D([0, 2], -1))

def vertical_shear2D(u, k):
    A = [[1, 0], [k, 1]] # A is vertical shear matrix
    b =  matvec_multiply(A, u)
    return b
#print(vertical_shear2D([2, 2], 1))   


def scale2D(u, Sx, Sy):
    #Sx and Sy are scalar constants
    A = [[Sx, 0], [0, Sy]] # A is scale  matrix
    b = matvec_multiply(A, u)
    return b
#print(scale([2, 2], 5, 0.5))

def clockwise_rotate2D(u, ang_deg):
    theta = radians(ang_deg)
    c = cos(theta)
    s = sin(theta)

    A = [[c, s],[-s,  c]]

    #A = [[cos(radians(ang_deg)), sin(radians(ang_deg))], [-sin(radians(ang_deg)), cos(radians(ang_deg))]]
    b = matvec_multiply(A, u)
    return b
#print(clockwise_rotate2D([1, 2], 30))


def antiClockwise_rotate2D(u, ang_deg):
   # A = [[cos(radians(ang_deg)), -sin(radians(ang_deg))], [sin(radians(ang_deg)), cos(radians(ang_deg))]]
    theta = radians(ang_deg)
    c = cos(theta)
    s = sin(theta)
    A = [[c, -s],[s,  c]]
    b = matvec_multiply(A, u)
    return b
#print(clockwise_rotate2D([1, 2], 30))

def flipX2D(u):
 #reflect along the y-axis
 A = [[-1, 0], [0, 1]]
 b = matvec_multiply(A, u)
 return b
#print(flipX2D([1, 2]))

def flipY2D(u):
 #reflect along the x-axis
 A = [[1, 0], [0, -1]]
 b = matvec_multiply(A, u)
 return b
#print(flipY2D([1, 2]))

def translate2D(u, translation):
   # translation is a 2d vector
   A = [[1, 0], [0, 1]]
   b = matvec_multiply(A, u)
   translated =  [b[0] + translation[0], b[1] + translation[1]]
   return translated
#print(translate2D([1, 2], [1, -1]))
