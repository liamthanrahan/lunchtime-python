def list_mean(a_list):
    answer = 0
    for value in a_list:
        answer += value

    answer = answer / len(a_list)
    return answer


print(list_mean([1, 2, 3]))
