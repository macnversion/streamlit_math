import streamlit as st
from src.utils.visualization import set_page_config
from src.utils.page_config import (
    PageID, 
    get_page_handler, 
    get_page_id_by_display_name,
    get_all_display_names
)

# 设置页面配置
set_page_config()

# 显示侧边栏导航
page_name = st.sidebar.selectbox(
    "选择页面",
    get_all_display_names()
)

# 获取页面ID
page_id = get_page_id_by_display_name(page_name)

if page_id:
    # 动态获取并调用页面处理函数
    page_handler = get_page_handler(page_id)
    page_handler()
else:
    st.markdown(f"# {page_name} 页面正在建设中...")