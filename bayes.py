#!/usr/bin/env python3

import sys
import math

if __name__ == '__main__':
    var, prob = sys.argv[1:3], sys.argv[3:]

    for index, cond in enumerate(zip(['+', '-'], [var[0], var[0]])):
        print(f'P{cond} = {prob[index]}')
    print('\n')

    temp = [f'{sign}{v}' for v in var for sign in '+ -'.split()]
    cond = [f'P({a} | {b}) = ' for b in temp[:2] for a in temp[2:]]

    for i in range(len(cond)):
        print(cond[i] + prob[2+i])
    print('\n')

    add = [f'P({a}, {b}) = ' for b in temp[:2] for a in temp[2:]]

    for i in range(len(cond)):
        print(add[i] + str((float(prob[i+2]) * float(prob[0 if i < 2 else 1]))))
    print('\n')

    concat = [float(prob[2+i]) * float(prob[0 if i < 2 else 1]) for i in range(len(cond))]
    reverse = [f'P({b} | {a}) = ' for b in temp[:2] for a in temp[2:]]

    posterior = []
    normal = [
        concat[0] + concat[2],
        concat[0] + concat[2],
        concat[1] + concat[3],
        concat[1] + concat[3]
    ]

    for i, (a, b) in enumerate(zip(concat, normal)):
        posterior.append(str(a / b))

    for i in range(len(posterior)):
        print(reverse[i] + posterior[i])
