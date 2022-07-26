from matplotlib import pyplot as plt

# Dictionary list of menu
menu_options = {1: 'Route 1', 2: 'Route 2', 3: 'Route 3', 4: 'Exit'}

# Defines how the direction of north, east, south, west translate
# the coordinates of the drone
# Have an empty vector list in order to produce graph from
coordinates = {'N': [0, 1], 'E': [1, 0], 'S': [0, -1], 'W': [-1, 0]}
vector_list = []

# Coordinates for each of the routes
rone_directions = ('S', 'S', 'W', 'S', 'S', 'S', 'E', 'E', 'E',
                   'S', 'S', 'W', 'W', 'S', 'E', 'E', 'E', 'E', 'N',
                   'N', 'N', 'N', 'W', 'N', 'N', 'E', 'E', 'S', 'E',
                   'S', 'E', 'S', 'S', 'W', 'S', 'S', 'S', 'S', 'S',
                   'E', 'N', 'E', 'E')

rtwo_directions = ('W', 'W', 'S', 'S', 'S', 'W', 'W', 'N', 'N',
                   'N', 'W', 'W', 'W', 'S', 'S', 'S', 'S', 'E',
                   'E', 'S', 'E', 'E', 'E', 'E', 'N', 'N', 'W',
                   'W', 'S')

rthree_directions = ('S', 'S', 'W', 'S', 'S', 'S', 'W', 'W', 'W',
                     'S', 'S', 'W', 'W', 'S', 'E', 'E', 'E', 'E',
                     'N', 'N', 'N', 'N', 'W', 'N', 'N', 'E', 'E',
                     'S', 'E')


# Route Grid

def grid():
    x = [p[0] for p in vector_list]
    y = [p[1] for p in vector_list]
    _, ax = plt.subplots()
    ax.set_xticks(range(13))
    ax.set_xticks(range(13))
    ax.plot(x, y, 'o-', color='red')
    plt.grid()
    plt.axis([1, 12, 1, 12])
    plt.title('Drone Flight Pattern')
    plt.show()


def rone():
    start = [3, 12]
    print(start)
    for d in rone_directions:
        dx, dy = coordinates[d]
        start[0] += dx
        start[1] += dy
        if start[0] > 12 or start[0] < 0:
            print('Error: this route is outside of the grid')
            break
        elif start[1] > 12 or start[1] < 0:
            print('Error: this route is outside of the grid')
            break
        else:
            print(start)
            vector_list.append(start.copy())
            x = [p[0] for p in vector_list]
            y = [p[1] for p in vector_list]
            _, ax = plt.subplots()
            ax.set_xticks(range(13))
            ax.set_xticks(range(13))
            ax.plot(x, y, 'o-', color='red')
            plt.grid()
            plt.axis([1, 12, 1, 12])
            plt.title('Drone Flight Pattern')
            plt.show()


def rtwo():
    start = [12, 11]
    print(start)
    for d in rtwo_directions:
        dx, dy = coordinates[d]
        start[0] += dx
        start[1] += dy
        if start[0] > 12 or start[0] < 0:
            print('Error: this route is outside of the grid')
            break
        elif start[1] > 12 or start[1] < 0:
            print('Error: this route is outside of the grid')
            break
        else:
            print(start)
            vector_list.append(start.copy())
            vector_list.append(start.copy())
            x = [p[0] for p in vector_list]
            y = [p[1] for p in vector_list]
            _, ax = plt.subplots()
            ax.set_xticks(range(13))
            ax.set_xticks(range(13))
            ax.plot(x, y, 'o-', color='red')
            plt.grid()
            plt.axis([1, 12, 1, 12])
            plt.title('Drone Flight Pattern')
            plt.show()


# Route Three Function

def rthree():
    start = [3, 12]
    print(start)
    for d in rthree_directions:
        dx, dy = coordinates[d]
        start[0] += dx
        start[1] += dy
        if start[0] > 12 or start[0] < 0:
            print('Error: this route is outside of the grid')
            break
        elif start[1] > 12 or start[1] < 0:
            print('Error: this route is outside of the grid')
            break
        else:
            print(start)
            vector_list.append(start.copy())
            vector_list.append(start.copy())
            x = [p[0] for p in vector_list]
            y = [p[1] for p in vector_list]
            _, ax = plt.subplots()
            ax.set_xticks(range(13))
            ax.set_xticks(range(13))
            ax.plot(x, y, 'o-', color='red')
            plt.grid()
            plt.axis([1, 12, 1, 12])
            plt.title('Drone Flight Pattern')
            plt.show()


# Route selection display for user
def routeselection():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


# User selection of route
while True:
    routeselection()
    option = int(input('Enter route:  '))
    if option == 1:
        print('Route 1 selected')
        rone()
    elif option == 2:
        print('Route 2 selected')
        rtwo()
    elif option == 3:
        print('Route 3 selected')
        rthree()
    elif option == 4:
        print('Quitting')
        exit()
    else:
        print('Invalid Route selected. Please enter a number between 1 and 4')
