# Analyzing Cricket Commentary Using NLP: Identifying Key Overs and Highlights

Cricket is a game of moments—those crucial overs that can turn the tide of the match. In this blog, I will walk you through an NLP project designed to analyze cricket commentary and extract key insights. By inputting the overs and runs of a match, the program identifies the top 10 overs with the highest wickets and highlights interesting events that occurred in those overs. This can be a powerful tool for cricket analysts, commentators, and fans who want to delve deeper into the game's intricacies.

# Table of Contents
1. Introduction
2. Project Overview
3. Data Collection and Preparation
4. NLP Techniques for Commentary Analysis
5. Identifying Key Overs
6. Highlighting Interesting Points
7. Conclusion

---

# 1. Introduction

Cricket commentary, whether text or audio, is rich in details that can provide deep insights into the flow of the game. By leveraging Natural Language Processing (NLP), we can analyze this commentary to extract meaningful patterns and highlight the most critical moments of a match.

# 2. Project Overview

The goal of this project is to analyze cricket commentary to:
- Identify the top 10 overs with the highest number of wickets.
- Highlight interesting points that occurred in those overs.

We will achieve this by:
- Collecting and preparing the commentary data.
- Applying NLP techniques to process the text.
- Extracting and analyzing the overs with the highest wickets.
- Highlighting key events in those overs.

# 3. Data Collection and Preparation

# Data Collection

For this project, we use a dataset from Kaggle, the Cricket Scorecard and Commentary Dataset(https://www.kaggle.com/datasets/raghuvansht/cricket-scorecard-and-commentary-dataset). This dataset includes detailed ball-by-ball commentary for various cricket matches, which is essential for our analysis.

#### Data Structure

The dataset includes:
- Over number
- Ball number
- Commentary text
- Wickets information
- Runs scored

Sample Data:

| Over | Ball | Commentary                                       | Wickets | Runs |
|------|------|--------------------------------------------------|---------|------|
| 1    | 1.1  | "Bowler X to Batsman Y, no run, good length ball"| 0       | 0    |
| 1    | 1.2  | "Bowler X to Batsman Y, OUT! Caught by Z!"       | 1       | 0    |
| ...  | ...  | ...                                              | ...     | ...  |

# 4. NLP Techniques for Commentary Analysis

We will use several NLP techniques to analyze the commentary text and extract key information.

# Text Preprocessing

1. Tokenization: Splitting the commentary text into individual words.
2. Stopword Removal: Removing common words that do not contribute to the analysis (e.g., "the", "is", "at").
3. Lemmatization: Reducing words to their base or root form.

# Sentiment Analysis

Applying sentiment analysis to determine the excitement level of each commentary line, helping to identify interesting points.

# Named Entity Recognition (NER)

Using NER to identify players' names, actions, and other important entities in the commentary.

# 5. Identifying Key Overs

To identify the top 10 overs with the highest wickets, we will:

1. Aggregate the number of wickets per over.
2. Sort the overs by the number of wickets in descending order.
3. Select the top 10 overs.

# 6. Highlighting Interesting Points

To highlight interesting points in the top 10 overs, we will:

1. Filter the commentary data for the top 10 overs.
2. Apply sentiment analysis to identify lines with high excitement levels.
3. Use NER to extract and highlight key events.

# 7. Conclusion

By using NLP techniques, we can effectively analyze cricket commentary to identify key moments in a match. This project demonstrates how data science can be applied to sports analytics, providing valuable insights and enhancing the viewing experience for fans.

Feel free to implement and extend this project to suit your specific needs. Happy analyzing!

----------

# Code and Data

You can find the complete code and dataset used in this project on GitHub(https://github.com/Psychellic/Analysis-of-Cricket-Commentary).

----------

By following the steps outlined in this blog, you can create a powerful tool to analyze cricket commentary and gain deeper insights into the game. Whether you're a cricket analyst, commentator, or just a passionate fan, this project will enhance your understanding and enjoyment of the sport.
