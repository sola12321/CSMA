import sys

with open(sys.argv[1]) as input:
    numOfNodes = int(input.readline().strip().split()[1])
    clockTick = int(input.readline().strip().split()[1])
    R = input.readline().strip().split()[1:]
    for i in range(len(R)):
        R[i] = int(R[i])
    maxRetransmissionAttempt = int(input.readline().strip().split()[1])
    TimeOfSimulations = int(input.readline().strip().split()[1])
    print(numOfNodes, clockTick, R, maxRetransmissionAttempt, TimeOfSimulations)
