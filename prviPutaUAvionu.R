##############################
##### Prvi puta u avionu #####
##############################

jedna_simulacija = function(n){
  zauzeta_mjesta = rep(0, n)
  brojevi_mjesta = sample.int(n, size = n, replace = FALSE)
  prvi_putnik = sample.int(n, size = 1)
  zauzeta_mjesta[prvi_putnik] = 1
  for(i in 2:n) {
    if((i == n) & (zauzeta_mjesta[brojevi_mjesta[n]] == 1))
      return(0)
    if((i == n) & (zauzeta_mjesta[brojevi_mjesta[n]] == 0))
      return(1)
    if(zauzeta_mjesta[brojevi_mjesta[i]] == 1){
      odabrano_mjesto = sample(which(zauzeta_mjesta == 0), size = 1)
      zauzeta_mjesta[odabrano_mjesto] = 1
    }
    if(zauzeta_mjesta[brojevi_mjesta[i]] == 0)
      zauzeta_mjesta[brojevi_mjesta[i]] = 1
  }
}


broj_putnika = 100
broj_simulacija = 100000
uspjeh = rep(0, broj_simulacija)

for(s in 1:broj_simulacija){
  uspjeh[s] = jedna_simulacija(broj_putnika)
  if(s %% 10000 == 0)
    print(s)
}

uspjeh
mean(uspjeh)
plot(1:broj_simulacija, cumsum(uspjeh) / (1:broj_simulacija), type = "l", ylim = c(0.4, 0.6))
abline(1/2, 0, col = "red")