match = 5
mismatch = -4
gap_pen = 2
gap_ext = 1

s1 = "ATTGCACTATAT"
s2 = "TTAGAATGCTTT"

l1 = len(s1)
l2 = len(s2)

inf = -999

M = [[0 for i in range(13)] for j in range(13)]
Ix = [[0 for i in range(13)] for j in range(13)]
Iy = [[0 for i in range(13)] for j in range(13)]

for i in range(1, 13):
  Ix[i][0] = -gap_pen - (i - 1) * gap_ext

for j in range(1, 13):
  Iy[0][j] = -gap_pen - (j - 1) * gap_ext

for i in range(13):
  M[i][0] = inf
  M[0][i] = inf
  Ix[0][i] = inf
  Iy[i][0] = inf

row = 1
col = 1

for i in range(1, 13):
  for j in range(1, 13):
    Ix[i][j] = max(M[i - 1][j] - gap_pen, Ix[i - 1][j] - gap_ext)
    Iy[i][j] = max(M[i][j - 1] - gap_pen, Iy[i][j - 1] - gap_ext)
    if s1[i - 1] == s2[j - 1]:
      M[i][j] = max(M[i - 1][j - 1] + match, Ix[i - 1][j - 1] + match,
                    Iy[i - 1][j - 1] + match)
    else:
      M[i][j] = max(M[i - 1][j - 1] + mismatch, Ix[i - 1][j - 1] + mismatch,
                    Iy[i - 1][j - 1] + mismatch)

for i in range(1, 13):
  for j in range(1, 13):
    pass

for i in range(13):
  print(M[i])

