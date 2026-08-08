import streamlit as st 
st.title("ユーザーネーム情報を入力")


if 'name' not in st.session_state:
    st.session_state.user_name = ""


name=st.text_input ("あなたの名前を入力してください")
if st.button("名前を保存"):
    st.sesstion_state.user_name = name

st.write(f"現在保存されてる名前: {st.sessionstate.user_name}")