###############################
###############################
### Monte Carlo integracija ###
###############################
###############################

################################################
### \int_{-1}^{2} \frac{x * ln(x^2 + 4)}{2^x} ###
################################################

n = 10000
set.seed(1627)

a = -1
b = 2
X = runif(n, min = a, max = b)

Y = 3 * (X * log(X^2 + 4)) / (2^X)


# Ilustracija JZVB
parc_sum = cumsum(Y)
proc_n = parc_sum / (1:n)

plot(1:n, proc_n, type = "l")

# Numericka integracija
f = function(x){
  return((x * log(x^2 + 4)) / (2^x))
}
num_val = integrate(f, lower = -1, upper = 2)$value

abline(num_val, 0, col = "red")

# Procjena nakon n koraka
mean(Y)

# Numerička vrijednost
num_val

# Pouzdani intervli
stderr_n = rep(0, n)
for(i in 1:n)
  stderr_n[i] = sd(Y[1:i]) / sqrt(i)

# Graficki prikaz
plot(1:n, proc_n, type = "l", ylim = mean(Y) + 20*c(-stderr_n[n], stderr_n[n]))
abline(0.215895, 0, col = "red")

### Ove granice u prvom prolazu kroz kod ignorirati
lines(proc_n + 2 * stderr_n, col = "blue")
lines(proc_n - 2 * stderr_n, col = "blue")
