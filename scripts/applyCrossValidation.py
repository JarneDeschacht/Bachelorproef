# code based on https://www.youtube.com/watch?v=gJo0uNL-5Qw
# this code will apply 5 fold cross validation (CV) for the dataset

# import the library to apply (CV)
from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True)

for train_index, test_index in kf.split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ]):
    print(train_index, test_index)
print('_______________________________________________________')
