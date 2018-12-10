from random import randint

class Node:

    def __init__(self, initialR, maxRetransmissionAttempt):
        self.initialR = initialR
        self.R = initialR
        self.maxRetransmissionAttempt = maxRetransmissionAttempt
        self.retransmissionLeft = maxRetransmissionAttempt
        self.backoff = randint(0, self.R)
        self.successfulTransmissions = 0
        self.collosions = 0

    def dropAPacket(self):
        if self.retransmissionLeft > 0:
            self.retransmissionLeft -= 1
            self.R = self.R * 2
            self.backoff = randint(0, self.R)
        else:
            self.getANewPacket()

    def getANewPacket(self):
        self.R = self.initialR
        self.retransmissionLeft = self.maxRetransmissionAttempt
        self.backoff = randint(0, self.R)

    def getBackoff(self):
        return self.backoff

    def countDown(self):
        if self.backoff > 0:
            self.backoff -= 1
