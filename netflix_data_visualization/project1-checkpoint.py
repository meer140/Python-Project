import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv("netflix.csv")
df = df.dropna()
print(df.head())

#pie chart for rating column
rating_col = df["rating"].value_counts()
plt.figure(figsize=(10,6))
plt.pie(rating_col.values, labels=rating_col.index, autopct ='%1.1f%%')
plt.title("RATING RATIO OF MOVIES")
plt.tight_layout()
plt.savefig("rating_ration.png")
plt.show()

#bar graph showing numbers of movies released in specific years
year_col = df['release_year'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(year_col.index, year_col.values, color = 'blue')
plt.xlabel('YEAR')
plt.ylabel('NO OF MOVIES')
plt.title("MOVIES RELEASED IN A YEAR", size = 15)
plt.tight_layout()
plt.savefig("Movies_released.png")

years = df['release_year'].values
scores = df['user_rating_score'].values
plt.figure(figsize = (8,6))
plt.scatter(years, scores, marker = 'o' , color = 'orange')
plt.title('RATING SCORES OF EACH YEAR MOVIES', size = 15)
plt.xlabel('MOVIE RELEASE YEAR')
plt.ylabel('RATING SCORE OF MOVIES')
plt.tight_layout()
plt.savefig('rating_score.png')
plt.show()