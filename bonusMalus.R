###############################################
###############################################
### Ross - Example 4.7 (Bonus-Malus system) ###
###############################################
###############################################

###############################################################################
### Simulacija evolucije Markovljevog lanca preko simuliranja broja odšteta ###
###############################################################################

sljedece_stanje = function(trenutno_stanje, broj_odsteta, S){
  if(broj_odsteta >= 3)
    return(4)
  return(S[trenutno_stanje, broj_odsteta + 1])
}



lambda = 1/2
broj_koraka = 1000000
kretanje_lanca = rep(0, broj_koraka + 1)
kretanje_lanca[1] = 4

S = matrix(c(1, 2, 3, 4,
             1, 3, 4, 4,
             2, 4, 4, 4,
             3, 4, 4, 4), nrow = 4, byrow = T)

for (i in 2:(broj_koraka + 1)){
  broj_odsteta = rpois(1, lambda)
  kretanje_lanca[i] = sljedece_stanje(kretanje_lanca[i - 1], broj_odsteta, S)
}

# plot(0:broj_koraka, kretanje_lanca, type = "l")

table(kretanje_lanca) / (broj_koraka + 1)
