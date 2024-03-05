import csv
import json
import os
from time import sleep

import pandas as pd
from django.conf import settings

from Main.models import Dataset

# import math

# from time import sleep

# region EXToJs
# Convert XlSX to Json


def EXToJs(file):
    try:
        os.makedirs(os.path.join(settings.MEDIA_ROOT, "Excel"))
    except BaseException:
        pass
    path = os.path.join(settings.MEDIA_ROOT, "Excel")
    f = pd.read_excel(
        file,
        sheet_name=[
            "titanic",
        ],
    )
    AP = f.get("titanic")
    AP.to_csv(f"{path}/Titanic_CSV.csv", encoding="utf-8", index=False)
    data = []
    with open(f"{path}/Titanic_CSV.csv", encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append({
                "PassengerId": rows["PassengerId"],
                "Survived": rows["Survived"],
                "Pclass": rows["Pclass"],
                "Name": rows["Name"],
                "Sex": rows["Sex"],
                "Age": rows["Age"],
                "SibSp": rows["SibSp"],
                "Parch": rows["Parch"],
                "Ticket": rows["Ticket"],
                "Fare": rows["Fare"],
                "Cabin": rows["Cabin"],
                "Embarked": rows["Embarked"],
            })

    with open(f"{path}/file.json", "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


# endregion

# region New Products Proccess


def NewProccess(file):
    EXToJs(file)
    path = os.path.join(settings.MEDIA_ROOT, "Excel")

    f = open(f"{path}/file.json")

    js = json.load(f)
    for item in js:
        try:
            AddToDB(item)
            sleep(0.25)
        except BaseException:
            pass


def AddToDB(data):
    PassengerId = data["PassengerId"]
    Pclass = data["Pclass"]
    Survived = data["Survived"]
    Name = data["Name"]
    Sex = data["Sex"]
    Age = data["Age"]
    SibSp = data["SibSp"]
    Parch = data["Parch"]
    Ticket = data["Ticket"]
    Fare = data["Fare"]
    Cabin = data["Cabin"]
    Embarked = data["Embarked"]
    try:
        Dataset.objects.get(PassengerId=PassengerId)
    except BaseException:
        Dataset.objects.create(
            PassengerId=PassengerId,
            Survived=Survived,
            Pclass=Pclass,
            Name=Name,
            Sex=Sex,
            Age=Age,
            SibSp=SibSp,
            Parch=Parch,
            Ticket=Ticket,
            Fare=Fare,
            Cabin=Cabin,
            Embarked=Embarked,
        )


# endregion
