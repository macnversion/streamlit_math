import streamlit as st
from ...components.angle_drawer import draw_angle_component, draw_special_angles_component

def show_angles_page():
    """角度页面"""
    st.title("认识角")
    
    # 基础介绍
    st.markdown("""
    角是几何中的基本概念之一。它由一个定点（称为角的顶点）和从该点出发的两条射线（称为角的边）所组成。
    
    在这个页面中，你可以：
    1. 通过交互式工具探索不同大小的角
    2. 认识一些常见的特殊角
    3. 了解角度的基本概念和性质
    """)
    
    # 添加角度绘制组件
    draw_angle_component()
    
    st.markdown("---")
    
    # 添加特殊角度组件
    draw_special_angles_component()
    
    st.markdown("---")
    
    # 奥数知识点
    st.subheader("奥数知识点")
    
    # 1. 角的运算
    st.markdown("""
    ### 1. 角的运算
    #### 互补角
    - 两个角的和等于90°，这两个角互为补角
    - 例如：30° 和 60°、45° 和 45°
    - 重要性质：直角三角形中，两个锐角互为补角
    
    #### 互余角
    - 两个角的和等于180°，这两个角互为余角
    - 例如：30° 和 150°、45° 和 135°
    - 重要性质：三角形内角和为180°
    
    ### 2. 角的度量方法
    #### 估测角度
    - 利用特殊角（30°、45°、60°、90°）来估计角的大小
    - 技巧：把手掌摊开，大拇指和食指张开约60°
    
    ### 3. 旋转角
    - 顺时针旋转：角度为负
    - 逆时针旋转：角度为正
    - 一周角等于360°
    - 重要应用：时钟的指针角（每小时30°，每分钟6°）
    
    ### 4. 常见奥数题型
    #### 角平分线
    - 角平分线将角分成相等的两部分
    - 角平分线上的点到角的两边距离相等
    
    #### 垂直与平行
    - 两条直线垂直：它们相交成90°
    - 两条平行线被第三条线相交：产生相等的角
        - 同位角相等
        - 内错角相等
        - 同旁内角互补（和为180°）
    
    ### 5. 解题技巧
    1. **补角法**：找到互补的角（和为90°）
    2. **余角法**：找到互余的角（和为180°）
    3. **等角法**：
       - 垂直线段之间的角相等
       - 平行线对应的角相等
    4. **倍角法**：
       - 找到成倍数关系的角
       - 常见于圆周角和圆心角的关系（圆心角是圆周角的2倍）
    
    ### 6. 趣味知识
    1. **生活中的角度**
        - 楼梯的倾角通常是30°左右
        - 自行车车把的转角通常不超过45°
        - 彩虹的角度总是42°
    
    2. **历史小知识**
        - 古埃及人用绳结测量直角
        - 古希腊人发现了黄金角（约137.5°）
    """)
    
    # 练习题示例
    st.markdown("""
    ### 练习题示例
    
    1. **基础题**：一个角的度数是它的补角的两倍，求这个角的度数。
    
    2. **思考题**：时钟的时针和分针在什么时候会形成90度角？
    
    3. **挑战题**：一个三角形的三个内角比是2:3:4，求这个三角形的三个内角的度数。
    
    <details>
    <summary>点击查看答案提示</summary>
    
    1. 基础题提示：设这个角为x°，则其补角为(90-x)°，根据题意可列方程：x = 2(90-x)
    
    2. 思考题提示：
       - 时针每小时转30°
       - 分针每小时转360°
       - 列出时针和分针之间角度的方程
    
    3. 挑战题提示：
       - 三角形内角和为180°
       - 设最小的角为x°，则其他角为1.5x°和2x°
       - 三个角的和为180°
    </details>
    """)