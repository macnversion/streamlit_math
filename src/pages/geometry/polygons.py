import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from ...components.polygon_drawer import draw_polygon_component

def plot_regular_polygon(n, size=1):
    """绘制正n边形"""
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = size * np.cos(angles)
    y = size * np.sin(angles)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), 'b-')
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f'正{n}边形')
    plt.close()
    return fig

def show_polygons_page():
    """显示多边形页面"""
    st.title("多边形探索 🔷")
    
    # 创建选项卡
    tab1, tab2, tab3, tab4 = st.tabs([
        "多边形基础",
        "正多边形",
        "多边形性质",
        "趣味知识"
    ])
    
    # Tab 1: 多边形基础
    with tab1:
        st.markdown("""
        ## 什么是多边形？
        
        多边形是由**有限个线段**首尾相连构成的**封闭**平面图形。这些线段称为多边形的**边**，线段的端点称为多边形的**顶点**。
        
        ### 多边形的基本要素
        1. **顶点**：多边形的角的位置
        2. **边**：连接顶点的线段
        3. **内角**：多边形内部的角
        4. **外角**：边的延长线与相邻边形成的角
        
        ### 多边形的分类
        
        根据边的数量：
        - 三角形（3边）
        - 四边形（4边）
        - 五边形（5边）
        - 六边形（6边）
        - ...
        
        根据形状特征：
        - **凸多边形**：任意两个顶点的连线都在多边形内部
        - **凹多边形**：存在两个顶点的连线不完全在多边形内部
        
        根据边和角的关系：
        - **正多边形**：所有边长相等且所有角相等
        - **不规则多边形**：边长或角度不全相等
        """)
        
        # 添加凸多边形和凹多边形的示意图
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Convex_polygon_illustration3.svg/220px-Convex_polygon_illustration3.svg.png", caption="凸多边形")
        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Concave_polygon_illustration3.svg/220px-Concave_polygon_illustration3.svg.png", caption="凹多边形")
    
    # Tab 2: 正多边形
    with tab2:
        st.markdown("""
        ## 正多边形
        
        正多边形是最美的多边形，它具有完美的对称性。
        
        ### 正多边形的性质
        1. 所有边长相等
        2. 所有内角相等
        3. 所有顶点到中心的距离（半径）相等
        4. 有相等数量的对称轴
        
        ### 正多边形的内角
        - 内角大小 = (n-2) × 180° ÷ n
        - 例如：正六边形的每个内角 = (6-2) × 180° ÷ 6 = 120°
        """)
        
        # 添加正多边形示例
        col1, col2, col3 = st.columns(3)
        with col1:
            st.pyplot(plot_regular_polygon(3))
            st.markdown("正三角形")
        with col2:
            st.pyplot(plot_regular_polygon(4))
            st.markdown("正方形")
        with col3:
            st.pyplot(plot_regular_polygon(6))
            st.markdown("正六边形")
            
        st.markdown("### 交互式正多边形绘制器")
        st.markdown("调整边数和大小，观察正多边形的变化：")
        draw_polygon_component()
    
    # Tab 3: 多边形性质
    with tab3:
        st.markdown("""
        ## 多边形的重要性质
        
        ### 1. 内角和
        n边形的内角和 = (n-2) × 180°
        
        例如：
        - 三角形：(3-2) × 180° = 180°
        - 四边形：(4-2) × 180° = 360°
        - 五边形：(5-2) × 180° = 540°
        
        ### 2. 外角和
        任何多边形的外角和都等于360°，这是一个非常神奇的性质！
        
        ### 3. 对角线的数量
        n边形的对角线数量 = n(n-3) ÷ 2
        
        例如：
        - 三角形：3(3-3) ÷ 2 = 0 条
        - 四边形：4(4-3) ÷ 2 = 2 条
        - 五边形：5(5-3) ÷ 2 = 5 条
        
        ### 4. 多边形的面积
        - **规则多边形**：面积 = 周长 × 半径 ÷ 2
        - **不规则多边形**：可以通过三角剖分法计算
        """)
        
        # 添加面积计算器
        st.markdown("### 正多边形面积计算器")
        col1, col2 = st.columns(2)
        with col1:
            sides = st.number_input("边数", min_value=3, max_value=12, value=6, key="geometry_polygons_calc_sides")
            side_length = st.number_input("边长", min_value=0.1, max_value=100.0, value=1.0, key="geometry_polygons_calc_side_length")
        with col2:
            # 计算面积
            angle = np.pi / sides
            radius = side_length / (2 * np.sin(angle))
            area = sides * side_length * radius / 2
            st.metric("面积", f"{area:.2f} 平方单位")
    
    # Tab 4: 趣味知识
    with tab4:
        st.markdown("""
        ## 多边形的趣味知识
        
        ### 1. 蜂巢的奥秘
        蜜蜂建造的蜂巢为什么是六边形的？这是因为正六边形是所有正多边形中最接近圆形，
        且能够完全铺满平面的形状，这样既节省材料又保证强度。
        
        ### 2. 高斯与17边形
        19岁的高斯证明了正17边形可以用尺规作图构造，这个发现让他决定终身献身于数学研究。
        实际上，可以用尺规作图的正多边形的边数必须是以下形式：
        - 2的幂（4, 8, 16, ...）
        - 费马素数（3, 5, 17, 257, ...）
        - 以上两种数的乘积
        
        ### 3. 自然界中的多边形
        - 雪花呈现六边形结构
        - 玄武岩柱多呈六边形
        - 石榴石晶体呈现十二面体
        - 蜂巢呈现规则六边形
        
        ### 4. 生活中的多边形
        - 交通标志：八边形（停车标志）、三角形（警告）
        - 建筑设计：五角大楼（五边形）
        - 运动场：足球（五边形和六边形的组合）
        """)
        
        # 添加一些趣味图片
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Basalt_Columns_in_Iceland.jpg/640px-Basalt_Columns_in_Iceland.jpg", 
                 caption="自然界中的六边形：玄武岩柱")