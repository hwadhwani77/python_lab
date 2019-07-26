def countJewels(J, S):
    return sum([S.count(j) for j in J])

J = "aA"
S = "aAAbbbb"
# print(countJewels(J, S))
s = set("aeiou")
print(s)