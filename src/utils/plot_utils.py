import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os

def get_chinese_font():
    """获取系统中可用的中文字体"""
    if platform.system() == 'Darwin':  # macOS
        # 尝试常见的中文字体路径
        font_paths = [
            '/System/Library/Fonts/STHeiti Medium.ttc',
            '/System/Library/Fonts/STHeiti Light.ttc',
            '/System/Library/Fonts/PingFang.ttc',
            '/Library/Fonts/Arial Unicode.ttf'
        ]
        
        for path in font_paths:
            if os.path.exists(path):
                return fm.FontProperties(fname=path)
    
    # 如果找不到指定字体，返回系统默认字体
    return fm.FontProperties()

def configure_matplotlib_defaults():
    """配置matplotlib的默认设置，主要用于支持中文显示和统一样式"""
    # 获取中文字体
    chinese_font = get_chinese_font()
    
    # 设置全局字体
    plt.rcParams['font.family'] = chinese_font.get_name()
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    
    # 设置图形样式
    plt.style.use('default')  # 使用默认样式
    
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
    
    return chinese_font  # 返回字体对象，以便在需要时使用
