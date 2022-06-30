n = 100000000
set.seed(1627)

correct = rep(0, n)

x = runif(n, min = 0, max = 1)
y = runif(n, min = 0, max = 1)
 
for (i in 1:n)
  if (x[i]*x[i]+y[i]*y[i] <= 1)
    correct[i] = 1
  
pi = sum(correct)/n *4
pi