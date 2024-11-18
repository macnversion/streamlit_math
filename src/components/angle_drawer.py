import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from ..utils.visualization import create_figure, setup_coordinate_system

def calculate_angle_points(angle_deg, radius=5, num_points=100):
    """计算角的边的点坐标
    
    Args:
        angle_deg: 角度（度数）
        radius: 射线长度
        num_points: 用于绘制弧的点数
        
    Returns:
        tuple: (起始射线点集, 终止射线点集, 弧线点集)
    """
    # 转换为弧度
    angle_rad = np.radians(angle_deg)
    
    # 计算起始射线的点（水平线）
    x_start = np.array([0, radius])
    y_start = np.array([0, 0])
    
    # 计算终止射线的点
    x_end = np.array([0, radius * np.cos(angle_rad)])
    y_end = np.array([0, radius * np.sin(angle_rad)])
    
    # 计算弧线点
    if angle_deg > 0:
        theta = np.linspace(0, angle_rad, num_points)
    else:
        theta = np.linspace(angle_rad, 0, num_points)
    arc_radius = radius * 0.3  # 弧的半径为射线长度的30%
    x_arc = arc_radius * np.cos(theta)
    y_arc = arc_radius * np.sin(theta)
    
    return (x_start, y_start), (x_end, y_end), (x_arc, y_arc)

def draw_angle_component():
    """角度绘制组件"""
    st.subheader("角度探索器")
    
    col1, col2 = st.columns(2)
    
    with col1:
        angle = st.slider("角度", min_value=-360, max_value=360, value=45,
                         help="拖动滑块改变角度大小（正值为逆时针，负值为顺时针）",
                         key="angle_slider")
        radius = st.slider("射线长度", min_value=1.0, max_value=10.0, value=5.0,
                          key="radius_slider")
    
    with col2:
        show_grid = st.checkbox("显示网格", value=True, key="show_grid_basic")
        show_degree = st.checkbox("显示度数", value=True, key="show_degree_basic")
        margin = st.slider("图形边距", min_value=1.1, max_value=2.0, value=1.5,
                          key="margin_slider")
    
    fig, ax = create_figure()
    
    # 计算角的点集
    (x_start, y_start), (x_end, y_end), (x_arc, y_arc) = calculate_angle_points(angle, radius)
    
    # 设置坐标系范围
    max_coord = radius * margin
    setup_coordinate_system(ax, xlim=(-max_coord, max_coord), ylim=(-max_coord, max_coord))
    
    # 绘制射线
    ax.plot(x_start, y_start, 'b-', linewidth=2)  # 起始射线
    ax.plot(x_end, y_end, 'b-', linewidth=2)      # 终止射线
    
    # 绘制弧线
    ax.plot(x_arc, y_arc, 'r-', linewidth=2)
    
    # 显示角度值
    if show_degree:
        arc_center_idx = len(x_arc) // 2
        text_x = x_arc[arc_center_idx] * 1.5
        text_y = y_arc[arc_center_idx] * 1.5
        ax.text(text_x, text_y, f'{angle}°', fontsize=12)
    
    # 设置网格
    ax.grid(show_grid)
    
    # 在原点添加一个点
    ax.plot(0, 0, 'ko')
    
    st.pyplot(fig)

def draw_special_angles_component():
    """特殊角度展示组件"""
    st.subheader("认识特殊角")
    
    special_angles = {
        "直角": 90,
        "锐角": 45,
        "钝角": 135,
        "平角": 180,
        "周角": 360
    }
    
    selected_angle = st.selectbox(
        "选择特殊角",
        list(special_angles.keys()),
        key="special_angle_select"
    )
    
    angle = special_angles[selected_angle]
    
    # 使用基本角度绘制组件的函数绘制选中的特殊角
    fig, ax = create_figure()
    (x_start, y_start), (x_end, y_end), (x_arc, y_arc) = calculate_angle_points(angle)
    
    # 设置坐标系范围
    setup_coordinate_system(ax, xlim=(-6, 6), ylim=(-6, 6))
    
    # 绘制角
    ax.plot(x_start, y_start, 'b-', linewidth=2)
    ax.plot(x_end, y_end, 'b-', linewidth=2)
    ax.plot(x_arc, y_arc, 'r-', linewidth=2)
    
    # 显示角度值和说明
    ax.text(1, 1, f'{angle}°', fontsize=12)
    
    st.pyplot(fig)
    
    # 显示说明文本
    angle_descriptions = {
        "直角": "90度角，是两条相互垂直的直线所成的角。在日常生活中很常见，比如房屋的墙角、课本的四角等。",
        "锐角": "小于90度的角。45度角是一个典型的锐角，它将直角平分。",
        "钝角": "大于90度但小于180度的角。135度角是一个典型的钝角，它比直角大45度。",
        "平角": "180度角，两条射线在同一直线上。",
        "周角": "360度角，一个完整的圆周。"
    }
    
    st.markdown(f"**{selected_angle}的说明：**")
    st.write(angle_descriptions[selected_angle])

def draw_dynamic_coordinate_system_component():
    """动态坐标系调整组件"""
    st.subheader("动态坐标系调整")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_min = st.slider("x轴最小值", min_value=-10.0, max_value=10.0, value=-5.0,
                         key="x_min_slider")
        x_max = st.slider("x轴最大值", min_value=-10.0, max_value=10.0, value=5.0,
                         key="x_max_slider")
    
    with col2:
        y_min = st.slider("y轴最小值", min_value=-10.0, max_value=10.0, value=-5.0,
                         key="y_min_slider")
        y_max = st.slider("y轴最大值", min_value=-10.0, max_value=10.0, value=5.0,
                         key="y_max_slider")
    
    fig, ax = create_figure()
    
    # 设置坐标系范围
    setup_coordinate_system(ax, xlim=(x_min, x_max), ylim=(y_min, y_max))
    
    st.pyplot(fig)

def draw_interactive_control_component():
    """交互控制选项组件"""
    st.subheader("交互控制选项")
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_grid = st.checkbox("显示网格", value=True, key="show_grid_interactive")
        show_axis = st.checkbox("显示坐标轴", value=True, key="show_axis_interactive")
    
    with col2:
        show_title = st.checkbox("显示标题", value=True, key="show_title_interactive")
        show_legend = st.checkbox("显示图例", value=True, key="show_legend_interactive")
    
    fig, ax = create_figure()
    
    # 设置交互控制选项
    ax.grid(show_grid)
    ax.axis('on' if show_axis else 'off')
    ax.set_title('交互控制选项' if show_title else '')
    ax.legend([] if show_legend else None)
    
    st.pyplot(fig)

# 绘制所有组件
draw_angle_component()
draw_special_angles_component()
draw_dynamic_coordinate_system_component()
draw_interactive_control_component()