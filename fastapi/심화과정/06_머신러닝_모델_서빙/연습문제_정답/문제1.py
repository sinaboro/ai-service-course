# 문제 1. model_core.PassModel을 직접 불러와(API 없이) 공부 3시간·수면 7시간·휴대폰 2시간인 학생의 합격 확률을 소수 3자리로 출력하세요.

# 정답 폴더에서 실행해도 되도록: 장 폴더(06_...)를 import 경로와 작업 폴더로 지정
import os
import sys
CHAPTER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CHAPTER)                      # model_core, ex01_serving_app 을 찾을 수 있게
os.chdir(CHAPTER)                                # "model/pass_model.npz" 같은 상대 경로가 맞도록

import numpy as np
from model_core import PassModel

model = PassModel.load("model/pass_model.npz")
p = model.predict_proba(np.array([[3, 7, 2]]))[0]
print(f"합격 확률: {p:.3f}  (모델 버전 {model.version})")
