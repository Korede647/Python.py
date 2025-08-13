payment_method = ("visa", "master", "verve", "bitcoin", "gift card")

print(len(payment_method))
print(payment_method[0])
payment_method[1] = "cash"
print(payment_method)

for pm in range(len(payment_method)):
    if pm == "master":
        break
    print(payment_method[pm])


# ridhwa