import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
programmers = [3000, 4500, 15000, 75000, 300000, 500000, 1500000, 3000000, 27000000]

plt.figure(figsize=(10, 6))
plt.plot(years, programmers, marker='o', linestyle='-', color='b')
plt.title("Matt Kotzbauer Estimate for Global Programmer Count")
plt.xlabel("Year")
plt.ylabel("Number of Programmers")
plt.grid(True)
plt.yscale('log')
plt.xticks(years, rotation=45)

plt.show()
