"""  Created by Paul A. Gureghian in Feb 2019 """

""" Gradient Descent Algorithm """

### Initialize parameters
cur_x = 3
rate = 0.01
precision = 0.000001
previous_step_size = 1
max_iters = 10000
iters = 0
df = lambda x: 2*(x+5)

### Run a 'while' loop for gradient descent
while previous_step_size > precision and iters < max_iters:

    prev_x = cur_x
    cur_x = cur_x - rate * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters = iters + 1
    print("Iteration:", iters, '\n', "X value is:", cur_x, '\n')

print("The local minimum occurs at:", cur_x)

