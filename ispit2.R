n = 10000

set.seed(1156517)
X = runif(n, min = 0, max = Inf)

Y = (exp(sin(X)-X))

proc_n = cumsum(Y) / (1:n)

mean(Y)

plot(1:n, proc_n, type = "l")
# Numericka integracija
g = function(x){
  return(exp(sin(x)-x))
}

num_val = integrate(g, lower = 0, upper = Inf)$value

abline(num_val, 0, col = "red")

