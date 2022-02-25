import streamlit as st
import numpy as np
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt

hideri = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=513&obsCd=305&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
oirase = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=513&obsCd=306&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
hanawa = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=1281&obsCd=8&appTime=2021-03-25%2015%3A45&isCurrent=true&fld=0'
fujikoto = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=1281&obsCd=27&appTime=2021-03-25%2015%3A59&isCurrent=true&fld=0'
maze = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000269&isCurrent=true&fld=0'
sirakawa = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=300&ofcCd=21000&obsCd=2100000112&isCurrent=true&fld=0'
tuketi = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=5377&obsCd=90&isCurrent=true&fld=0'
ado = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=6401&obsCd=94&isCurrent=true&fld=0'
nahari = 'https://www.river.go.jp/kawabou/pcfull/tm?itmkndCd=4&ofcCd=9985&obsCd=6&isCurrent=true&fld=0'


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

selriv = st.sidebar.radio(' ',('日照田','追良瀬','花輪','藤琴','馬瀬川','白川','付知川','安曇川','奈半利川'))

def showsite():
    if selriv == '日照田':
        webbrowser.open(hideri)
    elif selriv == '追良瀬':
        webbrowser.open(oirase)
    elif selriv == '花輪':
        webbrowser.open(hanawa)
    elif selriv == '藤琴':
        webbrowser.open(fujikoto)
    elif selriv == '馬瀬川':
        webbrowser.open(maze)
    elif selriv == '白川':
        webbrowser.open(sirakawa)
    elif selriv == '付知川':
        webbrowser.open(tuketi)
    elif selriv == '安曇川':
        webbrowser.open(ado)
    elif selriv == '奈半利川':
        webbrowser.open(nahari)
    else:
        st.title('さあ始めよう！')
        
st.title('週間水位アプリ')

if st.sidebar.button('サイト表示'):
    showsite()

st.sidebar.write('.　　　♡')
st.sidebar.write('----　　使い方　　----')
st.sidebar.write('アプリで場所を選択')
st.sidebar.write('アプリの「サイト表示」をクリック！')
st.sidebar.write('サイトの「過去一週間」をクリック！')
st.sidebar.write('過去一週間の「コピー」をクリック！')
st.sidebar.write('アプリの「グラフ表示」をクリック！')
st.sidebar.write('.　　　♡')

if st.sidebar.button('グラフ表示'):
    drwfunc()

