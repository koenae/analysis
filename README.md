# Analysis
Analysis performed for my master thesis in software engineering at the Open University. The output from [our crawler based on OpenWPM](https://github.com/koenae/openwpm-crawler) serves as input for this project.

## Prerequisites
- Python
- NPM and node (to run Cookiepedia crawler)

## Usage
Uncomment/comment the appropriate lines in main.py to run the desired analysis. Plots are saved in the respective folder of the country in the folder "plots". 

To start the Cookiepedia crawler, e.g., for The Netherlands, run the following command from the scripts/RQ3 folder:
```
node cookiepedia_crawler.js the_netherlands
```