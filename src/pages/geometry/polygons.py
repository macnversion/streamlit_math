import streamlit as st
from ...components.polygon_drawer import draw_polygon_component

def show_polygons_page():
    """显示多边形页面"""
    st.title("多边形探索")
    
    # 添加页面导航
    topic = st.selectbox(
        "选择主题",
        ["正多边形基础", "高斯17边形构造", "多边形的性质"]
    )
    
    if topic == "正多边形基础":
        st.markdown("""
        ## 正多边形基础
        
        正多边形是一个具有以下性质的多边形：
        1. 所有边长相等
        2. 所有内角相等
        3. 所有顶点到中心的距离相等
        
        使用下面的交互工具来探索正多边形：
        """)
        draw_polygon_component()
        
    elif topic == "高斯17边形构造":
        st.markdown("""
        ## 高斯17边形构造
        
        高斯在19岁时证明了可以用尺规作图作出正17边形，这是数学史上的重要发现。
        
        下面我们将一步步展示构造过程：
        """)
        pass
        
    else:
        st.markdown("""
        ## 多边形的性质
        
        ### 内角和公式
        n边形的内角和 = (n-2) × 180°
        
        ### 外角和
        任何多边形的外角和都等于360°
        """)
        # 这里可以添加更多的性质说明和演示