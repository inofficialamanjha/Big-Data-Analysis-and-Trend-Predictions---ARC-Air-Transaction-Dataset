# WHY - Hackathon & Dataset Details

## Airline Reporting Corporation (ARC)

Airline Reporting Corporation (ARC) [1] is an organization that provides ticket transaction settlement services between
airlines and travel agencies and the travel management companies that sell their products in the United States. In 2019,
ARC processed more than $97.4 billion worth of transactions for its customer.

ARC provides platforms, tools and insights that help the global travel community connect, grow and thrive. ARC enables the
diverse retailing strategies of its customers by providing innovative technology, flexible settlement solutions and access
to the world's most comprehensive air transaction dataset.

The data acquired from these transactions, representing more than 302Million passenger trips, can provide a unique perspective
on where travelers are going, when they travel and how much they are paying to get there.

## Hackathon Theme

The hackathons [5] goal is to identify a trend that leads to a new prediction using ARC's data to incorporate it into a marketable data
product withing the B2B or B2B2C space, i.e the task is to find creative ways to apply the vast data store from historical
trends mapped into predictive analysis to specific recommendations for consumers and suppliers of air travel.

## Dataset Details

![Dataset Image](Dataset/Original/Dataset Detail.png)

Datasets [2],[4] of two sample sizes are provided:
- Large Dataset: *Dataset*
- Small Sampled Dataset: *SampleDataset*

# HOW - Analysing data and figuring out innovating ideas

## DATA CLEANING

- Renaming data columns to appropriate Names
- Identifying data-types of all columns
- Finding out the occurrence of NaN / Invalid values in column entries
- Connecting *ORIGIN AIRPORT* to *ORIGIN* [3]
- Connecting *DESTINATION AIRPORT* to *DESTINATION* [3]
- Implementing an algorithm to merge appropriate segments of a Transaction to point out final *ORIGIN* and *DESTINATION*

# REFERENCES

[1]. [Airline Reporting Corporation (ARC)](https://www2.arccorp.com/)

[2]. [ARC Into the Travel Verse Dataset (ARC Airline Transaction Dataset)](https://drive.google.com/file/d/1McuYwEq-YPOEjMZat5qWrP1k5bQKDwMS/view?usp=sharing)

[3]. [Adrian Z., IATA Airport Codes - IATA Airport Codes and 3 letter code, Kaggle-Datasets](https://www.kaggle.com/zinovadr/iata-airport-code)

[4]. [J. Bhattacharyya, ARC-Enter the Travel-Verse - Hackerearth Competition, Kaggle-Datasets](https://www.kaggle.com/jayitabhattacharyya/hackerearth-arcenter-the-travelverse)

[5]. [Enter the Travel-Verse, HackerEarth-Hackathons](https://www.hackerearth.com/de/challenges/hackathon/enter-the-travel-verse/)


