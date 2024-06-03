import random
import math

def mae(y_pred, y_target):
    #sum_1^n |target - predict| / n
    sum = 0.0
    n = len(y_pred)

    for i in range(n):
        print(f'MAE, sample_{i}, pred = {y_pred[i]}, target = {y_target[i]}')
        loss_i = abs(y_target[i] - y_pred[i])
        print(f'\tloss_{i}={loss_i}')
        sum += loss_i

    final_MAE = sum / n
    print(f'final MAE={final_MAE}')

    return final_MAE


def mse(y_pred, y_target):
    #sum_1^n (target - predict)^2 / n
    sum = 0.0
    n = len(y_pred)

    for i in range(n):
        print(f'MSE, sample_{i}, pred = {y_pred[i]}, target={y_target[i]}')
        loss_i = math.pow(y_target[i] - y_pred[i], 2)
        print(f'\tloss_{i}={loss_i}')
        sum += loss_i

    final_MSE = sum / n
    print(f'final MSE={final_MSE}')

    return final_MSE


def rmse(y_pred, y_target):
    #sqrt(sum_1^n (target - predict)^2 / n)
    sum = 0.0
    n = len(y_pred)

    for i in range(n):
        print(f'RMSE, sample_{i}, pred = {y_pred[i]}, target = {y_target[i]}')
        loss_i = math.pow(y_target[i] - y_pred[i], 2)
        print(f'\tloss_{i}={loss_i}')
        sum += loss_i

    final_RMSE = math.sqrt(sum / n)
    print(f'final RMSE={final_RMSE}')

    return final_RMSE


def loss_cal():
    n = input('Input number of samples (n in N*) which are generated: ')
    if not n.isnumeric() or int(n) == 0:
        print('Number of samples must be a positive integer number')
        return

    loss_name = input('Input loss name: (MAE | MSE | RMSE): ')
    loss_function = {'mae': mae, 'mse': mse, 'rmse': rmse}
    loss_name_key = loss_name.lower()

    if loss_name_key not in loss_function.keys():
        print(f'{loss_name} is not supported')
        return

    n = int(n)
    y_pred = [random.uniform(0.0, 10.0) for i in range(n)]
    y_target = [random.uniform(0.0, 10.0) for i in range(n)]

    loss_function[loss_name_key](y_pred, y_target)


def exercise3():
    return loss_cal()
