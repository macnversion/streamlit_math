"""
圆的性质与应用页面
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from src.utils.plot_utils import configure_matplotlib_defaults
from src.i18n.language_manager import get_text, add_language_selector

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
    ax.plot(x, y, 'b-', label=get_text("circumference"))
    ax.fill(x, y, alpha=0.1, color='blue')
    
    if show_components:
        # 绘制半径
        ax.plot([0, radius], [0, 0], 'r--', label=get_text("radius"))
        # 绘制直径
        ax.plot([-radius, radius], [0, 0], 'g--', label=get_text("diameter"))
        # 绘制弦 (使用60度角的两点)
        angle = np.pi/3  # 60度
        x1, y1 = radius * np.cos(angle), radius * np.sin(angle)
        x2, y2 = radius * np.cos(-angle), radius * np.sin(-angle)
        ax.plot([x1, x2], [y1, y2], 'm--', label=get_text("chord"))
        # 绘制切线
        ax.plot([radius, radius+1], [0, 0], 'y-', label=get_text("tangent"))
        # 绘制圆心
        ax.plot([0], [0], 'ko', label=get_text("center"))
        
        # 绘制扇形
        arc = Arc((0, 0), radius*2, radius*2, theta1=0, theta2=45, color='orange', label=get_text("arc"))
        ax.add_patch(arc)
    
    # 设置标题和标签
    ax.set_title(get_text("circle_basic_elements"), fontproperties=chinese_font)
    ax.legend(prop=chinese_font, loc='upper right')
    
    # 固定坐标轴范围
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True)
    ax.set_aspect('equal')
    
    plt.close()
    return fig

def draw_concentric_circles(radius1=2.0, radius2=1.0):
    """绘制同心圆"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    theta = np.linspace(0, 2*np.pi, 100)
    
    # 绘制外圆
    x1 = radius1 * np.cos(theta)
    y1 = radius1 * np.sin(theta)
    ax.plot(x1, y1, 'b-', label=f'{get_text("outer_circle")} (r={radius1})')
    ax.fill(x1, y1, alpha=0.1, color='blue')
    
    # 绘制内圆
    x2 = radius2 * np.cos(theta)
    y2 = radius2 * np.sin(theta)
    ax.plot(x2, y2, 'r-', label=f'{get_text("inner_circle")} (r={radius2})')
    ax.fill(x2, y2, alpha=0.1, color='red')
    
    # 绘制半径
    ax.plot([0, radius1], [0, 0], 'b--', alpha=0.5)
    ax.plot([0, radius2], [0, 0], 'r--', alpha=0.5)
    ax.plot([0], [0], 'ko', label=get_text("center"))
    
    ax.set_title(get_text("concentric_circles"), fontproperties=chinese_font)
    ax.legend(prop=chinese_font)
    
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    ax.set_xlabel(get_text("x_axis"), fontproperties=chinese_font)
    ax.set_ylabel(get_text("y_axis"), fontproperties=chinese_font)
    
    plt.close()
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
    ax.plot([0, radius], [0, 0], 'r--', label=get_text("radius"))
    ax.plot([0], [0], 'ko', label=get_text("center"))
    
    # 添加标注
    ax.annotate(f'{get_text("radius")} = {radius}', xy=(radius/2, 0.2), fontproperties=chinese_font)
    
    ax.set_title(get_text("circle_calculations"), fontproperties=chinese_font)
    ax.legend(prop=chinese_font)
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    ax.set_xlabel(get_text("x_axis"), fontproperties=chinese_font)
    ax.set_ylabel(get_text("y_axis"), fontproperties=chinese_font)
    
    plt.close()
    return fig

def calculate_polygon_properties(n_sides, radius=1, inscribed=True):
    """计算正多边形的顶点、周长和直径"""
    if inscribed:
        # 内接正多边形
        theta = np.linspace(0, 2*np.pi, n_sides, endpoint=False)
        vertices = radius * np.column_stack((np.cos(theta), np.sin(theta)))
        perimeter = n_sides * 2 * radius * np.sin(np.pi/n_sides)
        diagonal = 2 * radius
    else:
        # 外切正多边形
        # 外切圆的半径需要调整，使得内切圆半径为指定值
        outer_radius = radius / np.cos(np.pi/n_sides)  # 调整后的外切圆半径
        theta = np.linspace(0, 2*np.pi, n_sides, endpoint=False)
        vertices = outer_radius * np.column_stack((np.cos(theta), np.sin(theta)))
        perimeter = n_sides * 2 * outer_radius * np.sin(np.pi/n_sides)
        diagonal = 2 * outer_radius
    
    return vertices, perimeter, diagonal

