import streamlit as st



def check(passw):
    count_spec_symbol = 0
    count_upper = 0
    count_lower = 0
    for symbol in passw:
        if symbol in '""=!@#$%^&*()_*"№;:?</|':
            count_spec_symbol += 1
        if symbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            count_upper += 1
        if symbol in 'йцукенгшщзхъфывапролджэячсмитьбю':
            count_lower += 1
    if len(passw) < 3:
        st.text('Пароль должен содержать хотя бы 3 буквы')
    elif len(passw) >= 35:
        st.text('Пароль не должен иметь более 35 символов')
    elif 3 > count_upper:
        st.text('В вашем пароле должно быть не менее 3 русских заглавных букв')
    elif 4 < count_spec_symbol:
        st.text('В вашем пароле должно быть не более 4 спец. символов')
    elif '89' not in passw:
        st.text('Число 89 должно находиться в пароле')
    elif 'Joker' not in passw:
        st.text('Пароль должен содержать имя персонажа из фильмов про "Бэтмана" и карты ')
    elif 'Киянка' and 'киянка' not in passw:
        st.text('В пароле должно содержаться название "деревянного молотка"')

st.markdown("<h1 style='text-align: center; color: white;'>Парольная игра</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: green;'>""Я здесь чтобы помочь тебе создать сильнейший пароль в мире</p>", unsafe_allow_html=True)

st.subheader('Попробуй пройти все проверки')
IP = st.text_input('Введите пароль', max_chars= 67, type="password")
check(IP)   