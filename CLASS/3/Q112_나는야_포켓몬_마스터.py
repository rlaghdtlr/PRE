#https://www.acmicpc.net/problem/1620
#문제 112번 - 나는야 포켓몬 마스터

# ver_1.0
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemons = []
for _ in range(n):
    pokemons.append(input().rstrip())

for _ in range(m):
    who = input().rstrip()
    if who.isdigit():
        print(pokemons[int(who)-1])
    else:
        try:
            index = pokemons.index(who)
            print(index+1)
        except ValueError:
            pass


# ver_2.0
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemons = {}
for i in range(n):
    pokemon = input().rstrip()
    pokemons[pokemon] = i + 1

keys = list(pokemons.keys())
for _ in range(m):
    who = input().rstrip()
    if who.isdigit():
        print(keys[int(who)-1])
    else:
        print(pokemons.get(who))