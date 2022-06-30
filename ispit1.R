set.seed(872436)


n = 1000000
uspjeli = rep(0, n)

vektorA = rep(1, 70)
vektorB = rep(0, 30)

vektor = c(vektorA, vektorB)

for (sim in 1:n) {
  randomVektor <- sample(vektor)
  brojA = 0
  brojB = 0
  neuspjeh = 0
  for(i in 1:100) {
    if (randomVektor[i] == 1) {
      brojA = brojA + 1
    }
    else {
      brojB = brojB + 1
    }
    if (brojB >= brojA) {
      neuspjeh = 1
      break
    }
  }
  if (!neuspjeh) {
    uspjeli[sim] = 1
  }
}

vjerojatnost = sum(uspjeli) / n
vjerojatnost
