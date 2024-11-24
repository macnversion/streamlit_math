"""语言管理器"""
import streamlit as st
from .translations import TRANSLATIONS

def get_language():
    """获取当前语言"""
    if 'language' not in st.session_state:
        st.session_state.language = 'zh'
    return st.session_state.language

def set_language(lang):
    """设置当前语言"""
    st.session_state.language = lang

def get_text(key):
    """获取指定key的翻译文本"""
    lang = get_language()
    return TRANSLATIONS[lang].get(key, key)

def add_language_selector():
    """添加语言选择器"""
    lang = get_language()
    languages = {
        'zh': get_text('chinese'),
        'en': get_text('english')
    }
    
    # 创建一个小容器来放置语言选择器
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col2:
            selected_lang = st.selectbox(
                get_text('language'),
                options=list(languages.keys()),
                format_func=lambda x: languages[x],
                index=list(languages.keys()).index(lang),
                key='language_selector'
            )
            
            if selected_lang != lang:
                set_language(selected_lang)
                st.rerun()
