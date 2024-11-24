import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from ..utils.visualization import create_figure, setup_coordinate_system
from ..utils.plot_utils import configure_matplotlib_defaults
from ..i18n.language_manager import get_text

# 配置matplotlib并获取中文字体
chinese_font = configure_matplotlib_defaults()

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

def draw_angle(angle_deg):
    """绘制角度"""
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # 计算角的点
    (x_start, y_start), (x_end, y_end), (x_arc, y_arc) = calculate_angle_points(angle_deg)
    
    # 绘制射线
    ax.plot(x_start, y_start, 'b-', linewidth=2, label=get_text('start_side'))
    ax.plot(x_end, y_end, 'r-', linewidth=2, label=get_text('end_side'))
    
    # 绘制弧线
    ax.plot(x_arc, y_arc, 'g-', linewidth=2)
    
    # 添加角度标注
    arc_center_idx = len(x_arc) // 2
    arc_center_x = x_arc[arc_center_idx] * 1.5
    arc_center_y = y_arc[arc_center_idx] * 1.5
    ax.text(arc_center_x, arc_center_y, f'{abs(angle_deg)}°',
            fontproperties=chinese_font, fontsize=12)
    
    # 设置图形属性
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_title(get_text('angle_visualization'), fontproperties=chinese_font)
    ax.set_xlabel('x', fontproperties=chinese_font)
    ax.set_ylabel('y', fontproperties=chinese_font)
    ax.legend(prop=chinese_font)
    
    return fig

def draw_angle_component():
    """角度绘制组件"""
    st.subheader(get_text('angle_explorer'))
    
    # 移除原来的列布局，改为垂直布局
    angle = st.slider(get_text('angle'), min_value=-360, max_value=360, value=45,
                     help=get_text('angle_slider_help'),
                     key="angle_explorer")
    
    st.markdown(f"""
    {get_text('current_angle')}：**{angle}°**
    
    {get_text('characteristics')}：
    - {get_text('acute_angle') if 0 < abs(angle) < 90 else get_text('right_angle') if abs(angle) == 90 else get_text('obtuse_angle') if 90 < abs(angle) < 180 else get_text('straight_angle') if abs(angle) == 180 else get_text('reflex_angle') if 180 < abs(angle) < 360 else get_text('zero_angle')}
    - {get_text('counterclockwise') if angle > 0 else get_text('clockwise') if angle < 0 else get_text('zero_angle')}
    """)
    
    # 图形放在特点说明的下面
    fig = draw_angle(angle)
    st.pyplot(fig)

def draw_special_angles_component():
    """特殊角度展示组件"""
    st.subheader(get_text('special_angles'))
    
    special_angles = {
        "30°": (30, 'special_angle_30'),
        "45°": (45, 'special_angle_45'),
        "60°": (60, 'special_angle_60'),
        "90°": (90, 'special_angle_90'),
        "120°": (120, 'special_angle_120'),
        "180°": (180, 'special_angle_180')
    }
    
    selected_angle = st.selectbox(
        get_text('select_special_angle'),
        list(special_angles.keys()),
        key="special_angle_selector"
    )
    
    angle, description_key = special_angles[selected_angle]
    fig = draw_angle(angle)
    st.pyplot(fig)
    
    # 添加说明
    st.markdown(get_text(description_key))

def draw_dynamic_coordinate_system_component():
    """动态坐标系调整组件"""
    st.subheader("动态坐标系调整")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_min = st.slider("x轴最小值", min_value=-10.0, max_value=10.0, value=-5.0,
                         key="x_min_adjuster")  # 使用更具描述性的key
        x_max = st.slider("x轴最大值", min_value=-10.0, max_value=10.0, value=5.0,
                         key="x_max_adjuster")  # 使用更具描述性的key
    
    with col2:
        y_min = st.slider("y轴最小值", min_value=-10.0, max_value=10.0, value=-5.0,
                         key="y_min_adjuster")  # 使用更具描述性的key
        y_max = st.slider("y轴最大值", min_value=-10.0, max_value=10.0, value=5.0,
                         key="y_max_adjuster")  # 使用更具描述性的key
    
    # 创建一个居中的容器
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:  # 使用中间的列来显示图形
        fig, ax = create_figure(figsize=(4, 4))  # 使用较小的图形尺寸
        
        # 设置坐标系范围
        setup_coordinate_system(ax, xlim=(x_min, x_max), ylim=(y_min, y_max))
        
        st.pyplot(fig)

def draw_interactive_control_component():
    """交互控制选项组件"""
    st.subheader("交互控制选项")
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_grid = st.checkbox("显示网格", value=True, key="show_grid_controller")  # 使用更具描述性的key
        show_axis = st.checkbox("显示坐标轴", value=True, key="show_axis_controller")  # 使用更具描述性的key
    
    with col2:
        show_title = st.checkbox("显示标题", value=True, key="show_title_controller")  # 使用更具描述性的key
        show_legend = st.checkbox("显示图例", value=True, key="show_legend_controller")  # 使用更具描述性的key
    
    # 创建一个居中的容器
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:  # 使用中间的列来显示图形
        fig, ax = create_figure(figsize=(4, 4))  # 使用较小的图形尺寸
        
        # 设置交互控制选项
        ax.grid(show_grid)
        ax.axis('on' if show_axis else 'off')
        ax.set_title('交互控制选项' if show_title else '')
        ax.legend([] if show_legend else None)
        
        st.pyplot(fig)