#################################
#################################
### Efikasnost MC integracije ###
#################################
#################################

gamma(1.9)

### Aproksimacija vrijednosti gamma(1.9) pomoću eksponencijalne distribucije
n = 1000
set.seed(15361)
exp_uzorak = rexp(n, rate = 1)
f_exp_uzorak = exp_uzorak^(0.9)
mean(f_exp_uzorak)

# Ilustracija JZVB
parc_sum_exp = cumsum(f_exp_uzorak)
proc_n_exp = parc_sum_exp / (1:n)

# Procjena nakon n koraka
mean(f_exp_uzorak)

# Ilustracija
plot(1:n, proc_n_exp, type = "l") 
abline(gamma(1.9), 0, col = "red")

# Pouzdani intervli
stderr_n_exp = rep(0, n)
for(i in 1:n)
  stderr_n_exp[i] = sd(f_exp_uzorak[1:i]) / sqrt(i)

# Graficki prikaz
plot(1:n, proc_n_exp, type = "l",
     ylim = mean(f_exp_uzorak) + 4*c(-stderr_n_exp[n], stderr_n_exp[n])) 
abline(gamma(1.9), 0, col = "black")
lines(proc_n_exp + 2 * stderr_n_exp, col = "blue")
lines(proc_n_exp - 2 * stderr_n_exp, col = "blue")


### Aproksimacija vrijednosti gamma(1.9) pomoću gamma distribucije
n = 1000
set.seed(15361)
gamma_uzorak = rgamma(n, shape = 2, rate = 1)
f_gamma_uzorak = gamma_uzorak^(-0.1)

# Ilustracija JZVB
parc_sum_gamma = cumsum(f_gamma_uzorak)
proc_n_gamma = parc_sum_gamma / (1:n)

# Procjena nakon n koraka
mean(f_gamma_uzorak)

# Pouzdani intervli
stderr_n_gamma = rep(0, n)
for(i in 1:n)
  stderr_n_gamma[i] = sd(f_gamma_uzorak[1:i]) / sqrt(i)

# Graficki prikaz
lines(1:n, proc_n_gamma, col = "green")
lines(proc_n_gamma + 2 * stderr_n_gamma, col = "red")
lines(proc_n_gamma - 2 * stderr_n_gamma, col = "red")


legend(600, 0.92, legend=c("Exp", "Gamma"),
       col=c("black", "green"), lty=c(1, 1), cex=0.9)