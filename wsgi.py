'''
아파치 서버가 이 파일을 구동하여 flask를 가동시킴
여기서는 flask 객체를 가져와서 참조
'''

import sys
import os

#경로설정
CUR_DIR=os.getcwd()
#에러의 출력 방향을 일반 출력과 동일하게 설정
sys.stdout = sys.stderr
#PATH 추가
sys.path.insert(0,CUR_DIR)
#서버 가져오기
from run import app as application