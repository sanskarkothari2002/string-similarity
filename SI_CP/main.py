import re
import numpy
_SPACE_PATTERN = re.compile("\\s+")


def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    print("Distance Table")
    printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]



class consecutiveK:

    def __init__(self, k=3):
        self.k = k

    def get_k(self):
        return self.k

    def get_profile(self, string):
        shingles = dict()
        no_space_str = _SPACE_PATTERN.sub(" ", string)
        for i in range(len(no_space_str) - self.k + 1):
            shingle = no_space_str[i:i + self.k]
            old = shingles.get(shingle)
            if old:
                shingles[str(shingle)] = int(old + 1)
            else:
                shingles[str(shingle)] = 1
        return shingles



class DiceCoefficient(consecutiveK):

    def __init__(self, k=3):
        super().__init__(k)

    def distance(self, s0, s1):
        return 1.0 - self.similarity(s0, s1)

    def similarity(self, s0, s1):
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        if s0 == s1:
            return 1.0
        union = set()
        profile0, profile1 = self.get_profile(s0), self.get_profile(s1)
        for k in profile0.keys():
            union.add(k)
        for k in profile1.keys():
            union.add(k)
        inter = (len(profile0.keys()) + len(profile1.keys()) - len(union))
        return 2.0 * inter / (len(profile0) + len(profile1))

a = DiceCoefficient(2)



n1 = input();
n2 =input();
distance = levenshteinDistanceDP(n1, n2)
sim=1-(distance/max(len(n1),len(n2)))
print("similarity between " + n1 + " and " + n2 + " is ",sim)

n11 = input();
n22 = input();
# print("Dice Coeff: {}".format(a.similarity("125 SW 39TH ST, Suite 10", "Suite 10, 125 SW 39TH ST")))
# print("Dice Coeff: {}".format(a.similarity("上海", "上海市")))
print("similarity index: {}".format(a.similarity(n11,n22)))


