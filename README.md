# Wykład miesiąca

## O projekcie
##### Wykład Miesiąca to dzielenie się wiedzą praktyków IT z młodymi programistami. W ramach projektu odbywają się cykliczne wykłady online z języka python.
##### Prowadzący: Robert Urbaniak

## Zasady:
1. Nie próbuj psuć innym pracy
2. To Ty mergujesz swoje zadanie JEŚLI zostanie ono zaakceptowane
3. Masz pełne prawo uczyć się na podstawie innych osób więc nie wstydź się podglądać innych rozwiązań!
4. Ale nie kopiuj. W najgorszym razie przepisz ze zrozumieniem.
5. Przez "zrozumienie" mam na myśli opisanie KAŻDEJ LINIJKI komentarzem tak abyś pokazał co się dzieje w tym kodzie :)
6. Zadania należy oddawać do sprawdzenia w formie PR - Pull request
7. Zadania są w 100% nieobowiązkowe, tak samo jak oglądanie wykładów i nauka czegokolwiek.
8. Masz pełne prawo zadawać pytania "Dlaczego tak?", "Po co?", "Jaki to ma cel?" do moich komentarzy odnośnie Twojego zadania
9. A nawet obowiązek :)

## Aby stać się kursantem:
1. Pobierz repo za pomocą komendy `git clone https://github.com/urbrob/wyklad-miesiaca.git`
2. Stwórzy własny branch `git checkout -b student/<imie>-<nazwisko>`
3. Dodaj folder o następującej nazwie `<imie>-<nazwisko>` do folderu wyklad-miesiaca
4. Stwórz plik tekstowy w powyższym folderze i napisz w nim coś o sobie
5. Dodaj pliki w konsoli `git add --all`
6. Stwórz nową zmianę za pomocą komendy `git commit -m 'Signup'`
7. Wyślij commit `git push origin student/<imie>-<nazwisko>`
8. Wjedź do repozytorium i stwórz nowy PR
9. Done :)

## Aby dodać nowe zadanie:
1. Przejdź na branch master `git checkout master`
2. Stwórz nową branch `git checkout -b exercise/<imie>-<nazwisko>-<nazwa_zadania>`
3. Wykonaj brawurowo zadanie
4. Dodaj pliki do commita `git add --all`
5. Stwórz commit `git commit -m '<opis_co_zostało_dodane>`
6. Wyślij zmianę do repo `git push origin exercise/<imie>-<nazwisko>-<nazwa_zadania>`
7. Wejdź do repo (tu jesteś)
8. Przjedź do zakładki `Pull requests` -> `New pull request`
9. Wybierz swoją branch, która ma zostać zmergowana, dodaj opis, tytuł i jeśli wszystko gotowe to daj mnie do `Reviewers`
10. Czekaj na werdykt :)
