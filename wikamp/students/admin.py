from django.contrib import admin
from students.models import Student, Kierunek, KierunekStudenta, Promotor, PracaNaukowa


class KieruinekInline(admin.TabularInline):
    model = KierunekStudenta
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['imie', 'nazwisko']
    list_display = ['id', 'imie', 'nazwisko',]
    inlines = [
        KieruinekInline,
    ]


@admin.register(Kierunek)
class KierunekAdmin(admin.ModelAdmin):
    search_fields = ['nazwa', 'typ']
