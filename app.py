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
    },

    "ISTJ": {
        "pokemon": "🛡️ 거북왕",
        "pokemon_trait": "📋 책임감 강하고 믿음직한 든든한 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "careers": [
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
    }
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
    },

    "ISTJ": {
        "pokemon": "🛡️ 거북왕",
        "pokemon_trait": "📋 책임감 강하고 믿음직한 든든한 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "careers": [
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
    st.image(data["pokemon_image"], width=180)
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

mbti = st.selectbox(
    "👇 너의 MBTI를 골라봐!",
    list(career_data.keys())
)

if st.button("✨ 결과 보기"):
    data = career_data[mbti]

    st.header(f"💖 {mbti} 유형 결과!")

    st.subheader(f"{data['pokemon']}")
    st.image(data["pokemon_image"], width=180)
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
