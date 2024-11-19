import streamlit as st
import matplotlib.pyplot as plt

def set_page_config():
    """设置 Streamlit 页面配置"""
    st.set_page_config(
        page_title="初等数学知识库",
        page_icon="📐",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def setup_matplotlib_defaults():
    """设置 Matplotlib 的默认样式"""
    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = [10, 6]
    plt.rcParams['axes.grid'] = True
    plt.rcParams['font.size'] = 12

def create_figure(figsize=(4, 4)):
    """创建一个新的图形对象
    
    Args:
        figsize: 图形大小，默认为 (4, 4)
        
    Returns:
        tuple: (fig, ax) Matplotlib图形对象和坐标轴对象
    """
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax

def setup_coordinate_system(ax, xlim=(-6, 10), ylim=(-6, 10)):
    """设置坐标系"""
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(True)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)