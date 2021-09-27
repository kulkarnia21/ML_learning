print('--------------------Perceptron--------------------')
tst = np.array([[-1, -1, 1], [1, 0, -1], [-1, 1.5, 1]])


def perceptron(input_array, T):
    ## inputs
    # T = number of epochs
    theta = np.zeros((input_array.shape[1] - 1))
    for t in range(T):
        for i in range(len(input_array)):
            print('i = ' + str(i) + '| t = ' + str(t))
            print(theta)
            # print(input_array[i])
            
            ##### Separate input array into x_i (inputs) and y_i (expected output)
            x_i = input_array[i][:-1]
            # print(x_i)
            y_i = input_array[i][-1]
            # print(y_i)
            ##### check if guess is correct, update if incorrect
            if y_i * np.dot(theta, x_i) <= 0:
                theta = theta + y_i * x_i
                print('updated on i = ' + str(i), ' t = ' + str(t))

                
perceptron(tst, 2)

print('initiating with x_2----------------------')
tst = np.array([[1, 0, -1], [-1, 1.5, 1], [-1, -1, 1]])
perceptron(tst, 2)
