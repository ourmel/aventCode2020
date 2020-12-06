from common.helpers import read_text
import os

class tobPosition:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def move(self,right, down ) :
        x_pos = self.x_pos + right
        y_pos = self.y_pos + down
        return [x_pos, y_pos]

def get_point(x,y):
    if plan[y][x] == "#":
        return 1
    else:
        return 0


if __name__ == '__main__':
    day = 3
    filename = str('input' + str(day))
    print(os.listdir())


    # final = solve_puzzle_with_comb(pos,plan,3,1)

    slope_list = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    nb_of_trees = 1
    for slope in slope_list :

        plan = read_text(filename)
        nb_of_trees_tmp = 0
        pos = tobPosition(0, 0)

        while (pos.y_pos < (len(plan) -1)) :

            pos.x_pos, pos.y_pos = pos.move(slope[0],slope[1])
            if pos.x_pos >= len(plan[0]):
                plan = [x+x for x in plan]
            nb_of_trees_tmp = nb_of_trees_tmp + get_point(pos.x_pos, pos.y_pos)
        print(nb_of_trees_tmp)

        nb_of_trees = nb_of_trees * nb_of_trees_tmp

    print(nb_of_trees)