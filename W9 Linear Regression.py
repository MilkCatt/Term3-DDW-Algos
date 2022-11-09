'''Importing necessary functions'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

'''Function for matrix multiplication'''
def calc_linear(X, beta):
    return np.matmul(X, beta)

'''Getting the target (y-axis) and feature (x-axis) DataFrames from a DataFrame'''
def get_features_targets(df, feature_names, target_names):
    df_feature = df.loc[:,feature_names]
    df_target = pd.DataFrame(df.loc[:,target_names])
    return df_feature, df_target

'''Z-Normalizing data in a DataFrame'''
def normalize_z(dfin):
    dfout = (dfin-dfin.mean(axis=0))/dfin.std(axis=0)
    return dfout

'''Splitting the DataFrames into a test and train DataFrame'''
def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    indexes = df_feature.index 
    if random_state != None:
        np.random.seed(random_state)
    k = int(test_size * len(indexes))
    test_index = np.random.choice(indexes, k, replace = False)
    indexes = set(indexes)
    test_index = set(test_index)
    train_index = indexes - test_index
    df_feature_train = df_feature.loc[train_index, :]
    df_feature_test = df_feature.loc[test_index, :]
    df_target_train = df_target.loc[train_index, :]
    df_target_test = df_target.loc[test_index, :]
    return df_feature_train, df_feature_test, df_target_train, df_target_test

'''Changing the feature DataFrame into a numpy array for matrix operations'''
def prepare_feature(df_feature):
    cols = df_feature.shape[1]
    rows = df_feature.shape[0]
    row_of_ones = np.ones((rows,1))
    feature = df_feature.to_numpy().reshape(-1,cols)
    result = np.concatenate((row_of_ones,feature), axis=1)
    return result

'''Changing the target DataFrame into a numpy array for matrix operations'''
def prepare_target(df_target):
    cols = len(df_target.columns)
    target = df_target.to_numpy().reshape(-1,cols) # The -1 tells np to infer the no. of rows from the data
    return target

'''Computing the cost function with a given beta matrix'''
def compute_cost(X, y, beta):
    J = 0
    m = X.shape[0] # Number of data elements
    yhat = calc_linear(X, beta) # Calculating y hat (X x b)
    error = yhat - y # Calculating y hat minus y (difference)
    error_sq = np.matmul(error.T, error) # Calculating squared error
    J = (1/(2*m))*error_sq # Cost function as a single item in a numpy array -> [[J]]
    J = J[0][0] # Retrieving the integer value from the numpy array
    return J

'''Minimizing the cost function via gradient descent'''
def gradient_descent(X, y, beta, alpha, num_iters):
    m = X.shape[0]
    J_storage = np.zeros([num_iters,1])
    for i in range(num_iters):
        yhat = calc_linear(X, beta)
        derivative = np.matmul(X.T,(yhat - y))
        beta = beta - alpha * (1/m) * derivative
        J_storage[i] = compute_cost(X, y, beta)
    return beta, J_storage

'''Obtaining the predicted y variable'''
def predict(df_feature, beta):
    df_feature = normalize_z(df_feature)
    feature = prepare_feature(df_feature)
    return np.matmul(feature, beta)

'''Obtains the R^2 score'''
def r2_score(y, ypred):
    SSres = 0
    SSres_arr = (y - ypred)**2
    for val in SSres_arr:
        SSres += val
    print(SSres)
    SStot = 0
    n = y.shape[0]
    y_mean = (1/n)*y.sum(axis=0)
    SStot_arr = (y - y_mean)**2
    for val in SStot_arr:
        SStot += val
    return (1-(SSres/SStot))
    
'''Obtains the MSE score'''
def mean_squared_error(target, pred):
    MSE = 0
    n = target.shape[0]
    MSE_arr = (1/n)*(target - pred)**2
    for val in MSE_arr:
        MSE += val
    return MSE