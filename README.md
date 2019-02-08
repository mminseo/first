# first
최초 flask app 소스 관리

배포관련 사항
deploy.json: 도메인, 아이피 등 정보
             형식이 JSON이라서 주석 작성 불가
             
fabfile.py: 페브릭 작업 내용 기술
fabfile_comment.py: 주석 버전
wsgi.py: entry파일, 서버 구동 시 시작점
requirements.txt: 서버 구동 시 필요한 모듈을 기술(사용한 모듈의 버전 등을 포함)

#서버 로그 확인
#접속로그
>tail -f /var/log/apache2/access.log
#나가기
>ctrl + c 
#에러로그
>tail -f /var/log/apache2/error.log