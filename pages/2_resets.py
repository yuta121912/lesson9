import streamlit as st

st.title("リセット")

if ('user_name' in st.session_state and st.session_state.user_name):
   st.success(" 保存されている情報:")
   col1, col2 = st.columns(2)
   with col1:
     st.metric("名前", st.session_state.user_name)
     st.metric("学年", st.session_state.grade)
     with col2:
        if st.session_state.get('hobbies'):
           st.write("**趣味:**")
           for hobby in st.session_state.hobbies:
             st.write(f"• {hobby}")
        else:
           st.write("")


if st.button("リセット"):
    st.session_state.user_name= ""
    st.session_state.grade= ""
    st.session_state.hobbies= []
else:
    st.write("設定されていません")




















# st.title("計算")

# if "expression" not in st.session_state:
#     st.session_state.expression = ""

# st.text_input(
#     "",
#     value=st.session_state.expression,
#     disabled=True
# )

# if "expression" not in st.session_state:
#     st.session_state.expression = ""
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button("7"):
#         st.session_state.expression += "7"

# with col2:
#     if st.button("8"):
#         st.session_state.expression += "8"

# with col3:
#     if st.button("9"):
#         st.session_state.expression += "9"

# col4, col5, col6 = st.columns(3)

# with col4:
#     if st.button("6"):
#         st.session_state.expression += "6"

# with col5:
#     if st.button("5"):
#         st.session_state.expression += "5"

# with col6:
#     if st.button("4"):
#         st.session_state.expression += "4"
# col7, col8, col9 = st.columns(3)

# with col7:
#     if st.button("3"):
#         st.session_state.expression += "3"

# with col8:
#     if st.button("2"):
#         st.session_state.expression += "2"

# with col9:
#     if st.button("1"):
#         st.session_state.expression += "1"


# col10, col11, col12, col13 = st.columns(4)

# with col10:
#     if st.button("+"):
#         st.session_state.expression += "+"

# with col11:
#     if st.button("-"):
#         st.session_state.expression += "-"

# with col12:
#     if st.button("×"):
#         st.session_state.expression += "*"

# with col13:
#     if st.button("÷"):
#         st.session_state.expression += "/"

# if st.button("="):
#     try:
#         answer = eval(st.session_state.expression)
#         st.session_state.expression = str(answer)
#     except Exception:
#         st.error("計算できませんでした")
#         st.session_state.expression = ""

# if st.button("りせっと"):
#     st.session_state.expression = ""