# 100-men-100-women

Simon Boas
sboas@ucsc.edu
University of California, Santa Cruz
CMPS 263 Winter 2017

## Leading Question
How do views on sexual promiscuity vary by gender and sexual orientation?

## Data Source/Input
* [The OKCupid dataset: A very large public dataset of dating site users](https://openpsych.net/paper/46)
	* Authors: Emil O. W. Kirkegaard, Ulster Institute for Social Research. <emil@emilkirkegaard.dk> and Julius D. Bjerrekær, University of Aalborg. <juliusdb.science@gmail.com>. Published in Open Differential Psychology, 2016. Data collected November 2014 to March 2015.
	* Data Files: user_data_public.csv, question_data.csv https://mega.nz/#F!QIpXkL4Q!b3QXepE6tgyZ3zDhWbv1eg
	
## Files
### Github Repository
[GitHub - bearsoup/100-men-100-women](https://github.com/bearsoup/100-men-100-women)
### Input
* ` user_data_public.csv`   T
This file not included in my GitHub repo due to its size (~1GB)
### Intermediate
* `process_okc_data_genbin.py`  
Goes through `user_data_public.csv` to extract all data potentially relevant to this project and saves it to a new, significantly smaller CSV file. (“genbin" is short for “gender binary” to differentiate this CSV from pervious versions that included a group of non-gender-binary users too small to perform statistical analysis on.
### Output
* `okc_relevant_data_genbin.csv`
Output from  previous file.
### Data Exploration
* `explore_relevant_data.py`
Uses the agate library for python to generate various tables from the data in `okc_relevant_data_genbin.csv`.

## Visualization Inspiration
This visualization is the most conceptually similar in terms of content:
[Sexual attitudes and lifestyles in Britain: Highlights from Natsal-3 | Visual.ly](http://visual.ly/sexual-attitudes-and-lifestyles-britain-highlights-natsal-3)

The following provide visual and interactive research, despite being conceptually different from my project:
### Interactive
[Behind the Bloodshed: The Untold Story of America’s Mass Killings](http://www.gannett-cdn.com/GDContent/mass-killings/index.html)
[Official site of James Anderson](http://jamesanderson613.com/)
[Sporting in England](http://infographics.sportengland.org/)
[Who’s in the American Center](http://www.nbcnews.com/id/53277240#intro)
### Static
[Marco Spies – Branded Interactions](https://www.designmadeingermany.de/2013/1654/)
[Weather Portraits](https://www.c82.net/blog/?id=71)
[SongPost - BRB](http://cargocollective.com/barbararebolledo/SongPost)

## Limitations
The researchers who collected the OKCupid dataset discuss its various limitations in their paper. It is important to note that, in order to scrape OkCupid profiles, the scraper must log in through an individual profile. The scraper that collected this dataset ran through a heterosexual male profile, which limited the results as discussed in the question below.

### Why this investigation is limited to gender-binary users?
From Kirkegaard and Bjerrekær:
>  Note that users with non-binary genders or sexual orientations can choose to hide their profiles from regular users. Since the scraper user was a heterosexual male, these users would not be included in the dataset. It is unknown how many users hide their profiles, so the 99.7 % figure should be cautiously interpreted.  

### Why is the mean user age so young (30s)?
This dataset is limited to OKCupid dating site users, most of whom tend to be younger in comparison to other online dating services like Match.com.

In general this dataset is largely limited by the OKCupid audience—mostly young, mostly located in North America—and by the profile used to scrape the data—a heterosexual male profile.

### Why are there only two options for the answers to the questions about promiscuity?
OKCupid match questions are all multiple choice. The pair of questions on promiscuity only have ‘Yes’ and ‘No’ as answer options.
