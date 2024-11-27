nom = "ps5"
prix_unitaire = 449.99
quantité_en_stock = 50
prix_inflation = prix_unitaire + prix_unitaire*0.10

print("produit:",nom,"prix:",prix_unitaire,"stock restant:",quantité_en_stock )
print("produit:",nom,"prix:",prix_unitaire,"stock restant:",quantité_en_stock + 10)
x = int(input("saisissez le nombre de produit souhaité:"))
print("produit:",nom,"prix:",prix_unitaire,"stock restant:",quantité_en_stock - x )
print("le prix après l'inflation est de ",prix_inflation,"euros")