def show_circles_page():
    """显示圆的页面"""
    # 添加语言选择器
    add_language_selector()
    
    st.title(get_text("circles_title"))
    
    # 创建四个标签页
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        get_text("circle_basics"),
        get_text("circle_properties"),
        get_text("concentric_circles"),
        get_text("circle_calculations"),
        get_text("pi_exploration")
    ])
    
    # 标签页1：圆的基础
    with tab1:
        st.header(get_text("circle_basic_concepts"))
        st.write(get_text("circle_definition"))
        
        st.markdown(f"""
        {get_text("basic_elements_intro")}:
        - {get_text("center_description")}
        - {get_text("radius_description")}
        - {get_text("diameter_description")}
        - {get_text("chord_description")}
        - {get_text("arc_description")}
        - {get_text("tangent_description")}
        """)
        
        show_components = st.checkbox(get_text("show_components"), value=True)
        fig = draw_circle_with_components(show_components=show_components)
        st.pyplot(fig)
    
    # 标签页2：圆的性质
    with tab2:
        st.header(get_text("important_properties"))
        st.write(f"""
        1. {get_text("inscribed_angle_properties")}
        - {get_text("inscribed_angle_theorem")}
        - {get_text("same_arc_angles")}
        
        2. {get_text("tangent_properties")}
        - {get_text("perpendicular_tangent")}
        - {get_text("equal_tangents")}
        
        3. {get_text("chord_properties")}
        - {get_text("perpendicular_bisector")}
        - {get_text("equal_chords")}
        
        4. {get_text("intersecting_chords")}
        - {get_text("intersecting_chords_theorem")}
        """)
        
        st.subheader(get_text("circle_symmetry"))
        st.write(get_text("circle_symmetry_description"))
    
    # 标签页3：同心圆
    with tab3:
        st.header(get_text("concentric_circles_demo"))
        
        col1, col2 = st.columns(2)
        
        with col1:
            radius1 = st.slider(
                get_text("adjust_outer_radius"),
                min_value=0.5,
                max_value=5.0,
                value=3.0,
                step=0.1,
                help=get_text("outer_radius_help"),
                key="geometry_circles_outer_radius"
            )
        
        with col2:
            radius2 = st.slider(
                get_text("adjust_inner_radius"),
                min_value=0.1,
                max_value=radius1 - 0.1,
                value=min(1.5, radius1 - 0.1),
                step=0.1,
                help=get_text("inner_radius_help"),
                key="geometry_circles_inner_radius"
            )
        
        # 显示圆的面积和周长
        col3, col4 = st.columns(2)
        with col3:
            area1 = np.pi * radius1 ** 2
            circumference1 = 2 * np.pi * radius1
            st.info(f"{get_text('outer_circle_metrics')}\n{get_text('area')}: {area1:.2f}\n{get_text('circumference')}: {circumference1:.2f}")
        
        with col4:
            area2 = np.pi * radius2 ** 2
            circumference2 = 2 * np.pi * radius2
            st.info(f"{get_text('inner_circle_metrics')}\n{get_text('area')}: {area2:.2f}\n{get_text('circumference')}: {circumference2:.2f}")
        
        ring_area = area1 - area2
        st.success(f"{get_text('ring_area')}: {ring_area:.2f}")
        
        fig = draw_concentric_circles(radius1, radius2)
        st.pyplot(fig)
    
    # 标签页4：圆的计算
    with tab4:
        st.header(get_text("circle_calculator"))
        
        radius = st.number_input(
            get_text("enter_radius"),
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
            st.metric(get_text("circle_area"), f"{area:.2f}")
            st.metric(get_text("circumference"), f"{circumference:.2f}")
        
        with col2:
            st.metric(get_text("diameter"), f"{diameter:.2f}")
            st.metric(get_text("pi_value"), f"{np.pi:.6f}")
        
        # 显示计算公式
        st.subheader(get_text("calculation_formulas"))
        st.latex(r"A = \pi r^2")
        st.latex(r"C = 2\pi r")
        st.latex(r"d = 2r")
        
        fig = draw_circle_calculator(radius)
        st.pyplot(fig)
    
    # 标签页5：圆周率 π
    with tab5:
        st.markdown(f"""
        ## {get_text("understanding_pi")}
        
        ### {get_text("pi_definition")}
        {get_text("pi_definition_text")}
        
        π = {get_text("pi_formula")}
        
        {get_text("pi_constant_text")}
        
        ### {get_text("pi_characteristics")}
        1. **{get_text("irrational_number")}**:
           - {get_text("irrational_description")}
           - {get_text("infinite_decimal")}
        
        2. **{get_text("transcendental_number")}**:
           - {get_text("transcendental_description")}
           - {get_text("no_algebraic_solution")}
        
        ### {get_text("pi_calculation_methods")}
        1. **{get_text("geometric_method")}**:
           - {get_text("polygon_approximation")}
           - {get_text("more_sides_better")}
        
        2. **{get_text("series_expansion")}**:
           - {get_text("leibniz_series")}
           - {get_text("ramanujan_series")}
        
        ### {get_text("pi_applications")}
        1. {get_text("circle_area_formula")}
        2. {get_text("circle_circumference_formula")}
        3. {get_text("sphere_volume_formula")}
        4. {get_text("sphere_surface_area_formula")}
        
        ### {get_text("pi_history")}
        {get_text("pi_history_text")}
        """)
        
        # 添加可视化演示
        st.subheader(get_text("pi_visualization"))
        
        col1, col2 = st.columns(2)
        with col1:
            radius = st.slider(get_text("adjust_circle_radius"), 0.5, 5.0, 2.0, 0.1, key="pi_demo_radius")
            
            # 计算圆的属性
            diameter = 2 * radius
            circumference = 2 * np.pi * radius
            ratio = circumference / diameter
            
            st.metric(get_text("diameter"), f"{diameter:.2f}")
            st.metric(get_text("circumference"), f"{circumference:.2f}")
            st.metric(get_text("pi_ratio"), f"{ratio:.6f}")