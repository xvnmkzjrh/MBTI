import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 & 포켓몬 추천",
    page_icon="🎮",
    layout="centered"
)

st.title("🎓 MBTI 진로 & 포켓몬 추천소")
st.markdown("### 😎 너의 MBTI와 닮은 포켓몬은 누구일까?!")
st.write("MBTI를 선택하면 추천 진로와 찰떡인 포켓몬까지 알려줄게 👀✨")

career_data = {

    "INTJ": {
        "pokemon": "🟣 뮤츠",
        "pokemon_trait": "🧠 엄청 똑똑하고 전략적인 성격! 혼자 깊게 생각하는 걸 좋아해 😎",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",

        "careers": [
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
        ]
    },

    "INTP": {
        "pokemon": "🔮 팬텀",
        "pokemon_trait": "👀 호기심 많고 독창적인 아이디어가 넘치는 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",

        "careers": [
            {
                "job": "👨‍💻 프로그래머",
                "major": "📚 컴퓨터공학과, 소프트웨어학과",
                "personality": "⚡ 새로운 기술에 관심 많고 탐구심 강한 사람!"
            },
            {
                "job": "🔬 연구원",
                "major": "📚 자연과학계열, 공학계열",
                "personality": "🧪 깊게 탐구하고 분석하는 걸 좋아하는 사람!"
            }
        ]
    },

    "ENTJ": {
        "pokemon": "🔥 리자몽",
        "pokemon_trait": "👑 리더십 강하고 자신감 넘치는 카리스마 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",

        "careers": [
            {
                "job": "👑 CEO",
                "major": "📚 경영학과",
                "personality": "🔥 목표를 향해 밀고 나가는 추진력 있는 사람!"
            },
            {
                "job": "⚖️ 변호사",
                "major": "📚 법학과",
                "personality": "🗣️ 논리적으로 말 잘하고 설득력 있는 사람!"
            }
        ]
    },

    "ENTP": {
        "pokemon": "⚡ 제라오라",
        "pokemon_trait": "🚀 도전 좋아하고 아이디어 넘치는 자유로운 영혼!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/807.png",

        "careers": [
            {
                "job": "🚀 창업가",
                "major": "📚 경영학과, 창업학과",
                "personality": "✨ 도전 정신 강하고 아이디어 많은 사람!"
            },
            {
                "job": "📢 마케팅 전문가",
                "major": "📚 광고홍보학과",
                "personality": "🎨 창의적이고 사람들과 소통 잘하는 사람!"
            }
        ]
    },

    "INFJ": {
        "pokemon": "🌌 루기아",
        "pokemon_trait": "💖 조용하지만 깊은 공감 능력을 가진 따뜻한 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",

        "careers": [
            {
                "job": "💖 상담사",
                "major": "📚 심리학과, 상담학과",
                "personality": "🤝 공감 능력이 뛰어나고 배려심 깊은 사람!"
            },
            {
                "job": "✍️ 작가",
                "major": "📚 문예창작과, 국어국문학과",
                "personality": "🌙 감수성이 풍부하고 상상력 좋은 사람!"
            }
        ]
    },

    "INFP": {
        "pokemon": "🌙 이브이",
        "pokemon_trait": "💖 감수성 풍부하고 따뜻한 감성러!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",

        "careers": [
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
        ]
    },

    "ENFP": {
        "pokemon": "⚡ 피카츄",
        "pokemon_trait": "✨ 밝고 에너지 넘치고 친구 많은 인기쟁이 스타일!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",

        "careers": [
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
        ]
    }
}

mbti = st.selectbox(
    "👇 너의 MBTI를 골라봐!",
    list(career_data.keys())
)

if st.button("✨ 결과 보기"):
    data = career_data[mbti]

    st.header(f"💖 {mbti} 유형 결과!")

    st.subheader(f"{data['pokemon']}")
    st.image(data["pokemon_image"], width=200)

    st.write(data["pokemon_trait"])

    st.markdown("---")

    st.header("🎓 추천 진로")

    for career in data["careers"]:
        st.subheader(career["job"])
        st.write(career["major"])
        st.write(career["personality"])
        st.markdown("---")

    st.success("🎉 너랑 잘 어울리는 포켓몬과 진로를 찾았어!")
    st.balloons()
