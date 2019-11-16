from particle import Particle
from frequency import Frequency, plaintext
from substitution import Substitution
import random


# Parameters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
true_key = "BCDAEFGLKJIHOMNQPRSWVUTYZX"
n_gram = [1, 2]
alpha = [1, 3]
c0 = 0
c1 = 3
c2 = 2

# n_gram statistics
n_gram_files = ["english_monograms.txt", "english_bigrams.txt"]
target = Frequency(n_gram, alphabet)
target.get_frequency_from_file(n_gram_files)
# target.get_frequency(open("text_original.txt", "r").read())

# Create cypher text from originaltext_file
originaltext_file = "text_original.txt"
originaltext = plaintext(open(originaltext_file, "r").read(), alphabet)
cyphertext = Substitution(alphabet, true_key).encrypt(originaltext)
cyphertext_file = "text_cypher.txt"
open(cyphertext_file, "w").write(cyphertext)

# Initialize population
population_size = 500
swarm = []
arr = [i for i in range(len(alphabet))]
for i in range(population_size):
    random.shuffle(arr)
    swarm.append(Particle(len(alphabet), arr))


# PSO
def fitness(position):
    key = "".join(alphabet[i] for i in position)
    substitution = Substitution(alphabet, key)
    original_text = substitution.decrypt(cyphertext)
    frequency = Frequency(n_gram, alphabet)
    frequency.get_frequency(original_text)
    res = 0
    for i in range(len(n_gram)):
        for j in range(len(frequency.ftab[i])):
            res += alpha[i] * abs(frequency.ftab[i][j] - target.ftab[i][j])
    return res


max_iter = 200
max_unchanged = 100
cnt_iter = 0
cnt_unchanged = 0
gbest = swarm[0].position.copy()
while cnt_iter < max_iter and cnt_unchanged < max_unchanged:
    cnt_iter += 1
    cnt_unchanged += 1
    print(cnt_iter)
    for particle in swarm:
        if particle.position == gbest:
            random.shuffle(particle.position)

    for particle in swarm:
        if fitness(particle.position) < fitness(particle.pbest):
            particle.pbest = particle.position.copy()
        if fitness(particle.position) < fitness(gbest):
            gbest = particle.position.copy()
            cnt_unchanged = 0
    for particle in swarm:
        particle.update_velocity(gbest, c0, c1, c2, random.random(), random.random())
        particle.update_position(gbest)

    print("Fitness current gbest:", fitness(gbest))
    key = "".join(alphabet[i] for i in gbest)
    print("Current best key:", key)
    result = Substitution(alphabet, key).decrypt(cyphertext)
    print("Current result: ", result)
