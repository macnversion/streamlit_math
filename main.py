"""
主程序入口
"""
import streamlit as st
from src.utils.page_config import (
    PageID, 
    get_page_handler, 
    get_page_id_by_display_name,
    get_all_display_names
)

def set_page_config():
    """设置页面配置"""
    st.set_page_config(
        page_title="数学可视化",
        page_icon="📐",
        layout="wide"
    )

def main():
    """主函数"""
    set_page_config()
    
    # 显示侧边栏导航
    page_name = st.sidebar.selectbox(
        "选择页面",
        get_all_display_names()
    )

    # 获取页面ID
    page_id = get_page_id_by_display_name(page_name)

    if page_id:
        # 获取并调用页面处理函数
        page_handler = get_page_handler(page_id)
        page_handler()
    else:
        st.markdown(f"# {page_name} 页面正在建设中...")

if __name__ == "__main__":
    main()