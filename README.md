# cardiac-attack-prediction

Before starting to model the data, need to do 2 steps:
 
1. Store the file heart.png in a folder named static.
2. Store the files index.html and index2.txt in a folder named templates.
3. Now the code of whole project should be stored in a single folder named cardiac project.

The code for the process below is in model.ipynb and in app.py

Step-by-Step process

Step-1: First, all the packages are imported into jupyter notebook, where the actual model is going to be created, like pandas, numpy, seaborn, plotly.express, matplotlib.pyplot, pickle and from sklearn.model_selection import train_test_split.

Step-2: Now, read the data which is in the csv form from the device and check for false or null values in the data. The visualization of different combination of attributes, like chest pain with gender and bp with cholesterol, is done by using bar plot, scatter plot etc….

Step-3: After the visualization is done for a number of combination of attributes, the data is split randomly using train_test_split() method into train and test datasets which are 75% and 25% respectively.

Step-4: The training data is used for training different types of classifiers as mentioned above, Random Forest, KNN, Naive Bayes, Soft Voting, XGBoost. 

Step-5: Then, the test data is used to test classifiers for their performance of predicting unseen data with accuracy. The accuracy, classification_report, f1_score are all calculated and compared for the best fitting model.

Step-6: This model is then dumped using pickle which is again loaded when the patient’s attributes are entered for results by the doctor in the GUI.

Step-7: The GUI is created, name “app.py”, using python language when executed generates a link which is a link of GUI interface for entering the data by the doctor. When attributes are entered and requested to predict, the pickle loaded in “app.py” is executed and the results are finally displayed. 
