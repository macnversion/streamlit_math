"""
多边形的可视化页面
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from ...components.polygon_drawer import draw_polygon_component
from ...utils.plot_utils import configure_matplotlib_defaults
from ...i18n.language_manager import get_text, add_language_selector

# 获取中文字体
chinese_font = configure_matplotlib_defaults()

def plot_regular_polygon(n, size=1):
    """绘制正n边形"""
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = size * np.cos(angles)
    y = size * np.sin(angles)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), 'b-')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f'{get_text("regular_polygons")} ({n})', fontproperties=chinese_font)
    
    # 设置坐标轴范围，确保图形居中显示
    margin = 0.2
    ax.set_xlim(-size-margin, size+margin)
    ax.set_ylim(-size-margin, size+margin)
    
    # 添加坐标轴标签
    ax.set_xlabel('x', fontproperties=chinese_font)
    ax.set_ylabel('y', fontproperties=chinese_font)
    
    plt.close()
    return fig

def show_polygons_page():
    """显示多边形页面"""
    # 添加语言选择器
    add_language_selector()
    
    st.title(get_text("polygons_title"))
    
    # 创建选项卡
    tab1, tab2, tab3, tab4 = st.tabs([
        get_text("regular_polygons"),
        get_text("polygons_intro"),
        get_text("properties"),
        get_text("fun_facts")
    ])
    
    # Tab 1: 正多边形
    with tab1:
        st.header(get_text("regular_polygons"))
        
        # 创建两列布局
        left_col, right_col = st.columns([1, 1])
        
        # 左列：控制滑块和图形
        with left_col:
            # 滑块控制
            n_sides = st.slider(get_text("number_of_sides"), min_value=3, max_value=36, value=5)
            size = st.slider(get_text("side_length"), min_value=0.5, max_value=2.0, value=1.0, step=0.1)
            
            # 图形显示
            fig = plot_regular_polygon(n_sides, size)
            st.pyplot(fig)
        
        # 右列：文字说明
        with right_col:
            st.markdown(f"""
            ### {get_text("regular_polygons")} ({n_sides})
            
            {get_text("polygons_intro")}

            ### {get_text("properties")}
            1. **{get_text("side_length")}**
               - {get_text("equal_sides")}
               - {get_text("number_of_sides")}: {n_sides}
            
            2. **{get_text("angles")}**
               - {get_text("equal_interior_angles")}
               - {get_text("equal_exterior_angles")}
               - {get_text("sum_of_interior_angles")}: {(n_sides-2)*180}°
               - {get_text("interior_angle")}: {(n_sides-2)*180/n_sides}°
               - {get_text("exterior_angle")}: {360/n_sides}°
            
            3. **{get_text("symmetry")}**
               - {get_text("symmetry_axes")}: {n_sides}
               - {get_text("rotational_symmetry")}: {360/n_sides}°
            
            4. **{get_text("circle_relationships")}**
               - {get_text("inscribed_circle")}
               - {get_text("circumscribed_circle")}
               - {get_text("equal_radius")}
            """)
    
    # Tab 2: 多边形基础
    with tab2:
        st.markdown(f"""
        ## {get_text("what_is_polygon")}
        
        {get_text("polygon_definition")}
        
        ### {get_text("basic_elements")}
        1. **{get_text("vertices")}**: {get_text("vertices_description")}
        2. **{get_text("sides")}**: {get_text("sides_description")}
        3. **{get_text("interior_angles")}**: {get_text("interior_angles_description")}
        4. **{get_text("exterior_angles")}**: {get_text("exterior_angles_description")}
        
        ### {get_text("polygon_classification")}
        
        {get_text("by_sides")}:
        - {get_text("triangle")} (3)
        - {get_text("quadrilateral")} (4)
        - {get_text("pentagon")} (5)
        - {get_text("hexagon")} (6)
        
        {get_text("by_shape")}:
        - **{get_text("convex_polygon")}**: {get_text("convex_description")}
        - **{get_text("concave_polygon")}**: {get_text("concave_description")}
        - **{get_text("regular_polygon")}**: {get_text("regular_description")}
        - **{get_text("irregular_polygon")}**: {get_text("irregular_description")}
        """)
        
    # Tab 3: 多边形性质
    with tab3:
        st.markdown(f"""
        ## {get_text("important_properties")}
        
        ### 1. {get_text("sum_of_interior_angles")}
        {get_text("interior_angles_formula")}
        
        {get_text("examples")}:
        - {get_text("triangle")}: (3-2) × 180° = 180°
        - {get_text("quadrilateral")}: (4-2) × 180° = 360°
        - {get_text("pentagon")}: (5-2) × 180° = 540°
        
        ### 2. {get_text("sum_of_exterior_angles")}
        {get_text("exterior_angles_property")}
        
        ### 3. {get_text("number_of_diagonals")}
        {get_text("diagonals_formula")}
        
        {get_text("examples")}:
        - {get_text("triangle")}: 3(3-3) ÷ 2 = 0
        - {get_text("quadrilateral")}: 4(4-3) ÷ 2 = 2
        - {get_text("pentagon")}: 5(5-3) ÷ 2 = 5
        
        ### 4. {get_text("area")}
        - **{get_text("regular_polygon")}**: {get_text("regular_area_formula")}
        - **{get_text("irregular_polygon")}**: {get_text("irregular_area_description")}
        """)
        
        # 添加面积计算器
        st.markdown(f"### {get_text('area_calculator')}")
        col1, col2 = st.columns(2)
        with col1:
            sides = st.number_input(get_text("number_of_sides"), min_value=3, max_value=12, value=6, key="geometry_polygons_calc_sides")
            side_length = st.number_input(get_text("side_length"), min_value=0.1, max_value=100.0, value=1.0, key="geometry_polygons_calc_side_length")
        with col2:
            # 计算面积
            angle = np.pi / sides
            radius = side_length / (2 * np.sin(angle))
            area = sides * side_length * radius / 2
            st.metric(get_text("area"), f"{area:.2f}")

    # Tab 4: 趣味知识
    with tab4:
        st.markdown(f"""
        ## {get_text("fun_facts")}
        
        ### 1. {get_text("bee_nest_secret")}
        {get_text("bee_nest_description")}
        
        ### 2. {get_text("gauss_and_17_gon")}
        {get_text("gauss_description")}
        
        ### 3. {get_text("polygons_in_nature")}
        {get_text("polygons_in_nature_description")}
        
        ### 4. {get_text("polygons_in_life")}
        {get_text("polygons_in_life_description")}
        """)