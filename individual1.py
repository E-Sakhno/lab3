#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 4. С клавиатуры вводится натуральное число n. В зависимости от значения остатка при
# делении числа на 7 вывести на экран число в виде n = 7*k + r . Если r=0, то  вывести на экран n = 7*k .
n = int(input("Введите натуральное число: "))
k = int(input("Введите k: "))
r = n % 7
if r == 0:
    n = 7*k
else:
    n = 7 * k + r
print(n)
