import streamlit as st
import pandas as pd

st.title("ストリームリット入門")

st.markdown('<h5 class="red-h5">サイドバーの入力をお願いします</h5>', unsafe_allow_html=True)

name = st. sidebar.text_input('名前を入力して下さい')
if name:
    name,'さん、こんにちは！'

number = st.sidebar.selectbox('誕生月を教えて下さい', list(range(1, 13)))
'あなたの誕生日は',number,'月です。'
if number==4:    
    '誕生石はダイアモンドです'
    st.image('diamond.png', width=100, caption="diamond")
if number==5:   
    '誕生石はエメラルドです'
    st.image('emerald.png', width=100, caption="emerald")
if number==7:    
    '誕生石はルビーです'
    st.image('ruby.png', width=100, caption="ruby")
    
bestLike = st.sidebar.selectbox('大好きなことを一つ選んでください', ['食事', '料理', 'スポーツ', '読書', 'パソコン', '旅行', 'ガーデニング'])
bestLike, 'は素晴らしいですね❤️'


st.markdown('<h3>welcome to my page!</h3>', unsafe_allow_html=True)
st.image('myphoto.png', width=150 )


st.markdown('<h3>マークダウンの練習です</h3>', unsafe_allow_html=True)
st.markdown("*ここはイタリック Italic Font-Style:Italic* ")
st.markdown("[私のホームページへの案内です](http://www.pc2627.sumomo.ne.jp/)")
st.markdown('<span style="color:red">これは赤色のテキストです</span>', unsafe_allow_html=True)
st.markdown('<h5 class="red-h4">これは見出し５で、緑色を使いたいのですが、教えて下さい。</h5>', unsafe_allow_html=True)

# CSSを使用
st.markdown("""
<style>
h3 {
    color: blue;
    }
.red-h4 {
    color: green;
}
.red-h5 {    
    color: #800000; /* Dark Brown */
}
</style>
""", unsafe_allow_html=True)


st.markdown('<h3>私のフィジカル＆ダイエット</h3>', unsafe_allow_html=True)
df = pd.read_csv('physical.csv', index_col='年')
st.dataframe(df)

st.image('physical_chart.jpg')

# 行と列を入れ替える
# df_transposed = df.T
# st.dataframe(df_transposed)
# st.line_chart(df)
# st.line_chart(df_transposed)











