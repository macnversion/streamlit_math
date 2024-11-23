"""
分形图形的可视化页面
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib并获取中文字体
chinese_font = configure_matplotlib_defaults()

def koch_snowflake(order, size=1):
    """生成科赫雪花的顶点
    
    Args:
        order: 递归深度
        size: 初始三角形的大小
    
    Returns:
        vertices: 所有线段的顶点坐标
    """
    def koch_curve(start, end, order):
        if order == 0:
            return [start, end]
        
        # 计算三等分点
        vec = end - start
        p1 = start + vec / 3
        p2 = start + 2 * vec / 3
        
        # 计算顶点
        # 使用复数进行旋转计算
        zv = complex(vec[0], vec[1])
        rot = zv * (0.5 + 0.8660254037844386j)  # exp(i*pi/3)
        p_top = p1 + np.array([rot.real, rot.imag]) / 3
        
        # 递归生成每个部分
        points = []
        points.extend(koch_curve(start, p1, order-1))
        points.extend(koch_curve(p1, p_top, order-1))
        points.extend(koch_curve(p_top, p2, order-1))
        points.extend(koch_curve(p2, end, order-1))
        
        return points
    
    # 创建初始等边三角形的顶点
    height = size * np.sqrt(3) / 2
    vertices = np.array([
        [-size/2, -height/3],
        [size/2, -height/3],
        [0, height*2/3]
    ])
    
    # 生成三条边的科赫曲线
    points = []
    for i in range(3):
        start = vertices[i]
        end = vertices[(i+1)%3]
        points.extend(koch_curve(start, end, order))
    
    return np.array(points)

def sierpinski_triangle(order, size=1):
    """生成谢尔宾斯基三角形的顶点
    
    Args:
        order: 递归深度
        size: 初始三角形的大小
    
    Returns:
        triangles: 所有三角形的顶点坐标
    """
    def create_triangles(vertices, order):
        if order == 0:
            return [vertices]
        
        # 计算三角形的中点
        mid_points = [
            (vertices[0] + vertices[1]) / 2,
            (vertices[1] + vertices[2]) / 2,
            (vertices[2] + vertices[0]) / 2
        ]
        
        # 递归生成三个新的三角形
        triangles = []
        triangles.extend(create_triangles([vertices[0], mid_points[0], mid_points[2]], order-1))
        triangles.extend(create_triangles([mid_points[0], vertices[1], mid_points[1]], order-1))
        triangles.extend(create_triangles([mid_points[2], mid_points[1], vertices[2]], order-1))
        
        return triangles
    
    # 创建初始等边三角形的顶点
    height = size * np.sqrt(3) / 2
    initial_vertices = np.array([
        [-size/2, -height/3],
        [size/2, -height/3],
        [0, height*2/3]
    ])
    
    return create_triangles(initial_vertices, order)

def plot_koch_snowflake(ax, points):
    """绘制科赫雪花"""
    ax.plot(points[:, 0], points[:, 1], 'b-', linewidth=1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('科赫雪花', fontproperties=chinese_font)

def plot_sierpinski_triangle(ax, triangles):
    """绘制谢尔宾斯基三角形"""
    for triangle in triangles:
        # 闭合三角形
        tri = np.vstack([triangle, triangle[0]])
        ax.plot(tri[:, 0], tri[:, 1], 'b-', linewidth=1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('谢尔宾斯基三角形', fontproperties=chinese_font)

def show_fractals_page():
    """显示分形图形页面"""
    st.title("分形图形")
    
    # 添加分形简介
    st.markdown("""
    ### 什么是分形？
    分形是一种具有自相似性的图形，即局部和整体具有相似的形状。在数学中，分形通常具有以下特征：
    1. 自相似性：图形的局部和整体形状相似
    2. 无限细节：无论放大多少倍，都能看到类似的结构
    3. 分数维：不同于普通的整数维度
    
    下面展示了两个经典的分形图形：科赫雪花和谢尔宾斯基三角形。
    """)
    
    # 创建分形控制
    st.sidebar.header("分形参数")
    fractal_type = st.sidebar.selectbox(
        "选择分形类型",
        ["科赫雪花", "谢尔宾斯基三角形"],
        key="geometry_fractals_type"
    )
    
    order = st.sidebar.slider("递归深度", 0, 6, 3, key="geometry_fractals_order")
    size = st.sidebar.slider("图形大小", 0.5, 2.0, 1.0, 0.1, key="geometry_fractals_size")
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 10))
    
    if fractal_type == "科赫雪花":
        points = koch_snowflake(order, size)
        plot_koch_snowflake(ax, points)
        
        # 添加科赫雪花的说明
        st.markdown("""
        ### 科赫雪花
        科赫雪花是由瑞典数学家赫尔格·冯·科赫在1904年首次描述的一种分形图形。它的构造过程如下：
        1. 从一个等边三角形开始
        2. 将每条边三等分
        3. 在中间三分之一的位置向外突出一个等边三角形
        4. 对所有新的边重复步骤2-3
        
        特点：
        - 具有无限的周长
        - 有限的面积
        - 处处连续但处处不可导
        - 分形维度约为1.262
        """)
        
    else:
        triangles = sierpinski_triangle(order, size)
        plot_sierpinski_triangle(ax, triangles)
        
        # 添加谢尔宾斯基三角形的说明
        st.markdown("""
        ### 谢尔宾斯基三角形
        谢尔宾斯基三角形是由波兰数学家瓦茨瓦夫·谢尔宾斯基在1915年提出的分形图形。它的构造过程如下：
        1. 从一个实心等边三角形开始
        2. 将三角形分成四个相等的小三角形
        3. 移除中间的小三角形
        4. 对剩下的三个小三角形重复步骤2-3
        
        特点：
        - 自相似性明显
        - 面积趋近于0
        - 分形维度约为1.585
        - 在计算机图形学中应用广泛
        """)
    
    # 显示图形
    st.pyplot(fig)
    
    # 添加交互说明
    st.sidebar.markdown("""
    ### 参数说明
    - 递归深度：决定分形的精细程度
    - 图形大小：调整整体图形的大小
    
    提示：递归深度越大，图形越精细，但计算量也越大。
    """)
    
    # 添加数学原理
    st.markdown("""
    ### 分形的数学原理
    分形图形通常可以通过以下方式定义：
    1. 递归方程：通过重复应用某种变换
    2. 迭代函数系统（IFS）：多个收缩变换的组合
    3. 复动力系统：在复平面上迭代特定函数
    
    分形在自然界中普遍存在，例如：
    - 云朵的形状
    - 山脉的轮廓
    - 树木的分支结构
    - 海岸线的形状
    """)
