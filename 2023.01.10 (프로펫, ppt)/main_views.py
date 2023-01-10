from flask import Blueprint, url_for, render_template, flash, request,redirect,escape,jsonify, json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from PIL import Image
from torchvision import datasets, models, transforms
import warnings
warnings.filterwarnings('ignore')

bp = Blueprint('main',__name__,url_prefix='/')

model = models.resnet34(pretrained=True)

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 2)
model.load_state_dict(torch.load("C:/pythonprj/covid/covid/models/38-model_dict3.pth"), strict=False)
model.eval()
print('모델 로드 완료')
transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

model = model.to('cpu')

# 지수로그 없애기 위해 소수점 6자리까지만
np.set_printoptions(precision=6, suppress=True)
# 한국어 모델 불러오기
model1 = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

# csv 불러오기
df = pd.read_csv('C:/pythonprj/covid/covid/data/서울_선별진료소_질문답변1.csv')
df1 = pd.read_csv('C:/pythonprj/covid/covid/data/embeding_SB.csv', header=None)

df2 = pd.read_csv('C:/pythonprj/covid/covid/data/호흡기환자진료센터_질문답변1.csv')
df3 = pd.read_csv('C:/pythonprj/covid/covid/data/embeding_호흡기.csv', header=None)

prophet_new = pd.read_csv('C:\\pythonprj\\covid\\covid\\data\\prophet_new.csv')
prophet_sum = pd.read_csv('C:\\pythonprj\\covid\\covid\\data\\prophet_sum.csv')
new_ds_ls = list(prophet_new['ds'])
new_y_ls = list(prophet_new['y'])
sum_ds_ls = list(prophet_sum['ds'])
sum_y_ls = list(prophet_sum['y'])

@bp.route('/')
def index():
    return render_template('home.html', new_ds=new_ds_ls, new_y=new_y_ls, sum_ds=sum_ds_ls, sum_y=sum_y_ls)

@bp.route("/process_wav", methods=['GET', 'POST'])
def process_wav():
    print('Start')
    if request.method == "POST":
        print('POST')
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        return render_template("Recording.html", methods='post')
    else:
        print('GET')
        return render_template("Recording.html")

@bp.route('/result')
def result():
    input_audio_path = 'audio.wav'
    x, sr = librosa.load(input_audio_path)
    fig, ax = plt.subplots(figsize=(15, 5))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(x, hop_length=160)), ref=np.max)
    tmp = librosa.display.specshow(D, hop_length=160)
    plt.savefig('mel.jpg')
    if os.path.isfile('./file.wav'):
        print("./file.wav exists")

    image = Image.open('mel.jpg')
    image = transforms_test(image).unsqueeze(0).to('cpu')
    with torch.no_grad():
        outputs = model(image)

        _, preds = torch.max(outputs, 1)
        pred = preds[0].item()
        print(pred)
    return render_template('result.html', pred=pred)

@bp.route('/map')
def map():
    return render_template('map.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('coviddashboard.html')



# 챗봇 함수 입력받은 텍스트와 embeding 유사도 체크후 원본 챗봇에 cos컬럼 만든후 상위 정렬


def chatbot_text(text):
    em_result = model1.encode(text)
    co_result = []
    for temp in range(len(df1)):
        data = df1.iloc[temp]
        co_result.append(cosine_similarity([em_result], [data])[0][0])
    df['cos'] = co_result
    df_result = df.sort_values('cos', ascending=False)
    # r = random.randint(0,5)
    return df_result.iloc[0]['A']


def chatbot_text2(text):
    em_result2 = model1.encode(text)
    co_result2 = []
    for temp in range(len(df3)):
        data2 = df3.iloc[temp]
        co_result2.append(cosine_similarity([em_result2], [data2])[0][0])
    df2['cos'] = co_result2
    df2_result = df2.sort_values('cos', ascending=False)
    # r = random.randint(0,5)
    return df2_result.iloc[0]['A']


@bp.route('/movie1', methods=['POST'])
def movie1():
    result2 = request.get_json()
    result2 = pd.DataFrame(result2)
    print('입력 주소 : {}'.format(result2['queryResult']['queryText']))
    input_address = result2['queryResult']['queryText']

    re = jsonify(
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "list",
                                "title": "선별진료소",
                                "subtitle": chatbot_text(input_address),
                                "event": {
                                    "name": ""
                                }
                            },
                            {
                                "type": "divider"
                            },
                            {
                                "type": "list",
                                "title": "호흡기 진료센터",
                                "subtitle": chatbot_text2(input_address),
                                "event": {
                                    "name": ""
                                }
                            }
                        ]
                    ]
                }

            }
        ]
    )
    return re

