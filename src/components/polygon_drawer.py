import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from ..utils.visualization import create_figure, setup_coordinate_system
from ..utils.math_utils import calculate_regular_polygon_points
from ..utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib
configure_matplotlib_defaults()

def calculate_axis_limits(points, radius, margin_factor=1.5):
    """计算坐标轴的合适范围
    
    Args:
        points: 多边形顶点坐标
        radius: 多边形半径
        margin_factor: 边距系数，控制图形周围的空白区域
        
    Returns:
        tuple: (xlim, ylim) 坐标轴范围
    """
    # 计算顶点的最大绝对值坐标
    max_coord = max(abs(points).max(), radius) * margin_factor
    return (-max_coord, max_coord), (-max_coord, max_coord)

def draw_polygon_component():
    """多边形绘制组件"""
    st.subheader("正多边形绘制器")
    
    col1, col2 = st.columns(2)
    
    with col1:
        n_sides = st.slider("边数", min_value=3, max_value=20, value=5)
        radius = st.slider("半径", min_value=1.0, max_value=10.0, value=3.0)
    
    with col2:
        show_vertices = st.checkbox("显示顶点", value=True)
        show_center = st.checkbox("显示中心", value=True)
        margin = st.slider("图形边距", min_value=1.1, max_value=2.0, value=1.5, 
                         help="控制图形周围的空白区域大小")
    
    # 创建一个居中的容器
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:  # 使用中间的列来显示图形
        fig, ax = create_figure(figsize=(4, 4))  # 使用较小的图形尺寸
        
        # 计算并绘制多边形
        points = calculate_regular_polygon_points(n_sides, radius)
        
        # 根据多边形大小动态设置坐标系范围
        xlim, ylim = calculate_axis_limits(points, radius, margin)
        setup_coordinate_system(ax, xlim=xlim, ylim=ylim)
        
        polygon = plt.Polygon(points, fill=False)
        ax.add_patch(polygon)
        
        if show_vertices:
            ax.plot(points[:, 0], points[:, 1], 'ro')
            # 添加顶点标签
            for i, (x, y) in enumerate(points):
                # 根据坐标系范围调整标签位置
                label_offset = radius * 0.1
                ax.text(x + label_offset, y + label_offset, f'V{i+1}')
        
        if show_center:
            ax.plot(0, 0, 'ko')
            # 根据坐标系范围调整标签位置
            center_offset = radius * 0.1
            ax.text(center_offset, center_offset, 'O')
        
        st.pyplot(fig)
