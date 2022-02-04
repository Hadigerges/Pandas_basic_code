import numpy as np
import pandas as pd


#Exercice 1
s = pd.Series([1,5,2,3,7])
print(s)

pyt = []
for i in s:
    pyt.append(i)
print(pyt)


#Exercice 2
yo = []
for i in range(10):
    yo.append(np.random.rand())
print(yo)

s = pd.Series(yo)
print(s)

s1 = pd.Series(s<5)
print(s1)


#Exercice 3
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

print(s1 + s2)
print(s1 - s2)
print(s1 * s1)
print(s1 / s1)


#Exercice 4
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

print(s1 == s2)
print(s1 > s2)
print(s2 > s1)


#Exercice 5
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

s2[4] = 10
print(s1)
print(s2)

print("Compare the elements of the said Series: ")
print("Equals: ")
print(s1[s1 == s2])

print("Greater than: ")
print(s1[s1 > s2])

print("Lesser than: ")
print(s1[s1 < s2])


#Exercice 6
mydict={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(mydict)
s = pd.Series(mydict)
print(s)


#Exercice 7
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])

print(sr1[sr1.isin(sr2)])


#Exercice 8
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])

result = sr1[~sr1.isin(sr2)]
print(result)


#Exercice 9
lst = np.random.randint(10, 20, size=150)
s = pd.Series(lst)
print(s.value_counts())