import random
num_list = [random.randint(-50, 50) for i in range(1,26)]
print(num_list)
zero = 0
positive = 0
negative = 0
for num in num_list:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero+=1
print(f'Количество нулей ={zero}. Процент от общего количества {zero/len(num_list)*100}')
print(f'Количество положительных ={positive}. Процент от общего количества {positive/len(num_list)*100}')
print(f'Количество отрицательных ={negative}. Процент от общего количества {negative/len(num_list)*100}')
print(f'Максимальное значение={max(num_list)}')
print(f'Минимальное значение={min(num_list)}')
