# Openstack Nova's top contributors scraper

## Method 1: Local Jupyter notebook
1. ```git clone git@github.com:adbX/contributors_openstack.git```
1. ```pip3 install html5lib bs4 selenium matplotlib```
2. Install chromedriver: https://chromedriver.chromium.org/getting-started  (on mac: ```brew install chromedriver```)
3. Run with Jupyter ```jupyter-lab contributors.ipynb```

Note: ```contributors.py``` is also available to be run as a script (without Jupyter)

## Method 2: Docker
1. ```git clone git@github.com:adbX/contributors_openstack.git```
2. ```docker build -t openstack .```
3. ```docker run --name openstack-container -d -p 5000:5000 openstack```
4. ```docker cp openstack-container:/app/ .``` to copy generated docker files to current directory

## Outputs
- ```openstack_nova_contributions.html``` - The github webpage source code with the selected timeframe
- ```top_contributors.jpg``` - Barchart of the top 15 contributors
