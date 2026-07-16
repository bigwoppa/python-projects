from numpy import *
def compute_error_for_line_given_points(b, m, points):
    #initialize the total error to 0
    totalError = 0
    #for every point in the data set
    for i in range(0, len(points)):
        #Get the X and Y values of the point
        x = points[i, 0]
        y = points[i, 1]
        #get the difference, square it and add it to the total error
        totalError += (y - (m*x + b)) **2
     
    #get the average error by dividing the total error by the number of points
    return totalError / float(len(points))

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    #starting m and b
    b = starting_b
    m = starting_m

    #Gradient Descent
    for i in range(num_iterations):
        #update b and m with the new more accurate b and m by performing this gradient step
        b, m = step_gradient(b,m, points, learning_rate)
    return [b, m]


def step_gradient(b_current, m_current, points, learningRate):
    #starting points
    b_gradient = 0
    m_gradient = 0
    N= float(len(points))
    for i in range(0, len(points)):
        #starting points for our gradient
        x = points[i, 0]
        y = points[i, 1]

        #direction with respect to b and m
        #computing partial derivatives
        b_gradient += -(2/N) * (y - (m_current*x + b_current))
        m_gradient += -(2/N) * x * (y - m_current * x - b_current)
    #update b and m
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def run():
    # Load the data
    points = genfromtxt('data.csv', delimiter=',')

    # Step 2: - define our hyperparameters
    #how fast should the model convert
    learning_rate = 0.0001
    #y=mx+b slope formula so inital slope and y intercept
    initial_b = 0
    initial_m = 0
    num_iterations = 500

    #Step 3: - train the model
    print (f'starting point at b = {initial_b}, m = {initial_m}, error = {compute_error_for_line_given_points(initial_b, initial_m, points)}')
    print('running...')
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print(f'after {num_iterations} iterations b = {b}, m = {m}, error = {compute_error_for_line_given_points(b, m, points)}')
run()