import streamlit as st 
st.title("ユーザーネーム情報を入力")


if 'name' not in st.session_state:
    st.session_state.user_name = ""


name=st.text_input ("あなたの名前を入力してください")

if 'name' not in st.session_state:
    st.session_state.grade = ""

grade=st.selectbox("あなたの年齢を選んでください" ,(["小学5年","小学6年","中学1年","中学2年","中学3年"]))

if 'name' not in st.session_state:
    st.session_state.hobby = ""

hobby=st.multiselect ("あなたの趣味を選んでください",(["読書","スポーツ","ゲーム","音楽","絵画","プログラム","その他"]))

if st.button(" 情報を保存"):
 st.session_state.user_name = name
st.session_state.grade = grade
st.session_state.hobbies = hobby
st.success(" 情報を保存しました!")