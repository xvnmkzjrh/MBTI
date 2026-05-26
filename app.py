import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 & 포켓몬 추천",
    page_icon="🎮",
    layout="centered"
)

st.title("🎓 MBTI 진로 & 포켓몬 추천소")
st.markdown("## 😎 너의 MBTI와 닮은 포켓몬은 누구일까?!")
st.write("✨ MBTI를 선택하면 추천 진로와 포켓몬을 알려줄게!")

career_data = {

    "INTJ": {
        "pokemon": "🟣 뮤츠",
        "pokemon_trait": "🧠 전략적이고 똑똑한 완벽주의자 스타일!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "careers": [
            {
                "job": "🧠 전략 기획가",
                "major": "📚 경영학과, 경제학과",
                "personality": "분석적이고 계획 세우기를 좋아함!"
            },
            {
                "job": "💻 데이터 과학자",
                "major": "📚 컴퓨터공학과, 통계학과",
                "personality": "논리적이고 문제 해결을 좋아함!"
            }
        ]
    },

    "INTP": {
        "pokemon": "👻 팬텀",
        "pokemon_trait": "🔍 호기심 많고 아이디어 넘치는 천재 스타일!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "careers": [
            {
                "job": "👨‍💻 프로그래머",
                "major": "📚 컴퓨터공학과",
                "personality": "새로운 기술 배우는 걸 좋아함!"
            },
            {
                "job": "🔬 연구원",
                "major": "📚 자연과학계열",
                "personality": "탐구심이 강함!"
            }
        ]
    },

    "ENTJ": {
        "pokemon": "🔥 리자몽",
        "pokemon_trait": "👑 카리스마 넘치는 리더 스타일!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "careers": [
            {
                "job": "👑 CEO",
                "major": "📚 경영학과",
                "personality": "목표 지향적이고 리더십 강함!"
            },
            {
                "job": "⚖️ 변호사",
                "major": "📚 법학과",
                "personality": "논리적이고 설득력 있음!"
            }
        ]
    },

    "ENTP": {
        "pokemon": "⚡ 제라오라",
        "pokemon_trait": "🚀 자유롭고 도전 좋아하는 스타일!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/807.png",
        "careers": [
            {
                "job": "🚀 창업가",
                "major": "📚 창업학과",
                "personality": "아이디어가 많고 도전적!"
            },
            {
                "job": "📢 마케팅 전문가",
                "major": "📚 광고홍보학과",
                "personality": "창의적이고 소통 잘함!"
            }
        ]
    },

    "INFJ": {
        "pokemon": "🌌 루기아",
        "pokemon_trait": "💖 조용하지만 따뜻한 이상주의자!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "careers": [
            {
                "job": "💖 상담사",
                "major": "📚 심리학과",
                "personality": "공감 능력이 뛰어남!"
            },
            {
                "job": "✍️ 작가",
                "major": "📚 문예창작과",
                "personality": "감수성이 풍부함!"
            }
        ]
    },

    "INFP": {
        "pokemon": "🌙 이브이",
        "pokemon_trait": "🌈 감성 풍부한 몽글몽글 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "careers": [
            {
                "job": "🎨 디자이너",
                "major": "📚 디자인학과",
                "personality": "창의적이고 감각적!"
            },
            {
                "job": "🧠 심리학자",
                "major": "📚 심리학과",
                "personality": "타인의 감정을 잘 이해함!"
            }
        ]
    },

    "ENFJ": {
        "pokemon": "☀️ 윈디",
        "pokemon_trait": "🌟 사람 챙기기 좋아하는 따뜻한 리더!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png",
        "careers": [
            {
                "job": "🏫 교사",
                "major": "📚 교육학과",
                "personality": "사람들을 이끄는 걸 좋아함!"
            },
            {
                "job": "👥 인사 담당자",
                "major": "📚 경영학과",
                "personality": "대인관계 능력이 뛰어남!"
            }
        ]
    },

    "ENFP": {
        "pokemon": "⚡ 피카츄",
        "pokemon_trait": "🎉 밝고 활발한 분위기 메이커!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "careers": [
            {
                "job": "🎥 크리에이터",
                "major": "📚 미디어학과",
                "personality": "표현력이 좋고 에너지 넘침!"
            },
            {
                "job": "📺 광고 기획자",
                "major": "📚 광고홍보학과",
                "personality": "아이디어가 풍부함!"
            }
        ]
    },

    "ISTJ": {
        "pokemon": "🛡️ 거북왕",
        "pokemon_trait": "📋 책임감 강한 믿음직한 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "careers": [
            {
                "job": "📊 회계사",
                "major": "📚 회계학과",
                "personality": "꼼꼼하고 성실함!"
            },
            {
                "job": "🏛️ 공무원",
                "major": "📚 행정학과",
                "personality": "체계적이고 책임감 있음!"
            }
        ]
    },

    "ISFJ": {
        "pokemon": "💧 라프라스",
        "pokemon_trait": "🤍 다정하고 배려심 넘치는 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
        "careers": [
            {
                "job": "🩺 간호사",
                "major": "📚 간호학과",
                "personality": "배려심 많고 책임감 강함!"
            },
            {
                "job": "🤲 사회복지사",
                "major": "📚 사회복지학과",
                "personality": "남 돕는 걸 좋아함!"
            }
        ]
    },

    "ESTJ": {
        "pokemon": "⚔️ 한카리아스",
        "pokemon_trait": "🔥 추진력 강한 현실 리더!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png",
        "careers": [
            {
                "job": "📈 경영 관리자",
                "major": "📚 경영학과",
                "personality": "조직 관리 능력이 뛰어남!"
            },
            {
                "job": "🚔 경찰관",
                "major": "📚 경찰행정학과",
                "personality": "원칙을 중요하게 생각함!"
            }
        ]
    },

    "ESFJ": {
        "pokemon": "🎀 픽시",
        "pokemon_trait": "😊 친절하고 사교성 좋은 인기쟁이!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
        "careers": [
            {
                "job": "✈️ 승무원",
                "major": "📚 항공서비스학과",
                "personality": "친절하고 서비스 정신 강함!"
            },
            {
                "job": "🎉 이벤트 플래너",
                "major": "📚 관광경영학과",
                "personality": "사람들과 협업 잘함!"
            }
        ]
    },

    "ISTP": {
        "pokemon": "⚙️ 메타그로스",
        "pokemon_trait": "🛠️ 조용하지만 실력파인 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/376.png",
        "careers": [
            {
                "job": "⚙️ 엔지니어",
                "major": "📚 기계공학과",
                "personality": "문제 해결 능력이 뛰어남!"
            },
            {
                "job": "🛫 파일럿",
                "major": "📚 항공운항학과",
                "personality": "침착하고 판단력 좋음!"
            }
        ]
    },

    "ISFP": {
        "pokemon": "🌸 치코리타",
        "pokemon_trait": "🎨 조용하고 감성적인 예술가 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/152.png",
        "careers": [
            {
                "job": "📸 사진작가",
                "major": "📚 사진학과",
                "personality": "감각적이고 예술적!"
            },
            {
                "job": "👗 패션 디자이너",
                "major": "📚 패션디자인학과",
                "personality": "개성 있고 창의적!"
            }
        ]
    },

    "ESTP": {
        "pokemon": "⚡ 번치코",
        "pokemon_trait": "🔥 활동적이고 승부욕 강한 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png",
        "careers": [
            {
                "job": "💼 영업 전문가",
                "major": "📚 경영학과",
                "personality": "활동적이고 적응력 좋음!"
            },
            {
                "job": "🏀 스포츠 코치",
                "major": "📚 체육학과",
                "personality": "리더십 있고 에너지 넘침!"
            }
        ]
    },

    "ESFP": {
        "pokemon": "🎤 푸린",
        "pokemon_trait": "🌟 사람들 앞에서 빛나는 슈퍼스타 타입!",
        "pokemon_image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "careers": [
            {
                "job": "🎭 배우",
                "major": "📚 연극영화과",
                "personality": "표현력이 풍부함!"
            },
            {
                "job": "🎤 방송인",
                "major": "📚 방송연예과",
                "personality": "사람들 앞에 나서는 걸 좋아함!"
            }
        ]
    }
}

mbti = st.selectbox(
    "👇 너의 MBTI를 선택해봐!",
    sorted(career_data.keys())
)

if st.button("✨ 결과 보기"):

    data = career_data[mbti]

    st.markdown("---")

    st.header(f"💖 {mbti} 유형 결과!")

    st.subheader(f"{data['pokemon']}")
    st.image(data["pokemon_image"], width=220)

    st.info(data["pokemon_trait"])

    st.markdown("---")

    st.header("🎓 추천 진로")

    for career in data["careers"]:

        with st.container():

            st.subheader(career["job"])

            st.write(f"📚 추천 학과: {career['major']}")
            st.write(f"✨ 어울리는 성격: {career['personality']}")

            st.markdown("---")

    st.success("🎉 너와 찰떡인 포켓몬과 진로를 찾았어!")
    st.balloons()
