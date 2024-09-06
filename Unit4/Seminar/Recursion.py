#Towers of Hanoi


import sys
auto : bool
number_of_disks: int #max number is 985 because we reach the recursion limit

turn_count : int = 0
peg_a = []
peg_b = []
peg_c = []
globals()["A"] = peg_a
globals()["B"] = peg_b
globals()["C"] = peg_c

#Interact and Solve:

def press_enter():
    if auto:
        return True
    else:
        try:
            input("Press Enter to continue to next move:")
        finally: 
            return True

def initialize(disks):
    for i in range(disks):
        peg_a.append(i + 1)
    peg_b = []
    peg_c = []
    draw()
    if press_enter():
        pass
    solve_hanoi(disks, "A", "B")

        
def solve_hanoi(num_disks, from_peg, to_peg):
    global turn_count
    if num_disks == 0:
        return
    spare_peg = get_spare_peg(from_peg, to_peg)
    solve_hanoi(num_disks - 1, from_peg, spare_peg)
    move_disk(from_peg, to_peg)
    turn_count += 1
    draw()
    if press_enter():
        solve_hanoi(num_disks - 1, spare_peg, to_peg)
        
#Hanoi:

def get_spare_peg(peg1, peg2):
    pegs = ["A", "B", "C"]
    pegs.remove(peg1)
    pegs.remove(peg2)
    return pegs[0]

def move_disk(from_peg, to_peg):
    if not len(globals()[from_peg]) > 0:
        print("This peg doesn't have any disks.")
        exit()
    if globals()[to_peg]:
        if not globals()[to_peg][0] > globals()[from_peg][0]:
            print("Invalid move. Can't move bigger disk on top of smaller disk.")
            exit()
    globals()[to_peg].append(globals()[from_peg][0])
    globals()[to_peg].sort()
    globals()[from_peg].pop(0)
    globals()[from_peg].sort()

#DRAW:

def draw_peg(peg):
    draw = []
    for i in peg:
        draw.append(str(i))
    return draw

def draw_space(peg, tallest_peg, letter):
    difference = tallest_peg - len(peg)
    if difference > 0:
        for i in range(difference):
            peg.append("")
    peg.append("||")
    peg.append(letter)
    return peg

def draw():
    tallest_peg = len(peg_a)
    if len(peg_b) > tallest_peg:
        tallest_peg = len(peg_b)
    if len(peg_c) > tallest_peg:
        tallest_peg = len(peg_c)
    
    draw_a = draw_peg(peg_a)
    draw_b = draw_peg(peg_b)
    draw_c = draw_peg(peg_c)
    
    draw_a = draw_space(draw_a, tallest_peg, "A")
    draw_b = draw_space(draw_b, tallest_peg, "B")
    draw_c = draw_space(draw_c, tallest_peg, "C")
    print("MOVE: ", turn_count)
    print("""


""")
    for i in range(tallest_peg + 2):
        print("                              ",draw_a[i], "                              ", draw_b[i], "                              ", draw_c[i])

#Runtime:

while True:
    try:
        inp = str(input("Type a for automatic mode or m for manual mode:"))
    except:
        print("You must enter a valid whole number.")
    if inp == "a":
            auto = True
            break
    elif inp == "m":
          auto = False
          break

while True:
     try:
         number_of_disks = int(input("Enter number of disks: "))
     except:
         print("You must enter a valid whole number.")
     if number_of_disks <= 984 and number_of_disks >= 0:
         break
     else:
         print("Use a number in the range 0-984.")

initialize(number_of_disks)
print("DONE!")
print("THIS TOOK ", turn_count, " MOVES")
print("OPTIMAL MOVE COUNT IS ", 2 ** number_of_disks - 1)