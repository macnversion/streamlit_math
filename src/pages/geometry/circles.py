"""
圆的性质与应用页面
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from src.utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib并获取中文字体
chinese_font = configure_matplotlib_defaults()

def draw_circle_with_components(radius=2.0, show_components=True):
    """绘制带有各种组成部分的圆"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 生成圆的点
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # 绘制圆
    ax.plot(x, y, 'b-', label='圆周')
    ax.fill(x, y, alpha=0.1, color='blue')
    
    if show_components:
        # 绘制半径
        ax.plot([0, radius], [0, 0], 'r--', label='半径')
        # 绘制直径
        ax.plot([-radius, radius], [0, 0], 'g--', label='直径')
        # 绘制弦 (使用60度角的两点)
        angle = np.pi/3  # 60度
        x1, y1 = radius * np.cos(angle), radius * np.sin(angle)
        x2, y2 = radius * np.cos(-angle), radius * np.sin(-angle)
        ax.plot([x1, x2], [y1, y2], 'm--', label='弦')
        # 绘制切线
        ax.plot([radius, radius+1], [0, 0], 'y-', label='切线')
        # 绘制圆心
        ax.plot([0], [0], 'ko', label='圆心')
        
        # 绘制扇形
        arc = Arc((0, 0), radius*2, radius*2, theta1=0, theta2=45, color='orange', label='弧')
        ax.add_patch(arc)
    
    # 设置标题和标签
    ax.set_title('圆的基本元素', fontproperties=chinese_font)
    ax.legend(prop=chinese_font, loc='upper right')
    
    # 固定坐标轴范围
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    
    # 添加网格和坐标轴
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    ax.set_xlabel('X轴', fontproperties=chinese_font)
    ax.set_ylabel('Y轴', fontproperties=chinese_font)
    
    return fig

def draw_concentric_circles(radius1=2.0, radius2=1.0):
    """绘制同心圆"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    theta = np.linspace(0, 2*np.pi, 100)
    
    # 绘制外圆
    x1 = radius1 * np.cos(theta)
    y1 = radius1 * np.sin(theta)
    ax.plot(x1, y1, 'b-', label=f'外圆 (r={radius1})')
    ax.fill(x1, y1, alpha=0.1, color='blue')
    
    # 绘制内圆
    x2 = radius2 * np.cos(theta)
    y2 = radius2 * np.sin(theta)
    ax.plot(x2, y2, 'r-', label=f'内圆 (r={radius2})')
    ax.fill(x2, y2, alpha=0.1, color='red')
    
    # 绘制半径
    ax.plot([0, radius1], [0, 0], 'b--', alpha=0.5)
    ax.plot([0, radius2], [0, 0], 'r--', alpha=0.5)
    ax.plot([0], [0], 'ko', label='圆心')
    
    ax.set_title('同心圆', fontproperties=chinese_font)
    ax.legend(prop=chinese_font)
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    ax.set_xlabel('X轴', fontproperties=chinese_font)
    ax.set_ylabel('Y轴', fontproperties=chinese_font)
    
    return fig

def draw_circle_calculator(radius=2.0):
    """绘制用于计算的圆"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    ax.plot(x, y, 'b-')
    ax.fill(x, y, alpha=0.1, color='blue')
    
    # 绘制半径
    ax.plot([0, radius], [0, 0], 'r--', label='半径')
    ax.plot([0], [0], 'ko', label='圆心')
    
    # 添加标注
    ax.annotate(f'r = {radius}', xy=(radius/2, 0.2), fontproperties=chinese_font)
    
    ax.set_title('圆的计算', fontproperties=chinese_font)
    ax.legend(prop=chinese_font)
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    return fig

