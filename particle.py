import random


class Particle:

    def __init__(self, n, arr):
        self.n = n
        self.position = arr.copy()
        self.velocity = [0 for i in range(n)]
        self.pbest = arr.copy()

    def update_velocity(self, gbest, c0, c1, c2, r1, r2):
        # print(self.velocity, c0, c1, c2, r1, r2)
        for i in range(self.n):
            # print((gbest[i] - self.position[i]))
            self.velocity[i] = self.velocity[i] * c0 + c1 * r1 * (self.pbest[i] - self.position[i]) + c2 * r2 * (gbest[i] - self.position[i])
        # print(self.velocity)

    def update_position(self, gbest):
        cs = [0 for i in range(self.n)]
        for i in range(self.n):
            cs[self.position[i]] = i
        max_v = max(self.velocity)
        probability = [1 if max_v == 0 else abs(i) / max_v for i in self.velocity]
        for i in range(self.n):
            j = cs[gbest[i]]
            if j != i and random.random() < probability[i]:
                self.position[i], self.position[j] = self.position[j], self.position[i]
                cs[i], cs[j] = cs[j], cs[i]
