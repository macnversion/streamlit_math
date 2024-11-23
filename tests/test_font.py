"""
测试matplotlib中文字体渲染
"""
import matplotlib.pyplot as plt
from src.utils.plot_utils import configure_matplotlib_defaults

def test_chinese_font():
    """测试中文字体渲染"""
    # 配置matplotlib并获取中文字体
    chinese_font = configure_matplotlib_defaults()
    
    # 创建测试图
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 添加中文文本
    ax.set_title('中文字体测试', fontproperties=chinese_font)
    ax.set_xlabel('X轴标签', fontproperties=chinese_font)
    ax.set_ylabel('Y轴标签', fontproperties=chinese_font)
    
    # 添加一些数据点和标签
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 5, 3]
    ax.plot(x, y, 'o-', label='测试数据')
    ax.legend(prop=chinese_font)
    
    # 保存测试图
    plt.savefig('tests/test_font.png')
    print("图片已保存为 tests/test_font.png")

if __name__ == '__main__':
    test_chinese_font()
