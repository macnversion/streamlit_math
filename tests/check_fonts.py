"""
检查系统中可用的字体
"""
import matplotlib.font_manager as fm

def list_available_fonts():
    """列出系统中所有可用的字体"""
    fonts = sorted([f.name for f in fm.fontManager.ttflist])
    print("\n可用字体列表:")
    print("-" * 40)
    for font in fonts:
        print(font)
    print("-" * 40)
    print(f"总计: {len(fonts)} 个字体")

def find_chinese_fonts():
    """查找可能的中文字体"""
    chinese_fonts = []
    keywords = ['Chinese', 'CN', 'GB', 'Ming', 'Kai', 'Hei', 'Song', 
                '中', '华', '宋', '楷', '黑', '苹方', 'PingFang', 'STHeiti']
    
    for f in fm.fontManager.ttflist:
        for keyword in keywords:
            if keyword in f.name or keyword in f.fname:
                chinese_fonts.append((f.name, f.fname))
                break
    
    print("\n可能的中文字体:")
    print("-" * 80)
    for name, path in sorted(chinese_fonts):
        print(f"名称: {name}")
        print(f"路径: {path}")
        print("-" * 80)
    print(f"总计: {len(chinese_fonts)} 个中文字体")

if __name__ == '__main__':
    print("=== 字体检查工具 ===")
    while True:
        print("\n1. 列出所有可用字体")
        print("2. 查找中文字体")
        print("3. 退出")
        choice = input("\n请选择操作 (1-3): ")
        
        if choice == '1':
            list_available_fonts()
        elif choice == '2':
            find_chinese_fonts()
        elif choice == '3':
            break
        else:
            print("无效的选择，请重试")
