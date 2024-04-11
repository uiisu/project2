from fastapi import APIRouter


router = APIRouter(tags=["Стажировка"])


"""
Задание_1. Удаление дублей
    Реализуйте функцию соответствующую следующему описанию:
    На вход подаётся массив слов зависимых от регистра, для которых необходимо произвести
    фильтрацию на основании дублей слов, если в списке найден дубль по регистру, то все
    подобные слова вне зависимости от регистра исключаются.
    На выходе должны получить уникальный список слов в нижнем регистре.

    Список слов для примера: ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
    Ожидаемый результат: ['папа','брат']
"""


@router.post("/find_in_different_registers", description="Задание_1. Удаление дублей")
async def find_in_different_registers(words: list[str]) -> list[str]:
    """
    Производит фильтрацию на основании дублей слов.

    Args:
        words (list[str]): Список слов для фильтрации.

    Returns:
        result (list[str]): Отфильтрованный список слов.
    """

    words_unique = []
    words_repeat = []
    result = []
    for i in range(len(words)):
        if words[i] not in words_unique:
            words_unique.append(words[i])
        else:
            words_repeat.append(words[i].lower())
    for i in range(len(words_unique)):
        if (words_unique[i].lower() not in words_repeat) and (words_unique[i].lower() not in result):
            result.append(words_unique[i].lower())
    return result
