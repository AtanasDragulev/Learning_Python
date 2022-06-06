import math

male = {"British Shorthair": 13, "Siamese": 15, "Persian": 14, "Ragdoll": 16, "American Shorthair": 12, "Siberian": 11}
female = {"British Shorthair": 14, "Siamese": 16, "Persian": 15, "Ragdoll": 17, "American Shorthair": 13, "Siberian": 12}
cat_type = input()
cat_gender = input()

if cat_gender == "m" and cat_type in male:
    print(f"{math.floor((male[cat_type]*12)/6)} cat months")
elif cat_gender == "f" and cat_type in female:
    print(f"{math.floor((female[cat_type]*12)/6)} cat months")
else:
    print(f"{cat_type} is invalid cat!")