def show_circles_page():
    """显示圆的页面"""
    st.title("圆")
    
    # 创建四个标签页
    tab1, tab2, tab3, tab4 = st.tabs([
        "圆的基础",
        "圆的性质",
        "同心圆",
        "圆的计算"
    ])
    
    # 标签页1：圆的基础
    with tab1:
        st.header("圆的基本概念")
        st.write("""
        圆是平面上到定点（圆心）距离相等的所有点的集合。这个固定的距离称为圆的半径。

        圆的基本元素包括：
        - 圆心：圆上所有点到圆心的距离相等
        - 半径：从圆心到圆周上任意一点的线段
        - 直径：通过圆心的弦，等于两倍半径
        - 弦：连接圆周上两点的线段
        - 弧：圆周上两点之间的部分
        - 切线：与圆周相切的直线
        """)
        
        show_components = st.checkbox("显示圆的组成部分", value=True)
        fig = draw_circle_with_components(show_components=show_components)
        st.pyplot(fig)
    
    # 标签页2：圆的性质
    with tab2:
        st.header("圆的重要性质")
        st.write("""
        1. 圆周角性质
        - 圆周角等于它所对的圆心角的一半
        - 同弧所对的圆周角相等
        
        2. 切线性质
        - 切线与半径垂直
        - 切点到圆心的距离等于半径
        
        3. 弦的性质
        - 垂直平分弦的直径必过圆心
        - 相等的弦到圆心的距离相等
        
        4. 相交弦性质
        - 圆中相交弦所形成的两条线段的乘积相等
        """)
        
        st.subheader("圆的对称性")
        st.write("""
        圆具有无数个对称轴，任何通过圆心的直线都是圆的对称轴。
        这使得圆成为最完美的几何图形之一。
        """)
    
    # 标签页3：同心圆
    with tab3:
        st.header("同心圆演示")
        
        col1, col2 = st.columns(2)
        
        with col1:
            radius1 = st.slider(
                "调整外圆半径",
                min_value=0.5,
                max_value=5.0,
                value=3.0,
                step=0.1,
                help="拖动滑块来改变外圆的大小",
                key="geometry_circles_outer_radius"
            )
        
        with col2:
            radius2 = st.slider(
                "调整内圆半径",
                min_value=0.1,
                max_value=radius1 - 0.1,
                value=min(1.5, radius1 - 0.1),
                step=0.1,
                help="拖动滑块来改变内圆的大小",
                key="geometry_circles_inner_radius"
            )
        
        # 显示圆的面积和周长
        col3, col4 = st.columns(2)
        with col3:
            area1 = np.pi * radius1 ** 2
            circumference1 = 2 * np.pi * radius1
            st.info(f"外圆面积：{area1:.2f}\n外圆周长：{circumference1:.2f}")
        
        with col4:
            area2 = np.pi * radius2 ** 2
            circumference2 = 2 * np.pi * radius2
            st.info(f"内圆面积：{area2:.2f}\n内圆周长：{circumference2:.2f}")
        
        ring_area = area1 - area2
        st.success(f"圆环面积：{ring_area:.2f}")
        
        fig = draw_concentric_circles(radius1, radius2)
        st.pyplot(fig)
    
    # 标签页4：圆的计算
    with tab4:
        st.header("圆的计算器")
        
        radius = st.number_input(
            "输入圆的半径",
            min_value=0.1,
            max_value=10.0,
            value=2.0,
            step=0.1,
            key="geometry_circles_calc_radius"
        )
        
        # 计算各种值
        area = np.pi * radius ** 2
        circumference = 2 * np.pi * radius
        diameter = 2 * radius
        
        # 显示计算结果
        col1, col2 = st.columns(2)
        with col1:
            st.metric("圆的面积", f"{area:.2f}")
            st.metric("圆的周长", f"{circumference:.2f}")
        
        with col2:
            st.metric("圆的直径", f"{diameter:.2f}")
            st.metric("圆周率 (π)", f"{np.pi:.6f}")
        
        # 显示计算公式
        st.subheader("计算公式")
        st.latex(r"面积 = \pi r^2")
        st.latex(r"周长 = 2\pi r")
        st.latex(r"直径 = 2r")
        
        fig = draw_circle_calculator(radius)
        st.pyplot(fig)