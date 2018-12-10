import sys
from Node import Node
from numpy import var
from random import choice


def csma(numOfNodes, packetLength, R, maxRetransmissionAttempt, timeOfSimulation, out):
    nodes = [Node(R[0], maxRetransmissionAttempt) for i in range(numOfNodes)]
    nodeOnTransmission = None
    nodesCountDownTo0 = []
    currentPacketLeft = 0
    channelUsed, channelIdle, numOfCollisions = 0, 0, 0

    for i in range(timeOfSimulations):
        # the channel is busy
        if currentPacketLeft != 0:
            currentPacketLeft -= 1
            channelUsed += 1
            # transmission finished, the node get a new packet
            if currentPacketLeft == 0:
                nodeOnTransmission.getANewPacket()
                nodeOnTransmission.successfulTransmissions += 1
                nodeOnTransmission = None
                pass

        # the channel is idle
        else:
            for node in nodes:
                if node.getBackoff() == 0:
                    nodesCountDownTo0.append(node)
            if len(nodesCountDownTo0) > 0:
                if len(nodesCountDownTo0) > 1:
                    for node in nodesCountDownTo0:
                        numOfCollisions += 1
                        node.collosions += 1
                        node.dropAPacket()
                    nodesCountDownTo0 = []
                    channelIdle += 1
                # only one
                else:
                    nodeOnTransmission = nodesCountDownTo0[0]
                    currentPacketLeft = packetLength
                    currentPacketLeft -= 1
                    channelUsed += 1
                    nodesCountDownTo0 = []
                    
            # no count down to 0, all count down
            else:
                for node in nodes:
                    node.countDown()
                channelIdle += 1
    print(channelUsed, channelIdle)
    print("Channel utilization:", "{0:.2%}".format(channelUsed * 1. / timeOfSimulations))
    print("Channel idle fraction:", "{0:.2%}".format(channelIdle * 1. / timeOfSimulations))
    out.writelines("Channel utilization: "+ str("{0:.2%}".format(channelUsed * 1. / timeOfSimulations)) + '\n')
    out.writelines("Channel idle fraction :"+ str("{0:.2%}".format(channelIdle * 1. / timeOfSimulations)) + '\n')
    totalNumOfCollisions = sum([node.collosions for node in nodes])
    print("Total number of collisions:", totalNumOfCollisions)
    out.writelines("Total number of collisions: "+ str(totalNumOfCollisions) + '\n')
    print("Variance in number of successful transmissions:", var([node.successfulTransmissions for node in nodes]))
    print("Variance in number of collisions:", var([node.collosions for node in nodes]))
    out.writelines("Variance in number of successful transmissions: "+ str(var([node.successfulTransmissions for node in nodes])) + '\n')
    out.writelines("Variance in number of collisions: "+ str(var([node.collosions for node in nodes])) + '\n')





with open(sys.argv[1]) as input:
    out = open("output.txt", "w")

    numOfNodes = int(input.readline().strip().split()[1])
    packetLength = int(input.readline().strip().split()[1])
    R = input.readline().strip().split()[1:]
    for i in range(len(R)):
        R[i] = int(R[i])
    maxRetransmissionAttempt = int(input.readline().strip().split()[1])
    timeOfSimulations = int(input.readline().strip().split()[1])
    print(numOfNodes, packetLength, R, maxRetransmissionAttempt, timeOfSimulations)
    csma(numOfNodes, packetLength, R, maxRetransmissionAttempt, timeOfSimulations, out)
    out.close()
