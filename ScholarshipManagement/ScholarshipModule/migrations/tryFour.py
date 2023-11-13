# Generated by Django 4.2.5 on 2023-11-13 02:05

from django.db import migrations
from ..models import *
from django.contrib.auth.hashers import make_password
from ..models import ScholarsipTypes


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0007_alter_scholarsiptypes_scholarship'),
    ]

    def insert_default_values(apps, schema_editor):

        usersValues = [
            ["0","admin@gmail.com", "Admin", "ADMIN"],
            ["1","financial@gmail.com", "Financial", "FINANCIAL"],
            ["2","philanthropy@gmail.com", "Philanthropy", "PHILANTHROPY"],
            ["3","default@gmail.com", "Default", "DEFAULT"]]

        for user in usersValues:
            if user[0] == "0":
                User(username = user[1], name = user[2], password = make_password(user[3]), role = 0).save()
            elif user[0] == "1":
                User(username = user[1], name = user[2], password = make_password(user[3]), role = 1).save()
            elif user[0] == "2":
                User(username = user[1], name = user[2], password = make_password(user[3]), role = 2).save()
            else:
                User(username = user[1], name = user[2], password = make_password(user[3]), role = 3).save()

        donorsValues = [
            "John Doe",
            "Alice Johnson",
            "Robert Smith",
            "Emily Davis",
            "Michael Brown",
            "Samantha White",
            "Christopher Lee",
            "Olivia Taylor",
            "Daniel Miller",
            "Sophia Anderson"
        ]


        for donor in donorsValues:
            Donors(name = donor).save()

        scholarshipsValues = [
            [1, "Beca de Mérito", "Beca para logros académicos destacados", 1, "Promedio superior a 3.5", False],
            [2, "Beca Basada en Necesidades", "Ayuda financiera para estudiantes con necesidades", 2, "Demostrar necesidad financiera", False],
            [3, "Beca de Excelencia en STEM", "Apoyo a estudiantes en disciplinas STEM", 3, "Carrera en una disciplina STEM", False],
            [4, "Subvención de Artes y Humanidades", "Financiamiento para estudiantes en artes y humanidades", 4, "Carrera en artes o humanidades", False],
            [5, "Premio de Servicio Comunitario", "Reconocimiento por servicio comunitario destacado", 5, "Horas documentadas de servicio comunitario", False],
            [6, "Beca de Ciudadanía Global", "Apoyo a estudiantes con una perspectiva global", 6, "Compromiso demostrado con problemas globales", False],
            [7, "Subvención de Excelencia en Liderazgo", "Financiamiento para líderes estudiantiles", 7, "Experiencia comprobada en liderazgo", False],
            [8, "Beca de Ciencias de la Salud", "Apoyo a estudiantes en ciencias de la salud", 8, "Carrera en ciencias de la salud", False],
            [9, "Premio de Conciencia Ambiental", "Reconocimiento por compromiso con problemas ambientales", 9, "Iniciativas ambientales documentadas", False],
            [10, "Subvención de Tecnología e Innovación", "Financiamiento para estudiantes en tecnología e innovación", 10, "Carrera en tecnología o campo relacionado", False]
        ]


        for scholarship in scholarshipsValues:
            Scholarships(id = scholarship[0], name = scholarship[1], description = scholarship[2], requirements = scholarship[4], donor_id = scholarship[3], isDeleted = scholarship[5]).save()

        typesValues = [
            [1, ScholarsipTypes.SchUnit.PERCENTAGE, 50.0, "Descuento"],
            [1, ScholarsipTypes.SchUnit.MONEY, 1000.0, "Monto Fijo"],
            [2, ScholarsipTypes.SchUnit.MONEY, 500.0, "Ayuda Financiera"],
            [3, ScholarsipTypes.SchUnit.PERCENTAGE, 40.0, "Descuento"],
            [4, ScholarsipTypes.SchUnit.MONEY, 800.0, "Monto Fijo"],
            [5, ScholarsipTypes.SchUnit.PERCENTAGE, 30.0, "Descuento"],
            [6, ScholarsipTypes.SchUnit.MONEY, 1200.0, "Monto Fijo"],
            [7, ScholarsipTypes.SchUnit.PERCENTAGE, 25.0, "Descuento"],
            [8, ScholarsipTypes.SchUnit.MONEY, 900.0, "Monto Fijo"],
            [9, ScholarsipTypes.SchUnit.PERCENTAGE, 20.0, "Descuento"],
            [10, ScholarsipTypes.SchUnit.MONEY, 1100.0, "Monto Fijo"]
        ]

        for type in typesValues:
            ScholarsipTypes(scholarship_id = type[0], unit = type[1], value = type[2], type = type[3])

        
    operations = [
        migrations.RunPython(insert_default_values),
    ]
