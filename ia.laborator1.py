y_pred = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
y_true = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]


def accuracy_score(list_1, list_2):
    n = len(list_1)
    suma = 0
    for i in range(n):
        if list_1[i] == list_2[i]:
            suma += 1
    accuracy = suma / n
    print('Accuracy: ', accuracy)
    return


def precision_recall_score(list_1, list_2):
    tp = 0
    fp = 0
    fn = 0  # incepem cu ele de la 0
    for i in range(len(list_1)):
        if list_2[i] == list_1[i] == 1:
            tp += 1
        if list_2[i] == 1 and list_1[i] == 0:
            fp += 1
        if list_2[i] == 0 and list_1[i] == 1:
            fn += 1
    precizie = tp / (tp + fp)
    recall = tp / (tp + fn)
    print('Precision and recall: ', precizie, recall)
    return


def mse(list_1, list_2):
    n = len(list_1)
    suma = 0
    for i in range(n):
        suma = suma + ((list_2[i] - list_1[i]) ** 2)
    print('Mean square error: ', suma/n)
    return


def mae(list_1, list_2):
    n = len(list_1)
    suma = 0
    for i in range(n):
        suma = suma + abs(list_2[i] - list_1[i])
    print('Mean absolute error: ', suma/n)
    return


accuracy_score(y_true, y_pred)
precision_recall_score(y_true, y_pred)
mse(y_true, y_pred)
mae(y_true, y_pred)

