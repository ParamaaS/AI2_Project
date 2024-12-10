import logic
import testcase

def testTestcase(i):
    maze_attr = f"maze{i}"
    ball_attr = f"ball{i}"
    hole_attr = f"hole{i}"
    
    maze = getattr(testcase, maze_attr)
    ball = getattr(testcase, ball_attr)
    hole = getattr(testcase, hole_attr)
    
    solution = logic.findShortestWay(maze, ball, hole)
    if solution == "impossible":
        return
    
    currentBall = ball
    logic.printMaze(maze, currentBall, hole)
    for e in solution:
        currentBall = logic.takeAction(maze, currentBall, e)
        logic.printMaze(maze, currentBall, hole)

if __name__ == "__main__":
    print("Welcome to our main.py. If you want to leave, just type anything that will cause error.")
    while True:
        try:
            testcaseNumber = int(input("input the testcase I want to test: "))
            testTestcase(testcaseNumber)
        except:
            break