def heapify(arr, n, d, i): 
    largest = i 
    first_child = d * i + 1  # Вычисление индекса первого потомка в k-арном дереве
    for j in range(d): 
        child = first_child + j # Вычисление индекса j-го потомка
        if child < n and arr[largest].polar < arr[child].polar: # Проверка, является ли потомок наибольшим
            largest = child 
        elif child < n and arr[largest].polar == arr[child].polar and arr[largest].distance < arr[child].distance: # Дополнительная проверка для равных значений
            largest = child   
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, d, largest) 
 

def heap_sort(arr, d): 
    n = len(arr)  
    for i in range(n // d - 1, -1, -1): # Цикл для построения начальной кучи
        heapify(arr, n, d, i)  
    for i in range(n - 1, 0, -1): 
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, d, 0) 


def k_merge_sort(arr, k):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    size = (n + k - 1) // k  # Размер каждого подсписка
    sublists = [arr[i:i + size] for i in range(0, n, size)]  # Разделение на подсписки
    sorted_sublists = [k_merge_sort(sublist, k) for sublist in sublists]  # Рекурсивный вызов для каждого подсписка
    return k_merge(sorted_sublists) 
 

def k_merge(sublists):
    merged = []
    pointers = [0] * len(sublists)  # Указатели на текущие элементы каждого подсписка
    while True:
        min_value = float('inf')  # Начальное значение минимального элемента
        min_index = -1
        for i, sublist in enumerate(sublists):
            if pointers[i] < len(sublist) and sublist[pointers[i]].polar < min_value:
                min_value = sublist[pointers[i]].polar
                min_index = i
        if min_index == -1:  # Если все указатели дошли до конца подсписков, прервать цикл
            break
        merged.append(sublists[min_index][pointers[min_index]])  # Добавить минимальный элемент в merged
        pointers[min_index] += 1  # Увеличить указатель
    return merged