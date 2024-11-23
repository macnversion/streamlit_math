import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.utils.plot_utils import configure_matplotlib_defaults

# 配置matplotlib并获取中文字体
chinese_font = configure_matplotlib_defaults()

def draw_triangle(ax, points, title="", color='blue', alpha=0.3, show_angles=False):
    """绘制三角形"""
    # 添加第一个点作为结束点，形成闭合图形
    points = np.vstack((points, points[0]))
    ax.plot(points[:, 0], points[:, 1], color=color)
    ax.fill(points[:, 0], points[:, 1], alpha=alpha, color=color)
    
    if show_angles:
        # 计算并显示角度
        for i in range(3):
            p1 = points[i]
            p2 = points[(i+1)%3]
            p3 = points[(i+2)%3]
            
            # 计算向量
            v1 = p2 - p1
            v2 = p3 - p1
            
            # 计算角度
            angle = np.degrees(np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))
            
            # 在角的位置显示角度
            midpoint = p1 + 0.2 * (v1 + v2) / 2
            ax.text(midpoint[0], midpoint[1], f'{angle:.0f}°', fontsize=8)
    
    ax.set_title(title, fontproperties=chinese_font)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.axis('on')

def draw_basic_triangles():
    """绘制基本三角形示例"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    # 普通三角形
    points1 = np.array([[0, 0], [1, 0], [0.5, 1]])
    draw_triangle(axes[0], points1, "普通三角形", show_angles=True)
    
    # 直角三角形
    points2 = np.array([[0, 0], [1, 0], [0, 1]])
    draw_triangle(axes[1], points2, "直角三角形", show_angles=True)
    
    # 等腰三角形
    points3 = np.array([[-0.5, 0], [0.5, 0], [0, 1]])
    draw_triangle(axes[2], points3, "等腰三角形", show_angles=True)
    
    plt.tight_layout()
    return fig

def draw_special_triangles():
    """绘制特殊三角形"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    # 等边三角形
    side = 1
    height = side * np.sqrt(3) / 2
    points1 = np.array([[0, 0], [1, 0], [0.5, height]])
    draw_triangle(axes[0], points1, "等边三角形", show_angles=True)
    
    # 30-60-90三角形
    points2 = np.array([[0, 0], [2, 0], [0, np.sqrt(3)]])
    draw_triangle(axes[1], points2, "30-60-90三角形", show_angles=True)
    
    # 45-45-90三角形
    points3 = np.array([[0, 0], [1, 0], [0, 1]])
    draw_triangle(axes[2], points3, "45-45-90三角形", show_angles=True)
    
    plt.tight_layout()
    return fig

def show_triangles_page():
    """显示三角形页面"""
    st.title("三角形 ")
    
    # 创建选项卡
    tab1, tab2, tab3, tab4 = st.tabs([
        "三角形基础",
        "特殊三角形",
        "三角形性质",
        "三角形计算"
    ])
    
    # Tab 1: 三角形基础
    with tab1:
        st.markdown("""
        ## 什么是三角形？
        
        三角形是由三条线段首尾相连构成的封闭图形。它是最基本的多边形，也是几何学中最重要的图形之一。
        
        ### 三角形的基本要素
        1. **三个顶点**：通常用大写字母A、B、C表示
        2. **三条边**：通常用小写字母a、b、c表示，分别对应对面的顶点
        3. **三个角**：通常用∠A、∠B、∠C表示，表示顶点处的角
        
        ### 三角形的分类
        
        按照边的关系分类：
        - **等边三角形**：三条边相等
        - **等腰三角形**：两条边相等
        - **不等边三角形**：三条边都不相等
        
        按照角的关系分类：
        - **锐角三角形**：三个角都是锐角（小于90°）
        - **直角三角形**：有一个角是直角（90°）
        - **钝角三角形**：有一个角是钝角（大于90°）
        """)
        
        st.pyplot(draw_basic_triangles())
    
    # Tab 2: 特殊三角形
    with tab2:
        st.markdown("""
        ## 特殊三角形
        
        ### 1. 等边三角形
        - 三条边相等
        - 三个角都是60°
        - 具有最高的对称性
        
        ### 2. 30-60-90三角形
        - 是直角三角形
        - 三个角分别是30°、60°、90°
        - 边的比例是1:√3:2
        
        ### 3. 45-45-90三角形
        - 是等腰直角三角形
        - 两个锐角都是45°
        - 两个直角边相等，斜边是直角边的√2倍
        """)
        
        st.pyplot(draw_special_triangles())
    
    # Tab 3: 三角形性质
    with tab3:
        st.markdown("""
        ## 三角形的重要性质
        
        ### 1. 内角和定理
        - 三角形的内角和为180°
        - 任意一个角都可以用其他两个角来确定
        
        ### 2. 三角不等式
        - 任意两边之和大于第三边
        - 任意两边之差小于第三边
        
        ### 3. 三角形的中线性质
        - 中线：顶点到对边中点的线段
        - 三条中线交于一点（重心）
        - 重心到顶点的距离是到对边中点距离的2倍
        
        ### 4. 三角形的高线性质
        - 高：顶点到对边（或其延长线）的垂线
        - 三条高线交于一点（垂心）
        
        ### 5. 三角形的角平分线性质
        - 角平分线：平分一个角的射线
        - 三条角平分线交于一点（内心）
        - 内心到三边的距离相等
        """)
        
        # 添加图片
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Triangle.Centroid.svg/330px-Triangle.Centroid.svg.png",
                 caption="三角形的重心")
    
    # Tab 4: 三角形计算
    with tab4:
        st.markdown("""
        ## 三角形的计算
        
        ### 面积计算公式
        1. **基本公式**：S = ah/2（底×高÷2）
        2. **海伦公式**：S = √(p(p-a)(p-b)(p-c))，其中p=(a+b+c)/2
        3. **正弦公式**：S = ab·sinC/2
        
        ### 三角形的周长
        - 周长 = a + b + c
        
        ### 特殊三角形的计算
        1. **等边三角形**
           - 边长为a时，面积 = a²√3/4
           - 高 = a√3/2
        
        2. **30-60-90三角形**
           - 最短边:中等边:最长边 = 1:√3:2
        
        3. **45-45-90三角形**
           - 两直角边相等
           - 斜边 = 直角边×√2
        """)
        
        # 添加三角形计算器
        st.subheader("三角形计算器")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 输入三角形的三边长")
            a = st.number_input("边a", min_value=0.1, value=3.0, step=0.1, key="geometry_triangles_calc_side_a")
            b = st.number_input("边b", min_value=0.1, value=4.0, step=0.1, key="geometry_triangles_calc_side_b")
            c = st.number_input("边c", min_value=0.1, value=5.0, step=0.1, key="geometry_triangles_calc_side_c")
        
        with col2:
            # 检查三角形是否合法
            if a + b > c and b + c > a and a + c > b:
                # 计算周长
                perimeter = a + b + c
                
                # 计算半周长
                s = perimeter / 2
                
                # 使用海伦公式计算面积
                area = np.sqrt(s * (s - a) * (s - b) * (s - c))
                
                st.metric("周长", f"{perimeter:.2f}")
                st.metric("面积", f"{area:.2f}")
            else:
                st.error("这不是一个有效的三角形！（任意两边之和必须大于第三边）")

show_triangles_page()
