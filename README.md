Step 1: Download the Dataset
1. Go to the URL: https://ai.stanford.edu/~amaas/data/sentiment/
2. Download and extract the dataset.
3. You will see two directories: `train/` and `test/`.

Step 2: Prepare the Data
1. Inside the `train/` and `test/` directories, you'll find `pos/` and `neg/` directories containing positive and negative reviews respectively.
2. You will use a script like `merge.py` to merge these reviews and create CSV files for training and testing.

Step 3: Run the Merge Script
1. Modify the `merge.py` script to create CSV files for both training and testing data. Run the script twice, once for training and once for testing.
2. The script should read reviews from `pos/` and `neg/` directories, extract text and label (positive/negative), and save them in CSV format.

Step 4: Build the Model
1. Open the `Movie_Sentiment_Analysis.ipynb` Jupyter Notebook.
2. Follow the steps in the notebook to build the sentiment analysis model.
