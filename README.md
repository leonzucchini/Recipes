# Introduction
This the code from a private research project. The project's aim is to gather and analyze data from the German-language website [Chefkoch][chefkoch].

## Data Source
Data is gathered from the German-language cooking website [Chefkoch][chefkoch]. Note: As of mid-October 2016 the chefkoch.de website's [terms of use][agb] made no provision restricting scraping the website for information, so this is all perfectly legal.

## Code

### Category pages
**Background**  
Recipe pages on [Chefkoch][chefkoch] are organized into seven overlapping [categories][categories]:
* Baking and sweets (Backen & Süßspeisen)
* Drinks (Getränke)
* Type of recipe (Menüart), e.g. starter or main course
* Regional cuisine (Regional)
* Seasonal recipes (Saisonal)
* Special recipes (Spezielles), e.g. baby food or camping
* Method of preparation (Zubereitungsarten), don't really understand this category

Categories comprise 12k-260k category-list-pages (like [this][cat-example]), each of which contains links to 30 recipes.

`crawl_category_subpages.py`  
This script uses a list of the category syntax and a list of *user-defined* path preferences in `config/`.
It downloads the HTML code of each category-list-page and and stores it to a local txt file.

**CAUTION**
* As of Nov 2016 there are ~27k category-list-pages (@30 recipes each), weighing in at 5GB
* Downloading took several hours (with a reasonably fast connection)


---
[chefkoch]: http://www.chefkoch.de
[agb]: http://www.chefkoch.de/terms-of-use.phps
[categories]: http://www.chefkoch.de/rezepte/kategorien/
[cat-example]: http://www.chefkoch.de/rs/s0g61/Zubereitungsarten.html
