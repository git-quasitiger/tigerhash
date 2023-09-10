import argparse
import os

from hash_digest import md5_digest, sha1_digest, sha256_digest


# 입력받은 경로의 백슬래시 \ 를 슬래시 / 로 바꾼 후 출력하는 함수
def read_file(_file_path) -> bytes:

    # 파일의 절대경로 획득
    abs_path = os.path.abspath(_file_path)
    abs_path = abs_path.replace('\\','/')  

    # 올바른 파일인지 체크
    if os.path.isfile(abs_path):
        print(f'File : {abs_path}')
    elif os.path.isdir(abs_path):
        print(f'파일이 아닌 디렉토리 경로 입니다 : {abs_path}')
        return
    elif not os.path.exists(abs_path):
        print(f'파일이 존재하지 않습니다 : {abs_path}')
        return

    # 파일을 바이너리로 읽기
    with open(abs_path, 'rb') as f:
        data = f.read()
    
    # 파일의 바이너리 데이터를 리턴
    return data

# 파일 데이터와 옵션을 받아서 해시 계산 후 출력하는 함수
def calc_hash(_data, _option):

    if _option == 'all':
        print(f'MD5 : {md5_digest(_data)}')
        print(f'SHA1 : {sha1_digest(_data)}')
        print(f'SHA256 : {sha256_digest(_data)}')

    elif _option == 'md5':
        print(md5_digest(_data))

    elif _option == 'sha1':
        print(sha1_digest(_data))
        
    elif _option == 'sha256':
        print(sha256_digest(_data))

# 인자 파싱기능 함수
def argparse_config() -> argparse.ArgumentParser:
   
    parser = argparse.ArgumentParser(description='해시 계산 프로그램 입니다. 파일 경로와 해싱 옵션을 입력해주세요')
    parser.add_argument('-f', '--file', type=str, required=True, help='파일 경로를 입력하세요')
    parser.add_argument('-o', '--option', type=str, required=False, default='all', choices=['md5','sha1','sha256'], \
                        help='해싱 방법을 입력하세요 입력하지 않으면 md5, sha1, sha256 이 모두 출력됩니다.')
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    # 인자 파싱
    args = argparse_config()

    # 파일 바이너리로 읽기
    data = read_file(args.file)

    # 해시 계산
    if data:
        calc_hash(data, args.option)

