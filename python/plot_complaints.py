
with open('filename.pickle', 'rb') as handle:
    complaints = pickle.load(handle)
print(complaints)
