################################################
################################################
### Ross - Example 4.27 (Bonus-Malus system) ###
################################################
################################################

lambda = 1/2

help(dpois)

P = matrix(c(dpois(0, lambda), dpois(1, lambda), dpois(2, lambda), 1 - ppois(2, lambda),
             dpois(0, lambda), 0, dpois(1, lambda), 1 - ppois(1, lambda),
             0, dpois(0, lambda), 0, 1 - dpois(0, lambda),
             0, 0, dpois(0, lambda), 1 - dpois(0, lambda)),
           nrow = 4, byrow = T)


# Izračun stacionarne distribucije
A = t(P) - diag(rep(1, 4))
A = rbind(A, rep(1, 4))
b = c(0, 0, 0, 0, 1)
stac_dist = qr.solve(A, b)


pom = eigen(t(P))$vectors[, 1]
stac_dist2 = pom / sum(pom)

# Izračun prosječne godišnje premije
premije = c(200, 250, 400, 600)
crossprod(premije, stac_dist)
