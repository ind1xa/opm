
lambda = 0.75

P = matrix(c(dpois(0, lambda), dpois(1, lambda), dpois(2, lambda), dpois(3, lambda), 1 - ppois(3, lambda),
             dpois(0, lambda), 0, dpois(1, lambda), dpois(2, lambda), 1 - ppois(2, lambda),
             0, dpois(0, lambda), 0, dpois(1, lambda), 1 - ppois(1, lambda),
             0, 0, dpois(0, lambda), 0, 1 - dpois(0, lambda),
             0, 0, 0, dpois(0, lambda), 1 - dpois(0, lambda)),
           nrow = 5, byrow = T)


# Izračun stacionarne distribucije
pom = eigen(t(P))$vectors[, 1]
stac_dist = pom / sum(pom)
### ili
A = t(P) - diag(rep(1, 5))
A = rbind(A, rep(1, 5))

b = c(0, 0, 0, 0, 0, 1)

stac_dist_1 = qr.solve(A, b)

novci = c(200, 250, 400, 600, 900)
crossprod(novci, stac_dist_1)
