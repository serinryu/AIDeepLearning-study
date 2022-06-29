# ⭐️ The Steps in Data Mining

![스크린샷 2022-06-09 오후 3 09 25](https://user-images.githubusercontent.com/74564995/172776681-c852fc05-3461-4c11-9bb8-73044ee6e780.png)

## [Preprocessing, Prelimiary process Step]

### 1. Develop an understanding of the purpose of the data mining project

- How will the stakeholder use the results? Who will be affected by the results? Will the analysis be a one-shot effort or an ongoing procedure?

### 2. Obtain the dataset to be used in the analysis: Sampling

- Sampling technique(ex. simple random sampling, stratified sampling, cluster sampling, multistage sampling...)
- If the event we are interested in classifying is rare, sampling may yield too few interesting cases to effectively train a model. So, we need appropriate number  of respondents or success cases to train a model. → solution : Oversample the rare events to obtain a balanced training set and adjust results to equal the number of each case. 

### 3. Explore, clean, and preprocess the data

- This step involves verifying that the data are in reasonable condition. How should missing data be handled? Are the values in a reasonable range, given what you would expect for each variable? Are there obvious outliers? 
- Outlier : 
  - Values that lie far away from the bulk of the data are called outliers.
- Missing Values(NaN) : 
  - An alternative to omitting records with missing values is to replace the missing value with an imputed value, based on the other values for that variable across all records.

### 4. Reduce the data dimension, if necessary

- Dimension reduction can involve operations such as eliminating unneeded variables, transforming variables and creating new variables. Make sure that you know what each variable means and whether it is sensible to include it in the model.
- Dimension reduction approaches: 
  - (1) incorporating domain knowledge to remove or combine categories, 
  - (2) using data summaries to detect information overlap between variables (and remove or combine redundant variables or categories), 
  - (3) using data conversion techniques such as converting categorical variables into numerical variables, 
  - (4) employing automated reduction techniques, such as principal components analysis (PCA), where a new set of variables (which are weighted averages of the original variables) is created.

### 5. Determine the data mining task (classification, prediction, clustering, etc.)

- This involves translating the general question or problem of Step 1 into a more specific data mining question.


## [Modeling Step]

### 6. Partition the data (for supervised tasks)

> 📌 Training data → Validation data → Test data → NEW DATA

- Training 데이터(훈련데이터)와 Input 데이터가 '달라져도' 똑같은 성능으로 출력되어야 한다(일반화). 즉, Training 데이터가 중요한 것이 아니라 그 데이터를 가지고 Test 데이터에 적용해봤을 때 비슷한 성과가 나오는 것이 중요함!! → 일반화가 제대로 되지 않을 때는 두 가지 문제가 발생한다. 과대적합overfitting(너무 복잡해서 문제 발생) 혹은 과소적합underfitting(너무 단순해 데이터에 내재된 구조를 학습하지 못할때 발생). 따라서 일반화를 위해서는 데이터 간의 퍼포먼스를 주의깊게 잘 봐야하고, 이를 위해 training data, validation data, test data 3개로 데이터셋을 분리한다.
- If the task is supervised (classification or prediction), randomly partition the dataset into three parts: training, validation, and test datasets.

### 7. Choose the data mining techniques to be used (regression, neural nets, hierarchical clustering, and so on).

### 8. Use algorithms to perform the task:

- This is typically an iterative process—trying multiple variants, and often using multiple variants of the same algorithm (choosing different variables or settings within the algorithm). Where appropriate, feedback from the algorithm’s performance on validation data is used to refine the settings.

### 9. Interpret the results of the algorithms: Evaluate results and compare models, best model 결정

- This involves making a choice as to the best algorithm to deploy, and where possible, testing the final choice on the test data to get an idea as to how well it will perform. (Recall that each algorithm may also be tested on the validation data for tuning purposes; in this way, the validation data become a part of the fitting process and are likely to underestimate the error in the deployment of the model that is finally chosen.)

### 10. Deploy the model

- This step involves integrating the model into operational systems and running it on real records to produce decisions or actions. For example, the model might be applied to a purchased list of possible customers, and the action might be “include in the mailing if the predicted amount of purchase is > $10.” A key step here is “scoring” the new records, or using the chosen model to predict the outcome value (“score”) for each new record.
