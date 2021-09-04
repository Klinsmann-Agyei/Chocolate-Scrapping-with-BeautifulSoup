import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, 'html.parser')
soup.prettify()
ratings = []
for rating in soup.find_all(attrs={"class": "Rating"}):
  ratings.append(rating.text)
ratings.pop(0)
ratings = [float(i) for i in ratings]
plt.hist(ratings)
plt.show()
company = soup.select(".Company")
company_names = []
for name in company:
  company_names.append(name.text)
company_names.pop(0)
dict = {"Rating": ratings, "Company": company_names}
df = pd.DataFrame(dict)
df.groupby("Company").mean()
#print(df.nlargest(10, "Ratings"))
cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  cocoa_percents.append(percent)

df["CocoaPercentage"] = cocoa_percents
plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
