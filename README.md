### Analyzing Cricket Commentary Using NLP: Identifying Key Overs and Highlights

Cricket is a game of moments—those crucial overs that can turn the tide of the match. In this blog, I will walk you through an NLP project designed to analyze cricket commentary and extract key insights. By inputting the overs and runs of a match, the program identifies the top 10 overs with the highest wickets and highlights interesting events that occurred in those overs. This can be a powerful tool for cricket analysts, commentators, and fans who want to delve deeper into the game's intricacies.

#### Table of Contents
1. Demo
2. Requirements
3. Order of Execution
4. Problem Statement
5. Motivation
6. Approach
7. Results/Discussion
8. Conclusion

---

### 1. Demo

Check out the demo of our Cricket Commentary Analysis tool:
![Screenshot 2024-06-02 232104](https://github.com/Psychellic/Analysis-of-Cricket-Commentary/assets/127924785/65837cb5-193a-4c13-b558-c915f9f48246)

---

### 2. Requirements
```
python3.12
nltk
numpy
tensorflow
pytorch
sklearn
transformers
```

These python libraries are required.

### 3. Order of Execution
### List of Files

1. `Data_ext.py` 
2. `rnn.py` (Optional)
3. `input.py`
4. `final.py`

The first three files are present in the 'Code/' directory and the last file is present in the main file.

### 4. Problem Statement

Cricket matches are filled with critical moments that can drastically influence the outcome of the game. Identifying these moments from ball-by-ball commentary can provide valuable insights. The problem we aim to solve is to analyze cricket commentary to identify the top 10 overs with the highest number of wickets and highlight interesting points that occurred during these overs.

### 5. Motivation

Cricket analysts, commentators, and fans often miss out on the finer details of a match's turning points. By leveraging Natural Language Processing (NLP), we can extract these moments from the commentary, providing a deeper understanding of the game. This project aims to enhance the viewing experience and offer a tool for in-depth match analysis.

### 6. Approach

#### Data Collection and Preparation

We use the [Cricket Scorecard and Commentary Dataset](https://www.kaggle.com/datasets/raghuvansht/cricket-scorecard-and-commentary-dataset) from Kaggle, which includes detailed ball-by-ball commentary for various cricket matches.

#### NLP Techniques for Commentary Analysis

- **Word2Vec** - Using word2vec, we found the cricket vocabulary. It Uses a Pretrained Transformer Model BERT (bidirectional encoder representations from transformers) to Summarize the over. The interesting score is calculated by interesting score= 0.5* (normalized sentiment score) + 0.5* (normalized wordscore) and then Ranks the top 10 overs based on this score.


### RNN Code Snippet

![63b413dc18abfa2aa3cb8ab9_62ea833ddbd70fadffa8ac7f_HERO simple recurrent neural network](https://github.com/Psychellic/Analysis-of-Cricket-Commentary/assets/148717275/c976416c-bf60-41b5-a6c7-71302a271985)


```python

# Create the RNN model
model = Sequential(
    [
        Embedding(len(tokenizer.word_index) + 1, 128, input_length=max_length),
        LSTM(128, return_sequences=True),
        Dropout(0.2),
        LSTM(64),
        Dropout(0.2),
        Dense(64, activation="relu"),
        Dense(32, activation="relu"),
        Dense(2, activation="linear"),
    ]
)

```

---

### Explanation

In our cricket commentary RNN code, we utilize Recurrent Neural Networks (RNNs), which excel at understanding sequential data, akin to reading a story or watching a video. Applied to cricket commentary, the RNN analyzes each line, discerning patterns to predict outcomes which are runs and wickets. By training the model with organized data, we enable it to interpret and anticipate cricket events with an accuracy of 85%.
It sums up the Runs and the wickets over an entire over and ranks the top 10 overs with the highest runs and wickets.

#### Identifying Key Overs

1. Aggregate the number of wickets per over.
2. Sort the overs by the number of wickets in descending order.
3. Select the top 10 overs.

#### Highlighting Interesting Points

1. Summarize the over using BERT
2.  Filter the commentary data for the top 10 overs.
3. Apply sentiment analysis to identify lines with high excitement levels.

### 7. Results/Discussion

By analyzing the commentary data, we successfully identified the top 10 overs with the highest number of wickets. For each of these overs, we highlighted the most exciting moments, providing insights into how the match unfolded. This analysis not only helps in understanding past matches but also serves as a valuable resource for live commentary and strategic planning.

Example Output:

Sample Data:

| Over | Ball | Commentary                                       | Wickets | Runs |
|------|------|--------------------------------------------------|---------|------|
| 1    | 1.1  | "Bowler X to Batsman Y, no run, good length ball"| 0       | 0    |
| 1    | 1.2  | "Bowler X to Batsman Y, OUT! Caught by Z!"       | 1       | 0    |
| ...  | ...  | ...                                              | ...     | ...  |

### 8. Conclusion

This project demonstrates the power of NLP in sports analytics. By analyzing cricket commentary, we can identify key moments and gain deeper insights into the game. This tool is beneficial for analysts, commentators, and fans who wish to enhance their understanding and enjoyment of cricket. 

Feel free to implement and extend this project to suit your specific needs. Happy analyzing!

---

### Code and Data

You can find the complete code and dataset used in this project on [GitHub](https://github.com/Psychellic/Analysis-of-Cricket-Commentary).

---

### Future Enhancements

1. **Expand Dataset:** Including more matches and a diverse set of commentaries to improve model accuracy.
2. **Real-Time Analysis:** Developing a real-time analysis tool to assist commentators during live matches.
3. **Enhanced Sentiment Analysis:** Integrating more sophisticated sentiment analysis techniques to capture the excitement levels more accurately.
4. **Visualization Tools:** Creating visualization tools to graphically represent the key overs and highlights.
---

By following the steps outlined in this blog, you can create a powerful tool to analyze cricket commentary and gain deeper insights into the game. Whether you're a cricket analyst, commentator, or just a passionate fan, this project will enhance your understanding and enjoyment of the sport.

Feel free to implement and extend this project to suit your specific needs. Happy analyzing!

---

**Note:** This project was developed using the Cricket Scorecard and Commentary Dataset from Kaggle. Special thanks to the creators of the dataset for making this possible.
