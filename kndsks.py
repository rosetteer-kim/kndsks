import pandas as pd
import streamlit as st


# CSV 파일에서 데이터 읽기
@st.cache_data
def load_data():
    data = pd.read_csv("data_all.csv")
    data['학번'] = data['학번'].astype(str)
    return data

# 메인 함수
def main():
    st.title("사랑으로")

    # 데이터 로드
    df = load_data()

    # 학번 입력 필드
    student_id = st.text_input("학번을 입력하세요:")

    # 버튼 생성
    if st.button("데이터 조회"):
        if student_id:
            # 입력된 학번으로 데이터 필터링
            student_data = df[df['학번'] == str(student_id)]

            if not student_data.empty:
                st.subheader(f"학번 {student_id}의 정보:")
                # 데이터를 세로로 표시
                # st.table(student_data.T)
                data_to_display = student_data.T
                data_to_display.columns = [''] * len(data_to_display.columns)  # 모든 열 이름을 빈 문자열로 설정
                st.table(data_to_display)

                # st.write(student_data)
            else:
                st.warning("해당 학번의 학생 정보를 찾을 수 없습니다.")
        else:
            st.warning("학번을 입력해주세요.")


if __name__ == "__main__":
    main()