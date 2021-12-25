from pyeasyga.pyeasyga import GeneticAlgorithm
import random
import numpy as np

# Формат задания значений (y(x), [x])
data = (4.0, [-2.0])

# Параметры работы генетического алгоритма :
ga = GeneticAlgorithm(data,                             # начальные данные
                      population_size = 20,             # кол-во особей в популяции
                      generations = 30,                 # кол-во генераций
                      crossover_probability = 0.7,      # вероятность применения оператора скрещивания
                      mutation_probability = 0.01,      # вероятность применения мутации к гену
                      elitism = True,                   # вкл. выбор лучшей особи
                      maximise_fitness = False)         # максимизация целевой функции


# Функция создания начальной популяции
def create_individual(data):
    # Вещественное кодирование
    ind = [random.uniform(-4.0, 4.0)]

    return ind
ga.create_individual = create_individual


# Функция кроссинговера ГА (арифметический кроссинговер, lambda = 0.2)
def crossover(parent_1, parent_2):
    child_1 = [parent_1[0] * 0.2 + parent_2[0] * 0.8]
    child_2 = [parent_2[0] * 0.2 + parent_1[0] * 0.8]
    return child_1, child_2


ga.crossover_function = crossover


# Функция мутации для вещественного кодирования
def mutate(individual):
    rnd = np.random.normal(0, 0.5)
    if rnd < -0.5:
        rnd = -0.5
    elif rnd > 0.5:
        rnd = 0.5
    individual[0] = individual[0] + rnd


ga.mutate_function = mutate


# Функция селекции / турнирный отбор
def selection(population):
    ind1 = random.choice(population)
    ind2 = random.choice(population)
    if ind1.fitness < ind2.fitness:
        return ind1
    else:
        return ind2


ga.selection_function = selection


def fitness(individual, data):  # Целевая функция
    return individual[0] * individual[0] + 4  # Значение целевой функции


ga.fitness_function = fitness
ga.run()
# Вывод лучшей особи популяции (Наше решение)
print("\nЛучшая особь: ", ga.best_individual(), "\n")
