import numpy as np 

def Q_learning(num_states, num_actions, num_iterations, file_name, learning_rate, discount_factor):

    data_table = np.loadtxt(file_name, skiprows=1, delimiter=',')
    Q_table = np.zeros((num__states, num_actions))

    while(num_iterations > 0):
        for row in data_table:
            Q_table[row[0]][row[1]] += learning_rate * 
            (row[2] + discount_factor * np.max(row[3]) - Q_table[row[0]][row[1]])
            num_iterations -= 1


    return Q_table

final_Q = Q_learning(100, 4, 200, "data/small.csv", 0.01, 0.95)

max_policy = np.argmax(Q_table, axis=1)

with open("small.policy", 'w') as file:
    for line in max_policy:
        f.write("{}\n".format(line))
