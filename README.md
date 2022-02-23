# CraigList-Job-Scam-Detection
In this project, We have explored natural language processing and machine learning techniques to automate detection of fradulent jobs.

This is the process flow/architecture of the project:

![alt text](https://github.com/sgoyanka10/CraigList-Job-Scam-Detection/blob/main/Other/process_flow.png)

## Data Sources:

1. Scraped listings from the Craigslist jobs section, then manually labelled the data depending on whether the job listing is authentic or fake/scam.
2. Enriched the dataset using third-party data. Specifically, we use EMSCAD - Employment Scam Aegean Dataset (http://emscad.samos.aegean.gr/), which is a labeled data set for job scams.

## Data Modelling & Results

Fraudulent job classification is a binary class classification problem where we are trying to correctly classify if the job advertisement is a scam or not. The input/predictors we have used here are the job title and description. The output target variable is fraudulent with 0 and 1(fraud) classes.
We tried multiple models:
• Naive Bayes (Default parameters)
• Random Forest (n_estimators=500, max_depth=6, bootstrap=True, class_weight = 'balanced')
• Support Vector Machines (penalty = l1)
• Boosting (n_estimators=100, learning_rate=1.0, max_depth=1)
• LSTM – (Glove embedding, 100 layers, dropout=0.3, recurrent_dropout=0.3 with two dense layers of 1024, one dense layer of 1 neuron and sigmoid layer at the end, binary crossentropy loss with adam optimizer)

LSTM performed the best with an F1 score of 0.95 while the Naive Bayes performed the worst with an F1 score of 0.76.
