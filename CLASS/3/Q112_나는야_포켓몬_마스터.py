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
# 1.0버전에서 구조를 딕셔너리형태로 만들어 실행시간 단축
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


# ver_3.0
# 2.0 버전에서 코드 정리
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
 
pokemons = {}
for i in range(1, n + 1):
    pokemon = input().rstrip()
    pokemons[i] = pokemon
    pokemons[pokemon] = i
 
for _ in range(m):
    who = input().rstrip()
    if who.isdigit():
        print(dict[int(who)])
    else:
        print(dict[who])