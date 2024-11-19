import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib
configure_matplotlib_defaults()

def draw_triangle(ax, points, title="", color='blue', alpha=0.3):
    """绘制三角形"""
    # 添加第一个点作为结束点，形成闭合图形
    points = np.vstack((points, points[0]))
    ax.plot(points[:, 0], points[:, 1], color=color)
    ax.fill(points[:, 0], points[:, 1], alpha=alpha, color=color)
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_basic_triangles():
    """绘制基本三角形示例"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    # 普通三角形
    points1 = np.array([[0, 0], [1, 0], [0.5, 1]])
    draw_triangle(axes[0], points1, "普通三角形")
    
    # 直角三角形
    points2 = np.array([[0, 0], [1, 0], [0, 1]])
    draw_triangle(axes[1], points2, "直角三角形")
    
    # 等腰三角形
    points3 = np.array([[-0.5, 0], [0.5, 0], [0, 1]])
    draw_triangle(axes[2], points3, "等腰三角形")
    
    plt.tight_layout()
    return fig

def draw_isosceles_triangles(angle_deg):
    """绘制不同方向的等腰三角形"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    # 计算等腰三角形的点
    angle_rad = np.radians(angle_deg)
    height = 1
    base = 2 * height * np.tan(angle_rad / 2)
    
    # 顶点在上的等腰三角形
    points1 = np.array([[-base/2, 0], [base/2, 0], [0, height]])
    draw_triangle(axes[0], points1, f"顶角 {angle_deg}°")
    
    # 顶点在左的等腰三角形
    points2 = np.array([[0, -base/2], [0, base/2], [-height, 0]])
    draw_triangle(axes[1], points2, f"顶角 {angle_deg}°")
    
    # 顶点在右的等腰三角形
    points3 = np.array([[0, -base/2], [0, base/2], [height, 0]])
    draw_triangle(axes[2], points3, f"顶角 {angle_deg}°")
    
    plt.tight_layout()
    return fig

def show_triangles_page():
    """显示三角形页面"""
    st.title("三角形")
    
    st.subheader("1. 基本三角形类型")
    st.pyplot(draw_basic_triangles())
    
    st.subheader("2. 等腰三角形的变化")
    angle = st.slider("调整顶角大小", min_value=30, max_value=150, value=60, step=1)
    st.pyplot(draw_isosceles_triangles(angle))
