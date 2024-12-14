import logic
import testcase
from colorama import Fore, Style, init

def testTestcase(i):
    maze_attr = f"maze{i}"
    ball_attr = f"ball{i}"
    hole_attr = f"hole{i}"
    
    maze = getattr(testcase, maze_attr)
    ball = getattr(testcase, ball_attr)
    hole = getattr(testcase, hole_attr)
    
    solution = logic.findShortestWay(maze, ball, hole)
    if solution == "impossible":
        print(f"The solution is impssoble")
        return
    
    currentBall = ball
    logic.printMaze(maze, currentBall, hole)
    for e in solution:
        currentBall = logic.takeAction(maze, currentBall, e)
        logic.printMaze(maze, currentBall, hole)
    print(f"We need to take {len(solution)} actions to achieve target")
    print("Here is our solution direction")
    idx=0
    for e in solution:
        idx+=1
        print(f"step {idx}:",logic.mapDirection(e))

if __name__ == "__main__":
    print("Welcome to our main.py. If you want to leave, just type anything that will cause error.")
    print("------------------------------")
    print('To see preview map. Type, "prev <testcase number>"')
    print('To see the solution. Type, "solve <testcase number>"')
    while True:
        print("------------------------------")
        try:
            command, testcaseNumber = input("input your command: ").split()
            if command == "prev":
                maze_attr = f"maze{testcaseNumber}"
                ball_attr = f"ball{testcaseNumber}"
                hole_attr = f"hole{testcaseNumber}"
    
                maze = getattr(testcase, maze_attr)
                ball = getattr(testcase, ball_attr)
                hole = getattr(testcase, hole_attr)

                logic.printMaze(maze, ball, hole, line = False)
            elif command == "solve":    
                testTestcase(testcaseNumber)
            else:
                print("Invalid command!")
        except:
            break