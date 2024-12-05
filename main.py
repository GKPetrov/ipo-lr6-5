import random
num_list = [random.randint(-50, 50) for i in range(1,26)]
print(num_list)
zero=0
positive=0
negative=0
for i in range(len(num_list)):
    if num_list[i]>0:
        positive+=1
    elif num_list[i]<0:
        negative+=1
    elif num_list[i]==0:
        zero+=1
print(f'Количество нулей ={zero}. Процент от общего количества {zero/len(a)*100}')
print(f'Количество положительных ={positive}. Процент от общего количества {positive/len(a)*100}')
print(f'Количество отрицательных ={negative}. Процент от общего количества {negative/len(a)*100}')
print(f'Максимальное значение={max(a)}')
print(f'Минимальное значение={min(a)}')
