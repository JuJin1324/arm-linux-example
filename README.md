# arm-linux-compile-example
Docker를 이용한 OS 독립적인 arm-linux-compile 빌드(애플리케이션 실행은 지원 안함.)

## Requirement
* Docker desktop CE
* Docker compose
* Python 에 대한 약간의 지식

## Run
### CLI 방식
현재 디렉터리를 기준으로 함.
```shell script
cd docker

# Debug 빌드
docker-compose run arm-build-debug

# Release 빌드
docker-compose run arm-build-release
```

### CLion 방식
CLion 에서 터미널을 이용하여 CLI 방식을 그대로해도 상관없음.   
Alt + Shift + F10 을 통해서 ARM-BUILD-DEBUG 혹은 ARM-BUILD-RELEASE 선택

## Terminate
```shell script
docker-compose down
```
