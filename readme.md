# MACRO 사용법
본 코드는 Python은 설치되어 있다고 가정한다.

만약 Conda 환경을 사용한다면, 적당한 이름의 Conda 환경을 만들고 activate 한다. 그 후, 
`pip install -r requirements.txt`를 shell에 입력하여 필요 라이브러리를 설치하여 준비한다.

1. 본 repository를 다운로드한다. (오른쪽 상단 code 버튼 클릭, download zip 또는 git clone하기)
2. config.ini를 에디터 (마땅한 게 떠오르지 않는다면 메모장을 쓸 것)로 연다.
3. config.ini의 로그인 정보를 입력하고, reservation information을 수정한다. 
4. python이 설치되어 있다고 가정한다. `pip install SRTrain`을 통하여 필요 라이브러리를 설치한다.
5. `python macro_SRTrain.py`를 shell에 입력하여 파이썬 파일을 실행한다.
6. 예매에 성공하면 성공했다고 뜨니깐, 예매에 성공했다는 알림이 터미널에 뜨면 SRT 사이트 가서 결제하면 된다.
