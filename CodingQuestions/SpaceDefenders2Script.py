#SD2 Script to auto write data.
import random
import os.path

def main():
    counter = 1
    final = 3  #number of files
    counter2 = 1
    final2 = 10  #number of commands per file

    save_path = 'C:/Users/Shesan/Desktop/spacedefendersSCRIPT/'

    while counter <= final:
        outfile = open(save_path + 'student_test' + str(counter) + '.txt', 'w')
        max_row = random.randint(5,10)
        max_col = random.randint(10,30)
        threshhold = random.sample(range(1,101), 5)
        threshhold.sort()
        row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        play = ("play(" + str(max_row) + "," + str(max_col) + "," + str(threshhold[0])+ "," + str(threshhold[1])+ "," + str(threshhold[2])+ "," + str(threshhold[3])+ "," + str(threshhold[4]) + ")")
        arr = []


        while counter2 <= final2:
            state = random.randint(1,5)
            select = random.randint(1,5)

            setup_select = ("setup_select(" + str(select) + ")")
            setup_next = ("setup_next(" + str(state) + ")")
            setup_back = ("setup_back(" + str(state) + ")")
            toggle_debug_mode = ("toggle_debug_mode")
            abort = ("abort")
            move = ("move(" + row[random.randint(0, max_row - 1)] + "," + str(random.randint(1, max_col)) + ")")
            pass2 = ("pass")
            fire = ("fire")
            special = ("special")

            arr.append(play)
            arr.append(setup_select)
            arr.append(setup_back)
            arr.append(setup_next)
            arr.append(toggle_debug_mode)
            arr.append(abort)
            arr.append(move)
            arr.append(pass2)
            arr.append(fire)
            arr.append(special)

            outfile.write(random.choice(arr) + "\n")
            


            counter2 += 1

        outfile.close()
        counter2 = 1
        counter += 1

main()


