import pandas as pd
import pickle
from model import train_model

df = pd.read_csv('data/student.csv')
X = df[['study_hours','attendance','previous_marks']]
y = df['final_score']
model = train_model(X, y)
with open('outputs/model.pkl','wb') as f:
    pickle.dump(model, f)
