import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

hideri = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=513&obsCd=305&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
oirase = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=513&obsCd=306&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
hanawa = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=1281&obsCd=8&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
fujikoto = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=1281&obsCd=27&appTime=2021-03-25%2015%3A59&isCurrent=true&fld=0'
maze = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000269&isCurrent=true&fld=0'
sirakawa = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000112&isCurrent=true&fld=0'
tuketi = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=5377&obsCd=90&isCurrent=true&fld=0'
ado = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=6401&obsCd=94&isCurrent=true&fld=0'
nahari = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=9985&obsCd=6&isCurrent=true&fld=0'
kakopath = '#app > div > div > div > div > div.mt-2 > div > div > div > div.row.mx-0.flex-row > div.py-0.col.col-10 > div:nth-child(2) > div > div > div.row.com-pc-card-header > button:nth-child(6) > span > span'
copypath = '#app > div > div > div > div > div.mt-2 > div > div > div > div.row.mx-0.flex-row > div.py-0.col.col-10 > div:nth-child(2) > div > div > div.com-pc-card-contents.pl-0.pr-0 > div.com-modal.com-modal-overlay > div > div.row.com-pc-card-header > button.mb-5.v-btn.v-btn--depressed.v-btn--flat.v-btn--outlined.theme--light.v-size--x-small.white--text > span > span'

# driver_manager 使用
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(1)

def cpyfunc(adrs):
    driver.get(adrs)
    kakobtn = driver.find_element_by_css_selector(kakopath)
    kakobtn.click()
    driver.implicitly_wait(1)
    copybtn = driver.find_element_by_css_selector(copypath)
    copybtn.click()

def drwfunc():
    dfs = pd.read_clipboard()
    df = dfs.iloc[1:,1:].replace(['^(?![+-]?(?:\d+\.?\d*|\.\d+)).+$'],'NaN',regex=True)
    arr = np.array(df.T,dtype=float).ravel()
    grf = pd.Series(arr)
    smin = grf.min()
    smax = grf.max()
    last = grf.iloc[-1]

    st.write(f'　　週間水位　　　　最大={smax}m　　最小={smin}m　　本日０時={last}m')

    x = [*range(0,168)]
    fig = plt.figure(figsize=(12,4))
    plt.plot(grf)
    plt.fill_between(x,grf,smin-0.2,color='c',alpha=0.2)
    plt.ylabel('Water Level(m)',fontsize=16)
    plt.yticks(fontsize=14)
    plt.xlabel('Time Transition(H)',fontsize=16)
    plt.xticks([0,24,48,72,96,120,144,168],[-168,-144,-120,-96,-72,-48,-24,0],fontsize=14)
    plt.ylim(smin-0.2,smax+0.2)
    plt.grid()
    st.pyplot(fig)

st.subheader('週間水位推移グラフ')

# チェックボックスの設定
st.sidebar.write('川選択')
riv1 = st.sidebar.checkbox('赤石川')
if riv1 :
        cpyfunc(hideri)
        st.write('赤石川日照田')
        drwfunc()
riv2 = st.sidebar.checkbox('追良瀬川')
if riv2 :
        cpyfunc(oirase)
        st.write('追良瀬川')
        drwfunc()
riv3 = st.sidebar.checkbox('米代川花輪')
if riv3 :
        cpyfunc(hanawa)
        st.write('米代川花輪')
        drwfunc()
riv4 = st.sidebar.checkbox('藤琴川')
if riv4 :
        cpyfunc(fujikoto)
        st.write('藤琴川')
        drwfunc()
riv5 = st.sidebar.checkbox('付知川')
if riv5 :
        cpyfunc(tuketi)
        st.write('付知川')
        drwfunc()
riv6 = st.sidebar.checkbox('安曇川')
if riv6 :
        cpyfunc(ado)
        st.write('安曇川')
        drwfunc()
riv7 = st.sidebar.checkbox('奈半利川')
if riv7 :
        cpyfunc(nahari)
        st.write('奈半利川')
        drwfunc()

# ホームページへのリンク
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('サイト表示')
link_maze = '[馬瀬川の水位](https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000269&isCurrent=true&fld=0)'
st.sidebar.markdown(link_maze, unsafe_allow_html=True)
link_sirakawa = '[白川の水位](https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000112&isCurrent=true&fld=0)'
st.sidebar.markdown(link_sirakawa, unsafe_allow_html=True)

st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
link1 = '[AyuZyのホームページ](https://sites.google.com/view/ayuzy)'
st.sidebar.markdown(link1, unsafe_allow_html=True)
st.text('※国土交通省川の防災情報のデーターを利用して表示しています')
