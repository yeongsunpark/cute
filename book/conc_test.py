import concurrent.futures
import urllib.request
from datetime import datetime
tm = datetime.today().strftime("%Y-%m-%d-%H:%M:%S:%f")[:-4]
"""
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:  # executor 는 함수 호출을 비동기로 디스패치 해주는 역할을 담당하는 실행기의 베이스가 되는 추상 클래스.
    # Executor 객체는 컨텍스트 매니저 프로토콜을 지원하기 때문에 with 구문 내에서 사용.
    # max_workers 는 몇 개의 스레드를 관리하는 스레드풀을 생성할 것인지.
    future = executor.submit(pow, 2, 2)  # 함수의 리턴 값은 병렬로 실행되는 작업을 래핑한 Future 클래스 객체가 된다.
    print(future.result())
"""
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# ThreadPoolExecutor의 사용 예제
def load_url(url, timeout):  # url 의 리스트로부터 해당 페이지를 읽어서 바이트 수를 리턴하는 함수
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

print (datetime.today().strftime("%Y-%m-%d-%H:%M:%S:%f")[:-4])
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:  # 이를 여러 URL에 대해서 비동기로 호출하는 예
    future_to_url = {exe.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):  # as_completed() 모듈 함수를 이용해서 제출한 작업이 하나씩 완료될 때마다 결과를 출력
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exp:
            print("%r generated an exception: %s" % (url, exp))
        else:
            print("{} page is {} bytes".format(url, len(data)))
print (datetime.today().strftime("%Y-%m-%d-%H:%M:%S:%f")[:-4])
