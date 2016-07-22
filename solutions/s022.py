"""Healthy sleep

Ann watched a TV program about health and learned that it is recommended
to sleep at least AA hours per day, but oversleeping is also not healthy
and you should not sleep more than BB hours. Now Ann sleeps HH hours per day.
If Ann's sleep schedule complies with the requirements of that TV program –
print "Normal". If Ann sleeps less than AA hours, output “Deficiency”, if she
sleeps more than BB hours, output “Excess”.

Input to this program are the three strings with variables in the following
order: AA, BB, HH. AA is always less than or equal to BB.

Please note latters case: the output should exactly correspond to what required
in the problem, i.e. if the program has to output "Excess", such output as
"excess", "EXCESS", "ExCeSs" and others will not be graded as correct.

You should carefully think about all conditions, which you need to use.
A special attention should be paid to the strictness of the used conditional
operators: distinguish between << and ≤≤; >> and ≥≥. In order to understand
which ones to use, please carefully read the problem statement.

Sample Input 1:
    6
    10
    8
Sample Output 1:
    Normal

Sample Input 2:
    7
    9
    10
Sample Output 2:
    Excess

Sample Input 3:
    7
    9
    2
Sample Output 3:
    Deficiency
"""


def main():
    low_limit = int(input().rstrip())
    top_limit = int(input().rstrip())
    sleep_hours = int(input().rstrip())

    if sleep_hours < low_limit:
        print('Deficiency')
    elif sleep_hours > top_limit:
        print('Excess')
    else:
        print('Normal')

if __name__ == '__main__':
    main()
