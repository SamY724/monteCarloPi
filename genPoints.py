
def generatePoints():
    '''
    A function to generate number of random points, this allows multiple tests
    without editing the code
    '''
    try:
        pointAmount = int(input(f"Please input point count to generate: "))
        return pointAmount
    except ValueError:
        print("Only integer amounts please")
        return generatePoints()
