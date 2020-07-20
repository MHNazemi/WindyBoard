from interfaces import IAi
import numpy as np
import math
import random


class MC(IAi.IAi):
    def __init__(self, player, s, a):
        self.s = s
        self.a = a
        self.Q = np.zeros((s, len(a)))
        self.N = np.zeros((s, len(a)))
        self.k = 1
        self.player = player
        self.states = {}
        self.actions = {}
        self.reverseActions = {}
        r = math.sqrt(self.s)
        self.visitedStates = []
        self.visitedRewards = []
        self.visitedActions = []
        i = 0
        for x in range(-int(r//2), int(r//2)):
            for y in range(-int(r//2), int(r//2)):
                self.states[str(x)+str(y)] = i
                i += 1

        i = 0
        for a_ in a:
            self.actions[a_] = i
            self.reverseActions[i] = a_
            i += 1

    def apply(self, reward=None, exclude=None):
        x, y = self.player.getCurrentPos()

        # random or greedy
        r = random.random()
        args = list(np.argsort(-self.Q[self.states[str(x)+str(y)]]))
        for e_ in exclude:
            args.remove(self.actions[e_])
        if r > 1/self.k:
            # greedy
            # args = np.argsort(-self.Q[self.states[str(x)+str(y)]])
            # for e_ in exclude:
            #     args.remove(self.actions[e_])

            valMax = self.Q[self.states[str(x)+str(y)]][args[0]]
            candidates = []
            for arg in args:
                if self.Q[self.states[str(x)+str(y)]][arg] == valMax:
                    candidates.append(arg)
                    continue

            selectedArg = random.choice(candidates)
            action = self.reverseActions[selectedArg]

        else:
            selectedArg = random.choice(args)
            action = self.reverseActions[selectedArg]

        if reward != None:
            self.visitedRewards.append(reward)

        self.visitedStates.append(self.states[str(x)+str(y)])
        self.visitedActions.append(selectedArg)

        self.N[self.states[str(x)+str(y)]][selectedArg] += 1
        print(action)
        return action

    def endEpisode(self, reward):
        x, y = self.player.getCurrentPos()
        self.visitedRewards.append(reward)
        self.visitedStates.append(self.states[str(x)+str(y)])

        G = 0
        for i in range(len(self.visitedRewards)-1, -1, -1):
            self.visitedStates[i]
            self.visitedActions[i]

            G += self.visitedRewards[i]
            self.Q[self.visitedStates[i]][self.visitedActions[i]
                                          ] += (1/self.N[self.visitedStates[i]][self.visitedActions[i]]) * (G - self.Q[self.visitedStates[i]][self.visitedActions[i]])

        self.N = np.zeros((self.s, len(self.a)))
        self.visitedStates = []
        self.visitedRewards = []
        self.visitedActions = []

        self.k += 1
