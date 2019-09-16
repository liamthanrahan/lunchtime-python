def list_min(a_list):
    answer = a_list[0]
    for value in a_list:
        if value < answer:
            answer = value
    return answer


print(list_min([1, 2, 3]))
