import hashlib
# 바이너리 데이터를 입력받아 md5 해시값을 반환하는 함수
def md5_digest(_data) -> str:
    md5_checksum = hashlib.md5(_data).hexdigest()
    return md5_checksum

# 바이너리 데이터를 입력받아 sha1 해시값을 반환하는 함수
def sha1_digest(_data) -> str:
    sha1_checksum = hashlib.sha1(_data).hexdigest()
    return sha1_checksum

# 바이너리 데이터를 입력받아 sha256 해시값을 반환하는 함수
def sha256_digest(_data) -> str:
    sha256_checksum = hashlib.sha256(_data).hexdigest()
    return sha256_checksum
