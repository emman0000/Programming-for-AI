import matplotlib.pyplot as plt

cities = [
    "Karachi", "Vancouver", "Abu Dhabi", "Paris", "Mexico City",
    "Cairo", "Kabul", "Berlin", "Beijing", "Osaka",
    "New York", "Paris", "Istanbul", "Chengdu", "London",
    "Bangkok", "Kolkata", "Rio de Janeiro", "Los Angeles", "Tianjin"
   ]

populations = [
37_400_000, 30_290_000, 26_320_000, 21_650_000, 21_580_000,
    20_500_000, 20_290_000, 20_000_000, 19_500_000, 19_300_000,
    18_800_000, 16_800_000, 15_700_000, 14_500_000, 9_000_000,
    10_500_000, 14_200_000, 13_400_000, 12_500_000, 13_000_000
]

plt.figure(figsize = (12,8))
plt.barh(cities, populations, color='skyblue')

plt.title("Population of Cities that are Major ", fontsize=16)
plt.xlabel("Population", fontsize=14)
plt.ylabel("Cities", fontsize=14)
plt.show()
