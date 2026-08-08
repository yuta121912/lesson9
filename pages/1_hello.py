import streamlit as st
if 'user_name' in st.session_state and st.sessionstate.user_name:
    st.success(f"こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")

    st.balloons ()

else:
    st.error("ユーザーネームが設定されていません")
    st.write("メインページで名前を入力してください")