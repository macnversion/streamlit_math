"""
窗帘模型：几何变换与伸缩
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import plotly.graph_objects as go

def draw_curtain_model(scale_factor=1.0, direction='vertical', shape='rectangle'):
    """
    绘制窗帘模型的高级版本
    
    Args:
        scale_factor (float): 缩放因子
        direction (str): 变换方向 'vertical' 或 'horizontal'
        shape (str): 形状类型 'rectangle' 或 'circle'
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 绘制网格
    grid_size = 6
    for i in range(grid_size + 1):
        ax.plot([i, i], [0, grid_size], 'gray', alpha=0.2, linewidth=0.5)
        ax.plot([0, grid_size], [i, i], 'gray', alpha=0.2, linewidth=0.5)
    
    # 设置基础形状
    base_x, base_y = 2, 2
    base_width, base_height = 2, 2
    
    # 根据缩放方向和形状调整
    if direction == 'vertical':
        draw_height = base_height * scale_factor
        draw_width = base_width
    else:  # horizontal
        draw_height = base_height
        draw_width = base_width * scale_factor
    
    # 绘制形状
    if shape == 'rectangle':
        rect = Rectangle(
            (base_x, base_y), 
            draw_width, draw_height, 
            facecolor='lightblue', 
            edgecolor='blue', 
            alpha=0.5
        )
        ax.add_patch(rect)
    else:  # circle
        # 计算圆的半径
        if direction == 'vertical':
            radius = base_height * scale_factor / 2
        else:
            radius = base_width * scale_factor / 2
        
        circle = Circle(
            (base_x + base_width/2, base_y + base_height/2), 
            radius, 
            facecolor='lightgreen', 
            edgecolor='green', 
            alpha=0.5
        )
        ax.add_patch(circle)
    
    # 设置坐标轴
    ax.set_xlim(-0.5, grid_size + 0.5)
    ax.set_ylim(-0.5, grid_size + 0.5)
    ax.set_aspect('equal')
    
    # 添加标题和说明
    transform_type = "垂直" if direction == 'vertical' else "水平"
    plt.title(f"{transform_type}方向{shape}伸缩变换 (k = {scale_factor:.2f})")
    
    return fig

def render_curtain_page():
    """渲染窗帘模型页面的高级版本"""
    st.title("窗帘模型：几何变换与伸缩")
    
    # 数学公式展示
    st.latex(r"""
    \text{伸缩变换公式：} 
    \begin{cases} 
    x' = kx & \text{水平方向} \\
    y' = ky & \text{垂直方向}
    \end{cases}
    """)
    
    # 创建三列布局
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.subheader("垂直方向-矩形")
        vertical_scale = st.slider(
            "垂直伸缩因子", 
            min_value=0.1, 
            max_value=3.0, 
            value=1.0,
            key="vertical_rect"
        )
        fig_v_rect = draw_curtain_model(vertical_scale, 'vertical', 'rectangle')
        st.pyplot(fig_v_rect)
    
    with col2:
        st.subheader("水平方向-矩形")
        horizontal_scale = st.slider(
            "水平伸缩因子",
            min_value=0.1,
            max_value=3.0,
            value=1.0,
            key="horizontal_rect"
        )
        fig_h_rect = draw_curtain_model(horizontal_scale, 'horizontal', 'rectangle')
        st.pyplot(fig_h_rect)
    
    with col3:
        st.subheader("圆形伸缩")
        circle_scale = st.slider(
            "圆形伸缩因子",
            min_value=0.1,
            max_value=3.0,
            value=1.0,
            key="circle_scale"
        )
        fig_circle = draw_curtain_model(circle_scale, 'vertical', 'circle')
        st.pyplot(fig_circle)
    
    # 交互式解释区域
    st.markdown("""
    ### 窗帘模型的数学原理
    
    #### 伸缩变换的基本概念
    
    1. **定义**：通过乘以一个非零常数 k 来改变图形的大小
    2. **特点**：
       - k > 1 时，图形放大
       - 0 < k < 1 时，图形缩小
       - k = 1 时，图形保持不变
    
    #### 面积变化规律
    
    - 矩形面积变化：$S' = k \cdot S$
    - 圆形面积变化：$S' = k^2 \cdot S$
    
    ### 应用场景
    
    1. 几何图形的比例变换
    2. 工程制图中的缩放
    3. 计算机图形学中的图像处理
    """)
    
    # 交互性测验
    st.subheader("测试你的理解")
    
    test_question = st.radio(
        "如果一个矩形的边长是 4，伸缩因子为 2，新的边长是？",
        ["6", "8", "2", "4"]
    )
    
    if test_question == "8":
        st.success("正确！边长乘以伸缩因子 4 * 2 = 8")
    else:
        st.warning("请再仔细思考一下")

# 添加交互性测验
def interactive_quiz():
    """额外的交互性测验"""
    st.title("窗帘模型测验")
    
    questions = [
        {
            "question": "伸缩因子 k = 2 对一个边长为 5 的正方形意味着什么？",
            "options": ["边长变为 2", "边长变为 10", "边长变为 5", "边长变为 7"],
            "correct": "边长变为 10"
        },
        {
            "question": "当 0 < k < 1 时，图形会发生什么变化？",
            "options": ["放大", "缩小", "旋转", "不变"],
            "correct": "缩小"
        }
    ]
    
    for i, q in enumerate(questions, 1):
        st.subheader(f"问题 {i}")
        answer = st.radio(q["question"], q["options"])
        
        if answer == q["correct"]:
            st.success("回答正确！")
        else:
            st.warning("请再仔细思考")

# 可选的额外交互测验入口
def render_curtain_page_with_quiz():
    """结合主页面和测验"""
    render_curtain_page()
    
    if st.checkbox("开始测验"):
        interactive_quiz()

render_curtain_page_with_quiz()
