Було побудовано дві функції щодо мінімального підбору монет для визначеної суми
find_coins_greedy - функція що використовуює жадібний алгоритм
find_min_coins - функція, що використовує динамічне програмування

Для визначення того, як швидно працюють функції для їх порівняння, була задана сума 98878, з повтором в 100 разів.
В результаті дослідження було отримано наступні результати:

Жадібний алгоримт:
{50: 1977, 25: 1, 2: 1, 1: 1}
Время выполнения find_coins_greedy: 5.729999975301325e-05
 
Динамічне програмування:
{50: 1977, 25: 1, 2: 1, 1: 1}
Время выполнения find_min_coins: 7.71987369999988

Як бачимо Жадібний алгоритм набагато швидший ніж алгоритм Динаміного програмування, але Жадібний алгоритм незавжди видає оптимальні варіанти, а алгоритм Динаміного програмування завжди видає оптимальні варіанти.