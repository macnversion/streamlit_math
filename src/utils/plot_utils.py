import matplotlib.pyplot as plt

def configure_matplotlib_defaults():
    """配置matplotlib的默认设置，主要用于支持中文显示和统一样式"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macOS 系统预装的支持中文的字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    
    # 设置图形样式
    plt.style.use('seaborn')  # 使用seaborn样式，让图形更美观
    
    # 设置默认图形大小
    plt.rcParams['figure.figsize'] = [10, 6]
    
    # 设置默认DPI（分辨率）
    plt.rcParams['figure.dpi'] = 100
    
    # 设置标题和标签的字体大小
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    
    # 设置图例字体大小
    plt.rcParams['legend.fontsize'] = 10
    
    # 设置刻度标签字体大小
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
