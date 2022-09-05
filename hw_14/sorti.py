"""
    Sorti - модуль включающий в себя  функции сортировки:
    sorti_bubble - сортирует методом пузырька. Последовательно сравнивает
    значения соседних элементов и меняет числа местами если предыдущее
    оказывается больше последующего.

    sorti_insert - сегментирует список на две части: отсортированную и не
    отсортированную. Алгоритм перебирает второй сегмент и вставляет текущий
    элемент в правильную позицию первого сегмента.

    sorti_quick - разделяет список относительно одного из выбранных
    элементов (опорный) на два подсписка, берет из каждого подсписка
    два элемента и происходит распределение чтоб в одном из подсписков
    находились элементы меньше опорного элемента, а в другом списке больше.
    Далее делит каждый из подсписков на по новому опорному элементу и
    алгоритм повторяется
"""


def partition(nums, low, high):
    """
    :param nums: int
    :param low: int
    :param high: int
    :return: возвращает список в котором элементы слева от pivot меньше,
            а с права больше чем pivot.
    """
    """
    partition - функция  ищет средний элемент pivot, на который делит
    список и меняет местами значения элементов относительно pivot, 
    при условии что значение слева больше значения справа.
    Функция является внутренней и не вызывается модулем sorti.
    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def sorti_quick(nums):
    """
    :param nums: list
    :return: выводит отсортированный список от меньшего значения к большему

    _sorti_quick - рекурсивная функция, которая получает индекс
    опорного элемента (pivot)   и делит список относительного него.
    """
    def _sorti_quick(item, low, high):
        if low < high:
            split_index = partition(item, low, high)
            #print(nums)
            _sorti_quick(item, low, split_index)
            _sorti_quick(item, split_index + 1, high)

    _sorti_quick(nums, 0, len(nums) - 1)


def sorti_insert(nums):
    #print(nums)
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1

        nums[j + 1] = item_to_insert


def sorti_bubble(nums):

    n = len(nums)
    for i in range(n-1):
        for j in range(n-2, i - 1, -1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


__all__ = ['sorti_insert', 'sorti_bubble', 'sorti_quick']
if __name__ == "__main__":
    lst = [12, 15, 97, 64, 15, 97, 5496, 125, 84, 31, 17]
    sorti_bubble(lst)
    print(lst)


