import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MBTI 진로 추천소")
st.markdown("### 😎 너의 MBTI에 딱 맞는 진로를 찾아보자!")
st.write("MBTI를 선택하면 어울리는 직업, 학과, 성격까지 알려줄게 👀✨")

career_data = {
    "INTJ": [
        {
            "job": "🧠 전략 기획가",
            "major": "📚 경영학과, 경제학과",
            "personality": "💡 계획 세우는 걸 좋아하고 분석 잘하는 사람!"
        },
        {
            "job": "💻 데이터 과학자",
            "major": "📚 컴퓨터공학과, 통계학과",
            "personality": "🔍 논리적으로 생각하고 문제 푸는 걸 좋아하는 사람!"
        }
    ],

    "INTP": [
        {
            "job": "👨‍💻 프로그래머",
            "major": "📚 컴퓨터공학과, 소프트웨어학과",
            "personality": "⚡ 새로운 기술에 관심 많고 호기심 많은 사람!"
        },
        {
            "job": "🔬 연구원",
            "major": "📚 자연과학계열, 공학계열",
            "personality": "🧪 깊게 탐구하고 생각하는 걸 좋아하는 사람!"
        }
    ],

    "ENTJ": [
        {
            "job": "👑 CEO",
            "major": "📚 경영학과",
            "personality": "🔥 리더십 있고 목표를 향해 달려가는 사람!"
        },
        {
            "job": "⚖️ 변호사",
            "major": "📚 법학과",
            "personality": "🗣️ 말 잘하고 논리적으로 설득하는 사람!"
        }
    ],

    "ENTP": [
        {
            "job": "🚀 창업가",
            "major": "📚 경영학과, 창업학과",
            "personality": "✨ 아이디어 많고 도전 좋아하는 사람!"
        },
        {
            "job": "📢 마케팅 전문가",
            "major": "📚 광고홍보학과, 경영학과",
            "personality": "🎨 창의적이고 사람들과 소통 잘하는 사람!"
        }
    ],

    "INFJ": [
        {
            "job": "💖 상담사",
            "major": "📚 심리학과, 상담학과",
            "personality": "🤝 공감 능력이 뛰어나고 따뜻한 사람!"
        },
        {
            "job": "✍️ 작가",
            "major": "📚 문예창작과, 국어국문학과",
            "personality": "🌙 감수성 풍부하고 상상력 좋은 사람!"
        }
    ],

    "INFP": [
        {
            "job": "🎨 디자이너",
            "major": "📚 시각디자인과, 산업디자인과",
            "personality": "🌈 감각적이고 창의력 넘치는 사람!"
        },
        {
            "job": "🧠 심리학자",
            "major": "📚 심리학과",
            "personality": "💬 다른 사람 마음을 잘 이해하는 사람!"
        }
    ],

    "ENFJ": [
        {
            "job": "🏫 교사",
            "major": "📚 교육학과",
            "personality": "🌟 사람들을 이끄는 걸 좋아하는 사람!"
        },
        {
            "job": "👥 인사 담당자",
            "major": "📚 경영학과, 심리학과",
            "personality": "😊 대인관계 능력이 뛰어난 사람!"
        }
    ],

    "ENFP": [
        {
            "job": "🎥 크리에이터",
            "major": "📚 미디어학과, 방송영상학과",
            "personality": "🔥 에너지 넘치고 표현력 좋은 사람!"
        },
        {
            "job": "📺 광고 기획자",
            "major": "📚 광고홍보학과",
            "personality": "💡 아이디어가 넘치고 창의적인 사람!"
        }
    ],

    "ISTJ": [
        {
            "job": "📊 회계사",
            "major": "📚 회계학과, 경영학과",
            "personality": "✅ 꼼꼼하고 책임감 강한 사람!"
        },
        {
            "job": "🏛️ 공무원",
            "major": "📚 행정학과",
            "personality": "📋 성실하고 체계적인 사람!"
        }
    ],

    "ISFJ": [
        {
            "job": "🩺 간호사",
            "major": "📚 간호학과",
            "personality": "💖 배려심 많고 책임감 있는 사람!"
        },
        {
            "job": "🤲 사회복지사",
            "major": "📚 사회복지학과",
            "personality": "🌼 다른 사람 돕는 걸 좋아하는 사람!"
        }
    ],

    "ESTJ": [
        {
            "job": "📈 경영 관리자",
            "major": "📚 경영학과",
            "personality": "🧩 조직 관리 능력이 뛰어난 사람!"
        },
        {
            "job": "🚔 경찰관",
            "major": "📚 경찰행정학과",
            "personality": "⚡ 원칙을 중요하게 생각하는 사람!"
        }
    ],

    "ESFJ": [
        {
            "job": "✈️ 승무원",
            "major": "📚 항공서비스학과",
            "personality": "😊 친절하고 서비스 정신이 강한 사람!"
        },
        {
            "job": "🎉 이벤트 플래너",
            "major": "📚 관광경영학과",
            "personality": "🤝 사교적이고 협업 잘하는 사람!"
        }
    ],

    "ISTP": [
        {
            "job": "⚙️ 엔지니어",
            "major": "📚 기계공학과, 전자공학과",
            "personality": "🔧 실용적이고 문제 해결 잘하는 사람!"
        },
        {
            "job": "🛫 파일럿",
            "major": "📚 항공운항학과",
            "personality": "😎 침착하고 판단력 좋은 사람!"
        }
    ],

    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "📚 사진학과",
            "personality": "🌅 감각적이고 예술적인 사람!"
        },
        {
            "job": "👗 패션 디자이너",
            "major": "📚 패션디자인학과",
            "personality": "✨ 개성 있고 창의적인 사람!"
        }
    ],

    "ESTP": [
        {
            "job": "💼 영업 전문가",
            "major": "📚 경영학과",
            "personality": "⚡ 활동적이고 적응력 좋은 사람!"
        },
        {
            "job": "🏀 스포츠 코치",
            "major": "📚 체육학과",
            "personality": "🔥 에너지 넘치고 리더십 있는 사람!"
        }
    ],

    "ESFP": [
        {
            "job": "🎭 배우",
            "major": "📚 연극영화과",
            "personality": "🌟 표현력 풍부하고 밝은 사람!"
        },
        {
            "job": "🎤 방송인",
            "major": "📚 방송연예과",
            "personality": "📸 사람들 앞에 나서는 걸 좋아하는 사람!"
        }
    ]
}

mbti = st.selectbox(
    "👇 너의 MBTI를 골라봐!",
    list(career_data.keys())
)

if st.button("✨ 진로 추천 보기"):
    st.header(f"💖 {mbti} 유형에게 추천하는 진로!")

    for career in career_data[mbti]:
        st.subheader(career["job"])
        st.write(career["major"])
        st.write(career["personality"])
        st.markdown("---")

    st.success("🎉 너에게 딱 맞는 진로를 찾았어!")
    st.balloons()
