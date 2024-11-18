# gauss_17gon_detailed_streamlit.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def draw_gauss_17gon_detailed(step):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-6, 10)
    ax.set_ylim(-6, 10)

    # 原点 O
    O = np.array([0, 0])

    if step >= 1:
        # 第1步：绘制单位圆和坐标系
        circle = plt.Circle(O, 5, fill=False, color='black')
        ax.add_artist(circle)
        ax.plot([-6, 10], [0, 0], color='blue', linestyle='--')  # x 轴
        ax.plot([0, 0], [-6, 10], color='blue', linestyle='--')  # y 轴
        ax.text(5.5, 0, 'A', va='center', fontsize=12)
        ax.text(-5.5, 0, 'B', va='center', fontsize=12)
        ax.text(0, 5.5, 'C', ha='center', fontsize=12)
        ax.text(0, -5.5, 'D', ha='center', fontsize=12)
        ax.text(-0.5, -0.5, 'O', ha='right', va='top', fontsize=12)
        ax.text(10, -0.5, 'x', fontsize=12)
        ax.text(-0.5, 10, 'y', fontsize=12)

    if step >= 2:
        # 第2步：在 x 轴上构造线段 OF = 4，OG = 1
        F = np.array([4, 0])
        G = np.array([1, 0])
        ax.plot([O[0], F[0]], [O[1], F[1]], color='green')
        ax.plot([O[0], G[0]], [O[1], G[1]], color='green')
        ax.text(4.1, 0, 'F', va='center', fontsize=12)
        ax.text(1.1, 0, 'G', va='center', fontsize=12)
        ax.text(2, -0.5, '4', ha='center', fontsize=12)
        ax.text(0.5, -0.5, '1', ha='center', fontsize=12)

    if step >= 3:
        # 第3步：以 GF 为直径作半圆
        midpoint_GF = (G + F) / 2
        radius_GF = np.linalg.norm(F - G) / 2
        semicircle_GF = plt.Circle(midpoint_GF, radius_GF, fill=False, color='orange')
        ax.add_artist(semicircle_GF)
        ax.text(midpoint_GF[0], midpoint_GF[1] + radius_GF + 0.5, '半圆', ha='center', fontsize=12)

    if step >= 4:
        # 第4步：过点 O 作垂直于 GF 的垂线，交半圆于点 H
        # 垂线的方向为 (F - G) 的垂直方向
        dir_GF = F - G
        perp_dir = np.array([-dir_GF[1], dir_GF[0]])
        perp_dir = perp_dir / np.linalg.norm(perp_dir)
        # 找到点 H
        H = O + perp_dir * radius_GF
        ax.plot([O[0], H[0]], [O[1], H[1]], color='purple')
        ax.plot([O[0], O[0] + perp_dir[0]*radius_GF*1.5], [O[1], O[1] + perp_dir[1]*radius_GF*1.5], color='purple', linestyle='--')
        ax.plot(H[0], H[1], 'o', color='red')
        ax.text(H[0] + 0.2, H[1] + 0.2, 'H', fontsize=12)
        ax.text(O[0] + perp_dir[0]*radius_GF*1.5 + 0.2, O[1] + perp_dir[1]*radius_GF*1.5 + 0.2, '垂线', fontsize=12)

    if step >= 5:
        # 第5步：OH 的长度为 sqrt(17)
        ax.text(H[0]/2 - 0.5, H[1]/2, '$\sqrt{17}$', fontsize=12)

    if step >= 6:
        # 第6步：构造所需的长度，利用 OH
        # 这里需要构造复杂的长度，例如：
        # L1 = (1 + sqrt(17)) / 4
        sqrt17 = np.linalg.norm(H - O)
        L1 = (1 + sqrt17) / 4
        # 在 OF 上截取长度 OL = L1
        L = O + (F - O) * (L1 / 4)
        ax.plot([O[0], L[0]], [O[1], L[1]], color='brown')
        ax.plot(L[0], L[1], 'o', color='red')
        ax.text(L[0] + 0.2, L[1] + 0.2, 'L', fontsize=12)
        ax.text(L[0]/2, -0.5, '$L_1$', ha='center', fontsize=12)

    if step >= 7:
        # 第7步：以 O 为圆心，半径 OL，作圆弧，交单位圆于点 P
        # 作圆弧
        circle_L = plt.Circle(O, np.linalg.norm(L - O), fill=False, color='gray', linestyle='--')
        ax.add_artist(circle_L)
        # 交点 P 的坐标
        radius_L = np.linalg.norm(L - O)
        angle_P = np.arccos(radius_L / 5)
        P = np.array([5 * np.cos(angle_P), 5 * np.sin(angle_P)])
        ax.plot(P[0], P[1], 'o', color='red')
        ax.text(P[0] + 0.2, P[1] + 0.2, 'P', fontsize=12)

    if step >= 8:
        # 第8步：以 P 点为起点，依次作弧，得到正17边形的所有顶点
        angles = [angle_P + 2 * np.pi * k / 17 for k in range(17)]
        vertices = np.array([[5 * np.cos(a), 5 * np.sin(a)] for a in angles])
        # 绘制顶点
        ax.plot(vertices[:,0], vertices[:,1], 'o', color='red')
        for i, (x, y) in enumerate(vertices):
            ax.text(x + 0.2, y + 0.2, f'{i+1}', fontsize=10)
        # 连接顶点
        ax.plot(np.append(vertices[:,0], vertices[0,0]), np.append(vertices[:,1], vertices[0,1]), color='black')

    if step >= 9:
        # 第9步：完成正17边形的绘制
        ax.text(0, -6, '正17边形', ha='center', fontsize=14)

    st.pyplot(fig)

