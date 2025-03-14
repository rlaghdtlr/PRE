def solution(answers):
    # 각 수포자의 찍는 패턴 정의
    pattern1 = [1, 2, 3, 4, 5]  # 1번 수포자
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번 수포자
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자

    # 각 수포자가 맞힌 문제 수를 저장할 변수
    scores = {1: 0, 2: 0, 3: 0}

    # 각 문제에 대해 수포자들의 답과 비교
    for i, answer in enumerate(answers):
        if pattern1[i % len(pattern1)] == answer:
            scores[1] += 1
        if pattern2[i % len(pattern2)] == answer:
            scores[2] += 1
        if pattern3[i % len(pattern3)] == answer:
            scores[3] += 1

    # 가장 높은 점수 찾기
    max_score = max(scores.values())

    # 가장 높은 점수를 받은 수포자 찾기 (동점자 포함)
    result = [person for person, score in scores.items() if score == max_score]

    # 결과를 오름차순으로 정렬
    result.sort()

    return result


print(solution([1, 2, 3, 4, 5]))
# 테스트 코드 제거
