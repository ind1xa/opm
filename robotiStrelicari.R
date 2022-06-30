#################################################################
### Funkcija koja simulira jedno natjecanje u kojem sudjeluje ###
### "broj_robota" robota te vraća redni broj robota koji je   ###
### pobijedio na natjecanju.                                  ###
#################################################################

jedna_runda = function(broj_robota){
  trenutni_najbolji_rezultat = runif(1)
  u_igri = rep(1, broj_robota)
  i = 1
  while (1) {
    if(sum(u_igri) == 1)
      break
    i = (i + 1) %% broj_robota
    if(i == 0)
      i = broj_robota
    if(u_igri[i]){
      rezultat = runif(1)
      if(rezultat > trenutni_najbolji_rezultat)
        u_igri[i] = 0
      else
        trenutni_najbolji_rezultat = rezultat
    }
  }
  return(which(u_igri == 1))
}



#### Postavljamo seed da možemo rekonstruirati rezultate
set.seed(1153115)

#### Odabiremo broj robota koji sudjeluju u natjecanju i broj natjecanja koje ćemo simulirati
broj_robota = 2
broj_simulacija = 50000
broj_pobjeda = rep(0, broj_robota)
for(sim in 1:broj_simulacija){
  pobjednik = jedna_runda(broj_robota)
  broj_pobjeda[pobjednik] = broj_pobjeda[pobjednik] + 1
}

broj_pobjeda
broj_pobjeda / broj_simulacija

plot(1:broj_robota, broj_pobjeda/broj_simulacija, type = "b",
     xlab = "Robot", ylab = "Udio pobjeda")
