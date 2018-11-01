import logging

# DEBUG < INFO << WARNING < ERROR < CRITICAL

if __name__ == '__main__':
    mylogger = logging.getLogger("my")  # my 라는 특정 로거 생성. 루트 로거를 얻어서 사용.

    mylogger.setLevel(logging.INFO)  # 레벨 설정

    # 출력 포매팅 설정
    formatter = logging.Formatter('%(asctimee)s - %(name)s - %(levelname)s - %(messages)s')

    # 핸들러로 내가 로깅한 정보가 출력되는 위치 설정 가능. 콘솔, 파일, DB, 소켓, 큐 등
    stream_hander = logging.StreamHandler()  # logging.StreamHandler 클래스를 통해 stream_handler 객체를 만듦
    stream_hander.setFormatter(formatter)  # 출력 포매팅 생성
    mylogger.addHandler(stream_hander)

    # 파일로도 동시에 출력하게 해보기.
    file_handler = logging.FileHandler('ys.log')  # logging.FileHandler 클래스를 통해 객체를 만들어
    mylogger.addHandler(file_handler)  # 나의 로거에 추가.

    logging.error("something wrong!")  # 직접 호출