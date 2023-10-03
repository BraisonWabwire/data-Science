from matplotlib import pyplot as plt
movies=["Annie Hall","Ben-Hur","Casablanca","Gandi","West Side Story"]
num_oscars=[5,11,3,8,10]
plt.bar(range(len(movies)),num_oscars)
plt.title("My Favorite Movies")
plt.ylabel("# of Academic Awards")
plt.xticks(range(len(movies)),movies)
plt.show()