# page1.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def draw_polygon():
    # 用户输入边数
    n = st.slider('Select the number of sides (n):', min_value=3, max_value=20, value=5)

    # 计算正n边形的顶点
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)

    # 创建图形和轴
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.fill(x, y, alpha=0.5, edgecolor='black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Regular {n}-gon')
    ax.set_aspect('equal')
    ax.grid()
    ax.axis('off')

    # 绘制内切圆和外接圆的选项
    draw_incircle = st.checkbox('Draw Incircle')
    draw_circumcircle = st.checkbox('Draw Circumcircle')

    # Correct calculation of the incircle radius
    incircle_radius = np.cos(np.pi / n)  # 内切圆半径
    circumcircle_radius = 1  # 外接圆半径

    # 绘制内切圆
    if draw_incircle:
        incircle = plt.Circle((0, 0), incircle_radius, color='blue', fill=False, linestyle='--')
        ax.add_artist(incircle)

    # 绘制外接圆
    if draw_circumcircle:
        circumcircle = plt.Circle((0, 0), circumcircle_radius, color='red', fill=False, linestyle='--')
        ax.add_artist(circumcircle)

    # 显示图形
    st.pyplot(fig)

# Streamlit 页面
st.title('Draw a Regular n-gon')
draw_polygon()
