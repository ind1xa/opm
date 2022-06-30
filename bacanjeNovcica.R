##############################
##############################
### Bacanje novcica - JZVB ###
##############################
##############################

# na početku postavljamo seed kako bismo mogli replicirati rezultate
set.seed(34158)

# prvo simuliramo uzorak duljine "n" iz uniformne razdiobe na [0, 1]
n = 100^3 # 10000, 1000000
pom_uzorak = runif(n, min = 0, max = 1)

# Bernoullijevu slučajnu varijablu simuliramo pomoću uzorka iz U(0, 1)
bacanje_novcica = pom_uzorak > 0.5

# Procjena nakon n bacanja
sum(bacanje_novcica) / n

# Ilustracija JZVB
parc_sum = cumsum(bacanje_novcica)
plot(1:n, parc_sum / (1:n), type = "l", ylim = c(0.4, 0.6))   #l = line
abline(1/2, 0, col = "red")

