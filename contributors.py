import html5lib
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Install chromedriver: https://chromedriver.chromium.org/getting-started

num_top=15 #top 15 contributors
days_range=1*365 #look back 1 year

# Choosing timeframe on Github's contributons tab
range_end=date.today()
range_start=range_end-timedelta(days=days_range)
url=f"https://github.com/openstack/nova/graphs/contributors?from={range_start}&to={range_end}&type=c"
print("Link being scrapped to view contributions: ", url)

# Setting up headless webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Wait till contributions are loaded and save to html file
try:
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "contrib-person")))
    soup = BeautifulSoup(driver.page_source, 'html5lib')

    with open("openstack_nova_contributions.html", "wb") as file:
        file.write(soup.prettify("utf-8"))
    print("Successfully scrapped page")
    
finally:
    driver.quit()

names=[] #list of contributors
commits=[] #list of number of commits
for i in range (1, num_top):
    all_contrib=soup.find_all("li",class_="contrib-person") #find all contributors
    name=all_contrib[i].find("a",class_="text-normal").getText() #get contributor names
    commit=int(all_contrib[i].find("a",class_="link-gray text-normal").getText().strip(" commits")) #get number of commits
    print(name, ": ", commit)
    names.append(name)
    commits.append(commit)

fig = plt.figure()
x_ax = [i for i, _ in enumerate(names)]
plt.barh(x_ax, commits) #using horizontal barchart to display complete usernames
plt.ylabel("Contributors")
plt.xlabel("Commits")
plt.title("Top 15 contributors to openstack/nova in the last 12 months")
plt.yticks(x_ax, names)
plt.savefig('top_contributors.jpg', dpi=300,bbox_inches='tight') #save plot to file
plt.show()