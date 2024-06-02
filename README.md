### Analyzing Cricket Commentary Using NLP: Identifying Key Overs and Highlights

Cricket is a game of moments—those crucial overs that can turn the tide of the match. In this blog, I will walk you through an NLP project designed to analyze cricket commentary and extract key insights. By inputting the overs and runs of a match, the program identifies the top 10 overs with the highest wickets and highlights interesting events that occurred in those overs. This can be a powerful tool for cricket analysts, commentators, and fans who want to delve deeper into the game's intricacies.

#### Table of Contents
1. Demo
2. Problem Statement
3. Motivation
4. Approach
5. Results/Discussion
6. Conclusion

---

### 1. Demo

Check out the live demo of our Cricket Commentary Analysis tool: [Cricket Commentary Analyzer Demo](https://example.com/demo)

---

### 2. Problem Statement

Cricket matches are filled with critical moments that can drastically influence the outcome of the game. Identifying these moments from ball-by-ball commentary can provide valuable insights. The problem we aim to solve is to analyze cricket commentary to identify the top 10 overs with the highest number of wickets and highlight interesting points that occurred during these overs.

### 3. Motivation

Cricket analysts, commentators, and fans often miss out on the finer details of a match's turning points. By leveraging Natural Language Processing (NLP), we can extract these moments from the commentary, providing a deeper understanding of the game. This project aims to enhance the viewing experience and offer a tool for in-depth match analysis.

### 4. Approach

#### Data Collection and Preparation

We use the [Cricket Scorecard and Commentary Dataset](https://www.kaggle.com/datasets/raghuvansht/cricket-scorecard-and-commentary-dataset) from Kaggle, which includes detailed ball-by-ball commentary for various cricket matches.

#### NLP Techniques for Commentary Analysis

- **Text Preprocessing:** Tokenization, stopword removal, and lemmatization to clean and prepare the commentary text.
- **Sentiment Analysis:** To gauge the excitement level of each commentary line.
- **Named Entity Recognition (NER):** To extract players' names, actions, and other important entities from the commentary.

#### Identifying Key Overs

1. Aggregate the number of wickets per over.
2. Sort the overs by the number of wickets in descending order.
3. Select the top 10 overs.

#### Highlighting Interesting Points

1. Filter the commentary data for the top 10 overs.
2. Apply sentiment analysis to identify lines with high excitement levels.
3. Use NER to extract and highlight key events.

### 5. Results/Discussion

By analyzing the commentary data, we successfully identified the top 10 overs with the highest number of wickets. For each of these overs, we highlighted the most exciting moments, providing insights into how the match unfolded. This analysis not only helps in understanding past matches but also serves as a valuable resource for live commentary and strategic planning.

Example Output:

Sample Data:

| Over | Ball | Commentary                                       | Wickets | Runs |
|------|------|--------------------------------------------------|---------|------|
| 1    | 1.1  | "Bowler X to Batsman Y, no run, good length ball"| 0       | 0    |
| 1    | 1.2  | "Bowler X to Batsman Y, OUT! Caught by Z!"       | 1       | 0    |
| ...  | ...  | ...                                              | ...     | ...  |

### 6. Conclusion

This project demonstrates the power of NLP in sports analytics. By analyzing cricket commentary, we can identify key moments and gain deeper insights into the game. This tool is beneficial for analysts, commentators, and fans who wish to enhance their understanding and enjoyment of cricket. 

Feel free to implement and extend this project to suit your specific needs. Happy analyzing!

---

### Code and Data

You can find the complete code and dataset used in this project on [GitHub](https://github.com/yourusername/cricket-commentary-analysis).

---

By following the steps outlined in this blog, you can create a powerful tool to analyze cricket commentary and gain deeper insights into the game. Whether you're a cricket analyst, commentator, or just a passionate fan, this project will enhance your understanding and enjoyment of the sport.

---

### RNN Code Explanation

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

### Explanation of the RNN Code

In the given RNN code, the primary goal is to predict the number of runs and wickets based on cricket commentary. Let's break down the code step-by-step:

1. **Import Libraries and Load Data:**

2. **Preprocess the Data:**

3. **Tokenize the Commentary:**
   ```python
   # Tokenize the commentary
   tokenizer = Tokenizer()
   tokenizer.fit_on_texts(commentary)
   sequences = tokenizer.texts_to_sequences(commentary)
   ```

   The `Tokenizer` is used to convert the text data into sequences of integers.

4. **Pad the Sequences:**

   The sequences are padded to ensure uniform input length for the RNN.

5. **Split the Data:**
   The data is split into training and testing sets.

6. **Create the RNN Model:**

   An RNN model is created with an Embedding layer, LSTM layers, Dropout layers to prevent overfitting, and Dense layers for output.

7. **Compile the Model:**
   The model is compiled using the Adam optimizer and mean squared error (MSE) loss function.

8. **Prepare the Target Variables:**
   The runs and wickets are combined into a single target variable.

9. **Train the Model:**
   The model is trained using the training data.

10. **Evaluate the Model:**
   The model is evaluated on the test data, and the accuracy and precision for runs and wickets predictions are calculated.

11. **Save the Trained Model:**
    The trained model is saved to disk using the pickle module.

12. **Make Predictions on Hard-Coded Inputs:**
    The model is used to make predictions on hard-coded commentary inputs to demonstrate its capability to predict runs and wickets based on the text commentary.

In the final section of the RNN code, we utilize the trained model to make predictions on new, hard-coded commentary inputs.

13. **Making Predictions on Hard-Coded Inputs:**
    # Hard-coded commentary input
    commentary_input = "taken! Yasir Shah strikes. Flatter trajectory outside off, gets it to turn a touch but more importantly, gets some extra bounce. Smith sees something short and goes back to cut. The extra bounce is responsible for a thick outside edge. Sarfraz hangs onto a quality reflex catch, had his gloves in the right spot."
    commentary_sequence = tokenizer.texts_to_sequences([commentary_input])
    commentary_padded = pad_sequences(commentary_sequence, maxlen=max_length)

    prediction = model.predict(commentary_padded)
    predicted_runs = np.round(prediction[:, 0]).astype(int)[0]
    predicted_wickets = np.round(prediction[:, 1]).astype(int)[0]

    print("Predicted Runs:", predicted_runs)
    print("Predicted Wickets:", predicted_wickets)
    ```

    - **Input Commentary:** This commentary text describes a ball that resulted in a wicket.
    - **Tokenization and Padding:** The text is tokenized and padded similarly.
    - **Prediction:** The model predicts the number of runs and wickets for this commentary line.
    - **Output:** The predicted runs and wickets are printed, demonstrating the model's ability to interpret and predict the outcome of the commentary.

### Conclusion

This project showcases how Natural Language Processing (NLP) can be effectively applied to sports commentary analysis. By leveraging an RNN model, we can predict significant events in cricket matches from textual commentary, providing valuable insights for analysts, commentators, and fans. This tool enhances the understanding and enjoyment of the game by highlighting key moments and identifying turning points in matches.

### Future Enhancements

1. **Expand Dataset:** Including more matches and a diverse set of commentaries to improve model accuracy.
2. **Real-Time Analysis:** Developing a real-time analysis tool to assist commentators during live matches.
3. **Enhanced Sentiment Analysis:** Integrating more sophisticated sentiment analysis techniques to capture the excitement levels more accurately.
4. **Visualization Tools:** Creating visualization tools to graphically represent the key overs and highlights.

### Code and Data

You can find the complete code and dataset used in this project on [GitHub](https://github.com/yourusername/cricket-commentary-analysis).

---

By following the steps outlined in this blog, you can create a powerful tool to analyze cricket commentary and gain deeper insights into the game. Whether you're a cricket analyst, commentator, or just a passionate fan, this project will enhance your understanding and enjoyment of the sport.

Feel free to implement and extend this project to suit your specific needs. Happy analyzing!

---

**Note:** This project was developed using the Cricket Scorecard and Commentary Dataset from Kaggle. Special thanks to the creators of the dataset for making this possible.
