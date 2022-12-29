# TrueFoundry coding assignment - https://sravanth-sentiment-analysis-api.hf.space 
## Deployment✅ 
## Did not use any pretrained models, completely developed from scracth. 
>1. Built ML models for the problem statement.✅
>2. Built Recurrent neural network for the same problem statement to prove that I have knowledge on Deep Learning too. (With fine tuning).✅
>3. Used OOPs Concepts.✅
>4. Developed API Server using FastAPI.✅
>5. Integrated Swagger Documentation.✅
>7. Containerized using Docker and deployed it on HuggingFace Spaces. (Bonus).✅
>8. Each and every point mentioned in assignment was completed.✅

## Tech Stack used
1. Tensorflow
2. Scikit-Learn
3. Fastapi
4. Docker & HuggingFace (Deployment)

Link for the deployed api - https://sravanth-sentiment-analysis-api.hf.space

### Screen Recordings
1. [Swagger UI](https://github.com/Sravanthgithub/assignment/blob/main/Truefoundry-submission-recording.mp4) 

### Steps to use this api
1. Click to get get the home page
![image](https://user-images.githubusercontent.com/77894804/209323381-1fd72192-0c6c-48db-a8f5-ce2b68346af6.png)

2. "/predict/{review}" to get the sentiment of the review entered.
Example review - "I love this airline"
![image](https://user-images.githubusercontent.com/77894804/209323485-99cc1603-7ff8-4135-b09b-ff4e423da198.png)

### Swagger UI (After cloning -> uvicorn app:app --reload -> http://127.0.0.1:8000/docs)
![image](https://user-images.githubusercontent.com/77894804/209323832-8944aa46-d216-4a47-b1a3-84c410491627.png)

## Best Models after tuning
1. Logistic Regression – {‘C’ : 1, ‘penalty’: : ‘l2”} Score – 91.85%
2. Support Vector Classifier – {‘C’ : 0.1, ‘Kernel’ : ‘Linear’} Score – 91.38%
3. Naïve Bayes – {‘alpha’ : 0.1} Score – 90.68%
4. Random Forest – {‘criterion’ : ‘gini’ , ‘n_estimators’ : 300} Score – 89.95%
5. Decision Tree – {‘criterion’ : ‘gini’,  ‘splitter’ :  ‘best’}  Score- 86.74%
6. KNN – {‘n_estimators’ : 5} Score – 71.71%
7. LSTM -  Score – 91%




