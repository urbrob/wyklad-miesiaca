from django.db import models


class Kierunek(models.Model):
    STACJONARNY = 'stacjonarny'
    NIESTACJONARNY = 'niestacjonarny'
    TYPY = (
        (STACJONARNY, 'Stacjonarne'),
        (NIESTACJONARNY, 'Niestacjonarne')
    )
    nazwa = models.CharField(max_length=50,)
    typ = models.CharField(max_length=50, choices=TYPY)

    def __str__(self):
        return self.nazwa


class KierunekStudenta(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='wybrane_kierunki')
    kierunek = models.ForeignKey(Kierunek, on_delete=models.CASCADE, related_name='studenci')



class Student(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    kierunki = models.ManyToManyField(Kierunek, through=KierunekStudenta)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class Promotor(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    stopien = models.CharField(max_length=50)


class PracaNaukowa(models.Model):
    WYDANA = 'wydana'
    TWORZONA = 'tworzona'
    PLAGIAT = 'plagiat'
    STATUSY = (
        (WYDANA, 'Wydana'),
        (TWORZONA, 'Tworzona'),
        (PLAGIAT, 'PLAGIAT 💩')
    )
    tytul = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUSY)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='prace_naukowe')
    promotor = models.ForeignKey(Promotor, on_delete=models.SET_NULL, null=True, related_name='prace_naukowe')
