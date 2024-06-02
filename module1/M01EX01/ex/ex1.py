def check_input(tp, fp, fn):
    flag = True
    var_name = {'tp': tp, 'fp': fp, 'fn': fn}

    for key, value in var_name.items():
        string_flag = True
        if not isinstance(value, int):
            print(f"{key} must be int", end='')
            string_flag = False
            flag = False
            
        if isinstance(value, (int, float)) and value <= 0:
            if not string_flag:
                print(' and greater than 0')
            else:
                print(f"{key} must be greater than 0")
            flag = False
        elif not string_flag:
            print('')   
        
    return flag


def f1_score(tp, fp, fn):
    if not check_input(tp, fp, fn):
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2.0 * precision * recall / (precision + recall)

    print(f"{'Precision':<{10}}: {precision}")
    print(f"{'Recall':<{10}}: {recall}")
    print(f"{'F1 Score':<{10}}: {f1_score}")
    
    
def exercise1(tp, fp, fn):
    f1_score(tp, fp, fn)