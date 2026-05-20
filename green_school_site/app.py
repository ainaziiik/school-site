import streamlit as st

st.title("Кыздар мектеби")
st.write("Биздин мектепке кош келиңиз!")

import streamlit as st

st.set_page_config(
    page_title="Кыздар мектеби",
    layout="wide",
)

# CSS
with open("./green_school_site/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
    <h2>Кыздар мектеби</h2>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="overlay">
        <h1>Кыздар мектеби</h1>
        <p>Билим • Тарбия • Келечек</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass card">
        <h3>🏆 Жетишкендиктер</h3>
        <p>Олимпиада жана сынак жеңүүчүлөрү.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass card">
        <h3>📰 Жаңылыктар</h3>
        <p>Мектептеги акыркы жаңылыктар.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass card">
        <h3>🎨 Ийримдер</h3>
        <p>Кошумча өнүгүү мүмкүнчүлүктөрү.</p>
    </div>
    """, unsafe_allow_html=True)

# Gallery
st.markdown("## 📸 Галерея")

gallery1, gallery2, gallery3 = st.columns(3)

with gallery1:
    st.image("./green_school_site/images/school1.jpg")

with gallery2:
    st.image("./green_school_site/images/school2.jpg")

with gallery3:
    st.image("./green_school_site/images/school3.jpg")

# Teachers
st.markdown("## 👩‍🏫 Мугалимдер")

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
    <div class="glass teacher-card">
        <h4>Айгүл эже</h4>
        <p>Математика</p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="glass teacher-card">
        <h4>Нурзат эже</h4>
        <p>Кыргыз тили</p>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="glass teacher-card">
        <h4>Жылдыз эже</h4>
        <p>Информатика</p>
    </div>
    """, unsafe_allow_html=True)

# Contacts
st.markdown("## 📍 Байланыш")

st.markdown("""
<div class="glass contact">
    <p>📞 +996 XXX XX XX XX</p>
    <p>📍 Бишкек шаары</p>
    <p>✉ school@gmail.com</p>
</div>
""", unsafe_allow_html=True)