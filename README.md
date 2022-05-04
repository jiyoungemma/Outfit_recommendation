# 날씨 예측 및 옷차림 추천서비스

### 프로젝트 기획 배경
날씨를 확인하는 행위는 결국 하루의 옷차림을 결정하기 위한 행위이다. 하지만 매우 덥거나 추운 날씨가 아니라면 어떤 옷차림이 적절한지 결정하는데 어려움이 있다. 이런 어려움과 매번 기온에 맞는 옷차림을 검색하는 불편함을 해소하기 위해 날씨를 예측함과 동시에 옷차림을 추천하는 서비스를 구현하였다.

### 내부 디렉토리 구조
```python
section3_project
┖ __pycache__
┖ flask_app
  ┖ templates
    ┖ index.html      # 홈페이지 첫 화면, 날씨를 예측할 지역 선택
    ┖ recommend.html  # 옷차림 추천 화면, 추천 옷차림을 선택하면 네이버 쇼핑으로 이동
    ┖ weather.html    # 예측된 날씨 화면
┖ __init__.py         # flask 연동
┖ db.py               # postgresql 연동
┖ openapi.py          # openapi key 저장
┖ past_weather.py     # 머신러닝 모델 pickle
Procfile	      # heroku ps 할당
requirements.txt      # 필요한 라이브러리
```

### 사용 기술
- HTML : 홈페이지 제작(메인 페이지, 날씨예측 페이지, 옷차림 추천 페이지)
- Python(Flask) : 서버 연결
- PostgreSQL : DB에 데이터 저장
- Goolge data studio : 시각화
- heroku : 배포
- colab : 머신러닝을 활용해 날씨예측 모델 개발
- 날씨예측 : open whether API 사용

### 시각화
https://datastudio.google.com/s/swYDUxctTzM
