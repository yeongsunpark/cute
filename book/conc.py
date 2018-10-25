import concurrent.futures
from functools import partial


def is_prime(n):
    if n < 2:
        return False
    if n is 2 or n is 3:
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True


def process(n, r=10000):  # 특정한 하나의 구간에 대해 소수의 합을 구하는 함수
    print("processing: {} ..< {}".format(n, n+r), end="... ")  # 범위와 결과를 출력
    s = sum((x for x in range(n, n+r)
             if is_prime(x)
             if x <= 2000000))
    print(s)
    return s


def main():  # 작업을 쪼개어 전달하는 메인 함수
    r = 50000  # 업무를 나누는 단위
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as exe:  # 병렬처리를 위해 작업을 스케줄링 하는 부분 담당.
        """
        result = 0
        for i in exe.map(partial(process, r=r), range(0, 2000000, r)):
            # map() 메소드를 이용해 입력 데이터와 동적 함수를 짝지어서 바로 스케줄링 함 (cf. submit())
            # map() 메소드는 이터레이터를 리턴함(for 문에서 유용하게 쓰임).
            # 이는 각 개별 작업이 동시에 실행된 후 먼저 종료된 작업부터 내놓는 리턴 값 리턴
            result += i
            print(result)
        """
        # map() 안 쓰고 Futures 의 기능 이용
        fs = {exe.submit(process, n, r) for n in range(0, 2000000, r)}  # submit()을 이용해 Future 객체를 받고 큐에 넣음
        done, _ = concurrent.futures.wait(fs)  # wait()를 통해 완료, 미완료 작업을 받아, 완료된 것 내에서 결과값을 꺼내어 합산
        result = sum((f.result() for f in done))

        print(result)


if __name__ == "__main__":
    # 멀티프로세스를 이용하는 경우, 해당 스크립트 파일이 매번 하위 프로세스로 반입된다.
    # 따라서 이 경우에는 반드시 __main__ 모듈인지 체크하는 로직이 있어야 한다.
    main()