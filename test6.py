def solution(bandage, health, attacks):
    # bandage: [시전 시간, 초당 회복량, 추가 회복량]
    cast_time, heal_per_sec, bonus_heal = bandage

    # 최대 체력 설정
    max_health = health
    current_health = health

    # 공격 시간을 키로 하는 딕셔너리 생성
    attack_dict = {attack[0]: attack[1] for attack in attacks}

    # 마지막 공격 시간
    last_attack_time = attacks[-1][0]

    # 연속 성공 시간
    consecutive_success = 0

    # 0초부터 마지막 공격 시간까지 시뮬레이션
    for time in range(1, last_attack_time + 1):
        # 공격 시간인 경우
        if time in attack_dict:
            # 체력 감소
            current_health -= attack_dict[time]
            # 연속 성공 초기화
            consecutive_success = 0

            # 체력이 0 이하면 사망
            if current_health <= 0:
                return -1
        # 공격 시간이 아닌 경우
        else:
            # 연속 성공 시간 증가
            consecutive_success += 1

            # 체력 회복
            current_health += heal_per_sec

            # 연속 성공 보너스 체력 회복
            if consecutive_success == cast_time:
                current_health += bonus_heal
                consecutive_success = 0

            # 최대 체력 초과 방지
            current_health = min(current_health, max_health)

    return current_health
