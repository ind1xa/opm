#######################################################
#######################################################
##### 1. način računanja stacionarne distribucije #####
#######################################################
#######################################################

##### Matrica prijelaznih vjerojatnosti
P = matrix(c(0.5, 0.4, 0.1,
             0.3, 0.4, 0.3,
             0.2, 0.3, 0.5),
           nrow = 3, byrow = T)

##### Matrica sustava A
A = t(P) - diag(rep(1, 3))
A = rbind(A, rep(1, 3))
A

##### Vektor b
b = c(0, 0, 0, 1)
b

##### Rješavanje sustava Ax = b
solve(A, b)      # solve radi samo s kvadratnim matricama
qr.solve(A, b)

#####
stac_dist_1 = qr.solve(A, b)
sum(stac_dist_1)



#######################################################
#######################################################
##### 2. način računanja stacionarne distribucije #####
#######################################################
#######################################################

eigen(t(P))
eigen(t(P))$vectors
eigen(t(P))$vectors[, 1]

stac_dist_2 = eigen(t(P))$vectors[, 1] / sum(eigen(t(P))$vectors[, 1])

stac_dist_1
stac_dist_2
sum((stac_dist_1 - stac_dist_2)^2)
