library(readxl)
dir()

podaci = as.data.frame(read_excel("Documents/fer/drugagod/opm/vjerojatnost/podaci.xlsx"))
broj_natjecatelja = nrow(podaci)

broj_simulacija = 100000
broj_pobjeda = rep(0, broj_natjecatelja)

for(sim in 1:broj_simulacija){
  if(sim %% 10000 == 0)
    print(sim)
  rezultati = rep(0, broj_natjecatelja)
  for(i in 1:broj_natjecatelja){
    skokovi = rnorm(3, mean = podaci$prosjecna_udaljenost[i],
                    sd = podaci$standardna_devijacija[i])
    prijestupi = rbinom(3, size = 1, prob = podaci$vjerojatnost_prijestupa[i])
    rezultati[i] = max(skokovi * prijestupi)
  }
  pobjednik = which.max(rezultati)
  # ako nitko nema uspješan skok, pobjednik je prvi natjecatelj
  # ako ih više ima isti rezultat, pobjednik je onaj koji je bolje stajao prije natjecanja
  broj_pobjeda[pobjednik] = broj_pobjeda[pobjednik] + 1
}

broj_pobjeda / broj_simulacija
plot(1:broj_natjecatelja, broj_pobjeda / broj_simulacija, type = "l")
