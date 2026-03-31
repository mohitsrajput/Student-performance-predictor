import pickle

def predict(data):
    model = pickle.load(open('outputs/model.pkl','rb'))
    return model.predict([data])
