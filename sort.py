import random as rd

list = rd.sample(range(0, 1_000), 10) #Список из рандомных чисел диапазона
list1 = list                          #Точно такой же список для selection_sort

#////////Bubble_sort////////

#Задаём переменные:
n = len(list)                         #Длина списка
count = 0                             #Счётчик сравнений

#Выводим сгенерированный рандомом список
print(list)

#Задаём цикл для каждого элемента списка
for i in range(n - 1):                #диапазон задаём (n-1), чтобы сравнивать последующие эл-ты

    #Задаём ещё цикл для сравнения элементов и последующих замен
    for k in range(0, n - i - 1):

        #Сравниваем текущий и последующий эл-ты
        if list[k] < list[k+1]:

            
            count += 1
            # Swap if elements are in the wrong order
            new = list[k+1]
            list[k+1] = list[k]
            list[k] = new
            print(f'Шаг {count}: \n', list)

print("Отсортированный список:", list, 'Число сравнений: ', count)


n = len(list1)
count1 = 0
print(list1)
for f in range(n-1):
  min_position = f
  
  for j in range(f+1, n):
     if list1[j] > list1[min_position]:
       count1 += 1
       min_position = j
       min_value = list1.pop(min_position)
       list1.insert(f, min_value)
       print(f'Шаг {count1}: \n', list1)
  

print("Отсортированный список:", list1, 'Число сравнений: ', count1)