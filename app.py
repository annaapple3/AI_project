# coding=utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

app = ['어저귀', '꿀풀' ,'메밀' ,'능소화' ,'용담', '세뿔석위', '접시꽃' ,'큰꿩의비름' ,'벌등골나물', '가지', '미국담쟁이덩굴'
 ,'억새' ,'오이풀', '장구채' ,'넉줄고사리' ,'물봉선' ,'산국', '담쟁이덩굴' ,'원추천인국', '난쟁이아욱' ,'봉선화', '하늘타리'
 ,'여우오줌' ,'시호', '담배풀', '뚝깔' ,'완두콩' ,'선괭이밥' ,'참죽나무' ,'가시오갈피' ,'당아욱' ,'석위', '무화과나무'
 ,'깨꽃(살비아)', '돼지감자' ,'한련초' ,'밤나무' ,'대청부채' ,'가죽나무' ,'감국' ,'석잠풀', '괭이밥' '오갈피나무' ,'여주'
 ,'회화나무', '쉽싸리', '범부채' ,'자귀나무', '개오동' ,'도깨비가지', '짚신나물' ,'제비쑥', '왕자귀나무', '매듭풀' ,'연꽃'
 ,'여뀌', '미국능소화' ,'둥근잎꿩의비름' ,'곰취', '해바라기', '진득찰', '독미나리', '과남풀(큰용담)', '황고사리' ,'부처손'
 ,'개옻나무' ,'아까시나무', '쪽' ,'개부처손' ,'미나리' ,'피마자' ,'술패랭이꽃' ,'마타리', '마디풀' ,'수세미오이', '아욱'
 ,'달뿌리풀' ,'닥풀', '동부', '오이' ,'가는장구채', '미국수련', '띠', '가시박' ,'미국까마중', '등골나물', '까마중'
 ,'묏대추나무' ,'맑은대쑥' ,'대추나무', '물억새' ,'갈대' ,'벽오동' ,'수박풀' ,'묏미나리' ,'개여뀌', '순비기나무', '꽃개오동'
 ,'털별꽃아재비', '참취', '감절대' ,'천선과나무' ,'개시호' ,'큰뱀무', '서양등골나물', '수박', '골등골나물', '단삼'
 ,'분홍장구채' ,'산오이풀', '수크령', '호장근' ,'붉나무', '털진득찰' ,'오동나무' ,'잇꽃' ,'패랭이꽃' ,'쥐방울덩굴', '좀담배풀']

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/image", methods=['POST'])
def ai():
    image = request.files['data']
    image.save('static/upload/'+image.filename)
    # 인공지능으로 이미지 처리
    img = Image.open('static/upload/'+image.filename)
    img_resize = img.resize((299,299))
    imgArray = np.array(img_resize)

    result = np.argmax(model.predict(imgArray.reshape(1,299,299,3)))
    # 처리한 이미지를 저장

    message = message + " I get it."
    return render_template("result.html", data=app[result-1])


if __name__ == "__main__":
    # 모델을 불러오는 부분
    model = tf.keras.models.load_model('C:\\Users\\annaa\\OneDrive\\바탕 화면\\임시저장소\\임시저장소\\AI project\\동의보감모델\\원본_잎-predict-model.h5')
    app.run(host='0.0.0.0', port=5000)
