# Lotte Project

8월부터 11월 말까지 롯데정보통신과 함께 진행된 프로젝트. 

**무인편의점 객체 인식과 얼굴인식 프로젝트.**


1. yolo-slim implementation[[yolo-slim]](https://www.youtube.com/watch?v=DQuO6h57ieo)

2. facenet implementation1[[facenet1]](https://www.youtube.com/watch?v=b7Es7vDKsRo)

3. fianl result[[result]](https://www.youtube.com/watch?v=_ZWP0opu5Wk)


## 1. 환경 셋팅

PyCharm IDE에서 실행할 것을 권장합니다.
아래 표은 개발 당시의 주요 파이썬 패키지의 버전 목록입니다.
표기된 버전의 상위 버전 패키지를 사용하시고 
에러가 발생한다면 아래의 버전으로 다운그레이드하세요.

tensorflow 2.x 버전대는 호환되지 않습니다.

| Package        | Version |
| -------------- | ------- |
| numpy          | 1.15.1  |
| pillow         | 5.3.0   |
| scipy          | 1.1.0   |
| tensorflow-gpu | 1.13.1  |
| wget           | 3.2     |
| seaborn        | 0.9.0   |
| pyqt           | 5.9.2   |
| easydict       | 1.9     |

## 2. 파일 복사

오른쪽 링크에서 압축파일을 다운로드합니다. [[Link]](https://drive.google.com/file/d/1cNmUbdONFoG3fmHxGyhcN5Fw7sR92c4g/view?usp=sharing)

`Facenet` 폴더, `checkpoint ` 폴더, `yolov3_coco.pb`를 `Unmanned counter` 폴더에 복사해주세요.

## 3. How to run this model

`Unmanned counter/obj/main_window.py` 파일을 실행하세요.

초기 설정으로 테스트 영상으로 모델이 작동합니다.
웹캠을 사용하시려면 `Unmanned counter/obj/showVideo.py`의 41번 라인을 참고하세요.
