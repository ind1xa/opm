###############################
###############################
### Monte Carlo integracija ###
###############################
###############################


##############################################
### \int_0^1 \frac{e^x \sin x}{1 + x^2} dx ###
##############################################
n = 1000

set.seed(1156517)
X = runif(n, min = 0, max = 1)

Y = (exp(X) * sin(X)) / (1 + X^2)

# Ilustracija JZVB
parc_sum = cumsum(Y)
proc_n = parc_sum / (1:n)

plot(1:n, proc_n, type = "l")

# Numericka integracija
g = function(x){
  return((exp(x) * sin(x)) / (1 + x^2))
}
num_val = integrate(g, lower = 0, upper = 1)$value

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
abline(0.608087, 0, col = "red")

### Ove granice u prvom prolazu kroz kod ignorirati
lines(proc_n + 2 * stderr_n, col = "blue")
lines(proc_n - 2 * stderr_n, col = "blue")