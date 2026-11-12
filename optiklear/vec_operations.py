import math

# Add more than 2 vectors
def add2D_multi(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))



def vec_add2D(u, v):
    w = [u[0] + v[0], u[1] + v[1]]
    return w
#print(vec_add([2, 4], [5, 10]))


def vec_subtract2D(u, v):
      w = [u[0]- v[0], u[1] - v[1]]
      return w


def mag_v2D(v):
   # return math.floor(math.sqrt(v[0]**2 + v[1]**2))
     return  math.sqrt(v[0]**2 + v[1]**2)
#print(mag_v([5, 10]))

def dis_vecs2D(u, v):
    return math.sqrt((v[0]-u[0])**2 + (v[1]-u[1])**2)



def dot_product2D(u, v):
     uv = u[0] * v[0] + u[1] * v[1]
     return uv



def ang_vectors2D(u, v):
    uv = dot_product2D(u, v)
    cos_val = uv/(mag_v2D(u) * mag_v2D(v))
    ang_between = math.degrees(math.acos(cos_val))
    return ang_between



def scale(weight, v):
     v = [weight * i for i in v]
     return v



# use for single polar coordinates
def pole_to_cart(radius, angle):
      x = radius * math.cos(math.radians(angle))
      y = radius * math.sin(math.radians(angle))
      return (x, y)


def polar_vector_to_cart(polar_vector):
    length, angle = polar_vector
    return (length*math.cos(angle), length*math.sin(angle))

# use for single vector
def cart_to_pole(x, y):
     radius = math.sqrt(x**2 + y**2)
    # tan_theta = y/x
     theta = math.atan2(y, x)    
     return (radius,  theta)

# use for multiple vectors
def cart_to_polar(vector):
    x, y = vector[0], vector[1]
    angle = math.atan2(y,x)
    return (mag_v2D(vector), angle)


def rotate(angle, vectors):
    polars = [cart_to_polar(v) for v in vectors]
    return [polar_vector_to_cart((length, a+angle)) for length,a in polars]


def translate(translation, vectors):
    return [add2D_multi(translation, v) for v in vectors]
 

def cross_prod(u, v):
   u_cross_v = [u[1]* v[2] - u[2] * v[1] ,  u[2] * v[0]  - u[0] * v[2] , u[0] * v[1] - u[1] * v[0] ]
   return u_cross_v
#print(cross_prod([1, 2, -1], [2, -1, 2]))