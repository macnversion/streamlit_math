"""
长方体的3D可视化页面
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from src.utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib并获取中文字体
chinese_font = configure_matplotlib_defaults()

def create_cuboid_vertices(length=1, width=1, height=1):
    """创建长方体的顶点坐标"""
    vertices = np.array([
        [0, 0, 0],  # 0: 左下后
        [length, 0, 0],  # 1: 右下后
        [length, width, 0],  # 2: 右上后
        [0, width, 0],  # 3: 左上后
        [0, 0, height],  # 4: 左下前
        [length, 0, height],  # 5: 右下前
        [length, width, height],  # 6: 右上前
        [0, width, height]  # 7: 左上前
    ])
    return vertices

def create_cuboid_faces():
    """创建长方体的面（按顶点索引定义）"""
    faces = [
        [0, 1, 2, 3],  # 底面
        [4, 5, 6, 7],  # 顶面
        [0, 1, 5, 4],  # 前面
        [2, 3, 7, 6],  # 后面
        [0, 3, 7, 4],  # 左面
        [1, 2, 6, 5]   # 右面
    ]
    return faces

def rotate_vertices(vertices, angles):
    """根据欧拉角旋转顶点
    angles: (x_angle, y_angle, z_angle) 分别是绕x、y、z轴的旋转角度（度）
    """
    # 将角度转换为弧度
    x_angle, y_angle, z_angle = np.radians(angles)
    
    # 创建旋转矩阵
    # 绕x轴旋转
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(x_angle), -np.sin(x_angle)],
        [0, np.sin(x_angle), np.cos(x_angle)]
    ])
    
    # 绕y轴旋转
    Ry = np.array([
        [np.cos(y_angle), 0, np.sin(y_angle)],
        [0, 1, 0],
        [-np.sin(y_angle), 0, np.cos(y_angle)]
    ])
    
    # 绕z轴旋转
    Rz = np.array([
        [np.cos(z_angle), -np.sin(z_angle), 0],
        [np.sin(z_angle), np.cos(z_angle), 0],
        [0, 0, 1]
    ])
    
    # 组合旋转矩阵（注意旋转顺序：先z，再y，最后x）
    R = Rx @ Ry @ Rz
    
    # 计算几何体中心
    center = np.mean(vertices, axis=0)
    
    # 将顶点移动到原点
    centered_vertices = vertices - center
    
    # 应用旋转
    rotated_vertices = np.dot(centered_vertices, R.T)
    
    # 将顶点移回原位置
    final_vertices = rotated_vertices + center
    
    return final_vertices

def plot_cuboid(fig, ax, vertices, faces, colors):
    """绘制长方体"""
    # 清除当前图形
    ax.clear()
    
    # 创建多边形集合
    cuboid = Poly3DCollection([vertices[face] for face in faces])
    
    # 设置面的颜色
    cuboid.set_facecolors(colors)
    cuboid.set_edgecolor('black')
    
    # 添加到图形中
    ax.add_collection3d(cuboid)
    
    # 设置坐标轴范围
    max_range = 2
    ax.set_xlim([-max_range/2, max_range/2])
    ax.set_ylim([-max_range/2, max_range/2])
    ax.set_zlim([-max_range/2, max_range/2])
    
    # 设置坐标轴标签
    ax.set_xlabel('X轴', fontproperties=chinese_font)
    ax.set_ylabel('Y轴', fontproperties=chinese_font)
    ax.set_zlabel('Z轴', fontproperties=chinese_font)
    
    # 设置固定视角
    ax.view_init(elev=20, azim=45)
    
    # 添加标题
    ax.set_title('可旋转的长方体', fontproperties=chinese_font)

def show_cuboid_page():
    """显示长方体页面"""
    st.title("长方体")
    
    # 创建侧边栏控件
    st.sidebar.header("长方体参数")
    length = st.sidebar.slider("长", 0.5, 2.0, 1.0, 0.1, key="geometry_cuboid_length")
    width = st.sidebar.slider("宽", 0.5, 2.0, 1.0, 0.1, key="geometry_cuboid_width")
    height = st.sidebar.slider("高", 0.5, 2.0, 1.0, 0.1, key="geometry_cuboid_height")
    
    # 创建旋转控制滑块
    st.sidebar.header("旋转控制")
    x_angle = st.sidebar.slider("绕X轴旋转", -180, 180, 0, 5, key="geometry_cuboid_rotate_x")
    y_angle = st.sidebar.slider("绕Y轴旋转", -180, 180, 0, 5, key="geometry_cuboid_rotate_y")
    z_angle = st.sidebar.slider("绕Z轴旋转", -180, 180, 0, 5, key="geometry_cuboid_rotate_z")
    
    # 创建图形
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # 创建长方体的顶点和面
    vertices = create_cuboid_vertices(length, width, height)
    faces = create_cuboid_faces()
    
    # 应用旋转
    rotated_vertices = rotate_vertices(vertices, (x_angle, y_angle, z_angle))
    
    # 定义每个面的颜色
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#99CCFF']
    
    # 绘制长方体
    plot_cuboid(fig, ax, rotated_vertices, faces, colors)
    
    # 显示图形
    st.pyplot(fig)
    
    # 添加说明
    st.markdown("""
    ### 长方体的特征
    1. 6个面都是长方形
    2. 相对的面平行且相等
    3. 相邻的面互相垂直
    4. 有12条边，8个顶点
    
    ### 体积计算
    长方体的体积 = 长 × 宽 × 高
    
    当前长方体的体积：{:.2f} 立方单位
    """.format(length * width * height))
    
    # 显示当前参数
    st.sidebar.markdown("""
    ### 当前参数
    - 长：{:.1f}
    - 宽：{:.1f}
    - 高：{:.1f}
    - X轴旋转：{}°
    - Y轴旋转：{}°
    - Z轴旋转：{}°
    """.format(length, width, height, x_angle, y_angle, z_angle))
