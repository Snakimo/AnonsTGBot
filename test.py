import pickle
saved_pattern = {}
with open('saved_patern.pickle', 'wb') as file:
            pickle.dump(obj=saved_pattern, file=file)