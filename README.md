# 3Soft - Zadanie rekrutacyjne na stanowisko Data Scientist
## Wprowadzenie
Do prawidłowego funkcjonowania kodu zachęcam do stworzyć wirtualne środowisco `venv` oraz zaimportować wszystkie biblioteki z pliku `requirements.txt`. Pozostałe instrukcje zostały opisane w notatnikach `Jupyter notebook`.

## Rozwiązania zadań:
### Zadanie 1
Napisz funkcję “dt_pred”, która w oparciu o drzewo decyzyjne na podstawie losowego podzbioru obserwacji oraz losowego zestawu atrybutów ze zbioru uczącego zwraca wytrenowanie na podanym zbiorze treningowym drzewo decyzyjne. Odsetek obserwacji oraz odsetek atrybutów wykorzystywanych do uczenia drzewa powinny zostać sparametryzowane. Zadbaj o powtarzalność otrzymywanych wyników. 
##### Rozwiązanie
Rozwiązanie w pliku (`1_drzewo_decyzyjne.ipynb`).

### Zadanie 2
Następnie skonstruuj funkcję “dt_bagg”, która wykorzystywać będzie funkcję “dt_pred” (jako tzw. weak learner) w procedurze baggingu*. Pamiętaj o uwzględnieniu odpowiednich (hiper)parametrów tej funkcji. Jeżeli to możliwe postaraj się zrównoleglić obliczenia. 
##### Rozwiązanie
Rozwiązanie w pliku (`1_drzewo_decyzyjne.ipynb`).

### Zadanie 3
Wykorzystaj napisaną przez siebie funkcję “dt_bagg”, aby na podstawie danych z załączonych plików (pliki “signal.csv”, “time.csv” oraz “descriptive.csv”) zbudować odpowiednie modele prognozujące zmienną “y” za pomocą zmiennych “x_1”-“x_78”. Dokonaj podziału na zbiór treningowy oraz zbiór testowy losując 150 obserwacji.
Porównaj jakość otrzymanych prognoz w oparciu o: 
<ul>
  <li>Wykorzystanie funkcji “dt_bagg” która zbuduje 100 niezależnych drzew, gdzie każde indywidualne drzewo uczone będzie na 80% obserwacji ze zbioru treningowego oraz 80% dostępnych atrybutów </li>
  <li>Wykorzystanie funkcji “dt_bagg” która zbuduje 200 niezależnych drzew, gdzie każde indywidualne drzewo uczone będzie na 70% obserwacji ze zbioru treningowego oraz 50% dostępnych atrybutów </li>
</ul>
Oceń i porównaj na zbiorze testowym jakość prognoz otrzymanych za pomocą obu podejść.
Czy dobór (hiper)parametrów ma wpływ na otrzymywane wyniki? Czy jesteś w stanie zaproponować inny (lepszy) dobór tych parametrów?

*bagging: w procedurze tej budujemy N niezależnych drzew decyzyjnych z których każde uczone jest na pewnym podzbiorze obserwacji ze zbioru uczącego. Przyjmijmy dodatkowo, że każde drzewo decyzyjne uczone będzie na pewnym (losowym) podzbiorze dostępnych predyktorów. Za ostateczną prognozę przyjmij średnią z indywidualnych prognoz N składowych drzew decyzyjnych.
##### Rozwiązanie
Rozwiązanie tego zostało podzielone na 2 etapy: pierwszy polegał na zbadaniu otrzymanych danych (`0_przygotowanie_danych.ipynb`) a następnie przechodzimy do trenowania modelu (`1_drzewo_decyzyjne.ipynb`)

### Zadanie 4 
Przygotuj omówienie zadania oraz otrzymanych wyników w postaci prostej prezentacji na max 10 minut.
##### Rozwiązanie
Całe rozwiązanie oraz przebieg prac zostanie przedstawiony w postaci krótkiej prezentacji w poniedziałek (03.10.2022r.) o godzinie 15 w ramach kolejnego etapu rekrutacji.


