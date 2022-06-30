############################################
############################################
### Ross - Example 4.11 (kulgice i urne) ###
############################################
############################################

P = matrix(c(1/8, 7/8, 0, 0,
             0, 2/8, 6/8, 0,
             0, 0, 3/8, 5/8,
             0, 0, 0, 1), nrow = 4, byrow = T)

install.packages("expm")
library(expm)
P8 = P %^% 8
P8[1, 3]


############################################
### Simulacija ubacivanja kuglica u urne ###
############################################

# Prvo pišemo funkciju kojom simuliramo jedan pokus ubacivanja
# k kuglica u n urni i pitamo se koliko je urni neprazno

broj_nepraznih_urni = function(k, n){
  odabrane_urne = sample.int(n, size = k, replace = TRUE)
  return(length(unique(odabrane_urne)))
}

set.seed(1415)
k = 200 # 200 # 9     #broj kuglica
n = 100 # 100 # 8     #broj urni
trazeni_broj_nepraznih = 80 # 80 # 3
broj_simulacija = 100000
neprazne_urne = rep(0, broj_simulacija)

for(i in 1:broj_simulacija)
  neprazne_urne[i] = broj_nepraznih_urni(k, n)

# Grafički prikaz
indeksi_trazenih_urni = (neprazne_urne == trazeni_broj_nepraznih)

plot(1:broj_simulacija, cumsum(indeksi_trazenih_urni) / (1:broj_simulacija),
     type = "l")
#abline(P8[1, 3], 0, col = "red")
sum(neprazne_urne == trazeni_broj_nepraznih) / broj_simulacija


##### Egzaktno rješenje u slučaju 100 urni
P = matrix(rep(0, (trazeni_broj_nepraznih + 1)^2),
           nrow = trazeni_broj_nepraznih + 1)
diag(P) = (1 : (trazeni_broj_nepraznih + 1)) / n
P[trazeni_broj_nepraznih + 1, trazeni_broj_nepraznih + 1] = 1
i = 1:trazeni_broj_nepraznih
j = 2:(trazeni_broj_nepraznih + 1)
P[cbind(i, j)] = 1 - P[cbind(i, i)]

egzaktno_rjesenje = (P %^% (k - 1))[1, trazeni_broj_nepraznih]

plot(1:broj_simulacija, cumsum(indeksi_trazenih_urni) / (1:broj_simulacija),
     type = "l")
abline(egzaktno_rjesenje, 0, col = "red")