# Streamlit 应用程序
st.title('高斯尺规作图正17边形的详细步骤演示')

st.markdown("""
本应用程序逐步展示了高斯如何使用尺规作图构造正17边形。
请使用下方的滑块浏览构造过程的每个步骤。
""")

# 使用滑块控制当前步骤
step = st.slider('选择构造步骤：', min_value=1, max_value=9, value=1)

# 绘制当前步骤的图形
draw_gauss_17gon_detailed(step)

# 显示当前步骤的说明
if step == 1:
    st.subheader('第1步：绘制单位圆和坐标系')
    st.write('以点 O 为圆心，绘制单位圆，并绘制水平和垂直的坐标轴。')
elif step == 2:
    st.subheader('第2步：在 x 轴上构造线段 OF = 4，OG = 1')
    st.write('在 x 轴上，从原点 O 开始，向右标记点 G（距离为 1）和点 F（距离为 4）。')
elif step == 3:
    st.subheader('第3步：以 GF 为直径作半圆')
    st.write('以 GF 为直径，作半圆。')
elif step == 4:
    st.subheader('第4步：过点 O 作垂直于 GF 的垂线，交半圆于点 H')
    st.write('过点 O 作垂直于 GF 的垂线，交半圆于点 H。')
elif step == 5:
    st.subheader('第5步：得到长度 OH = $\sqrt{17}$')
    st.write('根据几何关系，线段 OH 的长度为 $\sqrt{17}$。')
elif step == 6:
    st.subheader('第6步：构造所需的长度 L1')
    st.write('计算并构造长度 $L_1 = \\frac{1 + \\sqrt{17}}{4}$，在 OF 上截取对应的长度。')
elif step == 7:
    st.subheader('第7步：以 O 为圆心，半径 OL，作圆弧，交单位圆于点 P')
    st.write('以 O 为圆心，半径为 $L_1$，作圆弧，交单位圆于点 P。')
elif step == 8:
    st.subheader('第8步：标记正17边形的所有顶点')
    st.write('以 P 为起点，按照每次旋转 $\\frac{360^\circ}{17}$ 的角度，标记所有顶点。')
elif step == 9:
    st.subheader('第9步：完成正17边形的绘制')
    st.write('连接所有顶点，完成正17边形的绘制。')
