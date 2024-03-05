import csv
import json
import os

import pandas as pd
from django.conf import settings

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
    with open(f"{path}/PRD_CSV.csv", encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append({
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

    json.load(f)


# def AddPrdToDB(data):
#     Name = data["Name"]
#     Bnd = data["Brand"]
#     BasePrice = data["BasePrice"]
#     Description = data["Description"]
#     Demo = data["Demo"]
#     Guar = data["Guarantee"]
#     CT = data["Category"]
#     try:
#         prd = Product.objects.get(Name=Name, Brand__Name=Bnd)
#         try:
#             if prd.Guarantee.Name != Guar:
#                 try:
#                     gua = Guarantee.objects.get(Name=Guar)
#                 except:
#                     gua = Guarantee()
#                     gua.Name = Guar
#                     gua.save()
#                 prd.Guarantee = gua

#                 Product.objects.filter(pk=prd.pk).update(
#                     Guarantee=gua,
#                 )
#         except:
#             pass
#         try:
#             if prd.Category_id != int(CT):
#                 cat = Category.objects.get(pk=int(CT))
#                 prd.Category = cat
#                 BasePrice *= (100 + cat.Commission) / 100
#                 BasePrice = roundUp(BasePrice)
#                 Product.objects.filter(pk=prd.pk).update(
#                     Guarantee=gua,
#                     Category=cat,
#                     BasePrice=BasePrice,
#                 )
#         except:
#             pass
#         cat = prd.Category

#     except:
#         try:
#             brand = Brand.objects.get(Name=Bnd)
#         except:
#             brand = Brand()
#             brand.Name = Bnd
#             brand.save()

#         try:
#             gua = Guarantee.objects.get(Name=Guar)
#         except:
#             gua = Guarantee()
#             gua.Name = Guar
#             gua.save()

#         try:
#             cat = Category.objects.get(pk=int(CT))
#             BasePrice *= (100 + cat.Commission) / 100
#             BasePrice = roundUp(BasePrice)
#             prd = Product.objects.create(
#                 Category=cat,
#                 Name=Name,
#                 BasePrice=BasePrice,
#                 Demo=Demo,
#                 Guarantee=gua,
#                 Brand=brand,
#                 Status=ProductStat.check,
#             )
#         except:
#             prd = Product.objects.create(
#                 Name=Name,
#                 BasePrice=BasePrice,
#                 Demo=Demo,
#                 Guarantee=gua,
#                 Brand=brand,
#                 Status=ProductStat.check,
#             )
#         Type = "Product"
#         date = jdatetime.datetime.now().strftime("%Y%m%d")
#         RP = f"RP-{date}{prd.pk}"
#         inp = Digits()
#         inpu = Digits()
#         slug = Slugify(Type, inp, inpu)
#         ref = REFFERER
#         name = "Qr-" + str(RP) + ".png"
#         path = f"Product/{RP}/{name}"
#         root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
#         root = f"{settings.MEDIA_ROOT}/Products/{RP}/{name}"
#         dir = f"{settings.MEDIA_ROOT}/Products/{RP}"
#         url = f"{ref}product/" + str(slug)
#         qr = qrcode.make(url)
#         if os.path.exists(dir):
#             qr.save(root)
#         else:
#             os.makedirs(dir)
#             qr.save(root)
#         Product.objects.filter(pk=prd.pk).update(
#             QrCode=path,
#             RP=RP,
#             Slug=slug,
#         )

#     try:
#         Vars = data["Vars"]
#         for item in Vars:
#             try:
#                 var = Variety.objects.get(
#                     Product=prd,
#                     ColorCode=item["ColorCode"],
#                     ColorName=item["ColorName"],
#                 )
#             except:
#                 var = Variety.objects.create(
#                     Product=prd,
#                     ColorCode=item["ColorCode"],
#                     ColorName=item["ColorName"],
#                 )
#             for s in item["Subs"]:
#                 FinalPrice = int(s["FinalPrice"] * (100 + cat.Commission) / 100)
#                 FinalPrice = roundUp(FinalPrice)
#                 try:
#                     Dis = s["Discount"]
#                     FinalPrice *= (100 - Dis) / 100
#                 except:
#                     Dis = 0

#                 if "Size" in s:
#                     if VarietySub.objects.filter(Size=s["Size"], Variety=var).exists():
#                         VarietySub.objects.filter(Size=s["Size"], Variety=var).update(
#                             FinalPrice=FinalPrice,
#                             Quantity=s["Quantity"],
#                             Discount=Dis,
#                             Size=s["Size"],
#                         )
#                     else:
#                         VarietySub.objects.create(
#                             Variety=var,
#                             FinalPrice=FinalPrice,
#                             Quantity=s["Quantity"],
#                             Discount=Dis,
#                             Size=s["Size"],
#                         )
#                 else:
#                     if VarietySub.objects.filter(Variety=var).exists():
#                         VarietySub.objects.filter(Variety=var).update(
#                             FinalPrice=FinalPrice,
#                             Quantity=s["Quantity"],
#                             Discount=Dis,
#                         )
#                     else:
#                         VarietySub.objects.create(
#                             Variety=var,
#                             FinalPrice=FinalPrice,
#                             Quantity=s["Quantity"],
#                             Discount=Dis,
#                         )
#     except:
#         pass
#     try:
#         Imgs = data["Imgs"]
#         for img in Imgs:
#             try:
#                 IM = ProductImage.objects.get(
#                     Product=prd, Image=img["Image"], Primary=img["Primary"]
#                 )
#             except:
#                 if img["Primary"] == True:
#                     ProductImage.objects.filter(Product=prd, Primary=True).update(
#                         Primary=False
#                     )
#                 IM = ProductImage.objects.create(
#                     Product=prd,
#                     Image=img["Image"],
#                     Primary=img["Primary"],
#                 )
#     except:
#         pass
#     try:
#         Techs = data["Techs"]
#         for te in Techs:
#             try:
#                 TE = ProductTech.objects.get(
#                     Product=prd, Name=te["Name"], Value=te["Value"]
#                 )
#             except:
#                 ProductTech.objects.create(
#                     Product=prd, Name=te["Name"], Value=te["Value"]
#                 )
#     except:
#         pass

# endregion
