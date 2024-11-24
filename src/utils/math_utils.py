import numpy as np

def calculate_regular_polygon_points(n, radius=1, center=(0, 0)):
    """计算正多边形的顶点坐标
    
    Args:
        n (int): 边数
        radius (float): 半径
        center (tuple): 中心点坐标
        
    Returns:
        numpy.ndarray: 顶点坐标数组
    """
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return np.column_stack((x, y))

def calculate_circle_intersection(circle1, circle2):
    """计算两个圆的交点
    
    Args:
        circle1 (tuple): (center_x, center_y, radius)
        circle2 (tuple): (center_x, center_y, radius)
        
    Returns:
        tuple: 交点坐标，如果没有交点则返回None
    """
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    
    d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if d > r1 + r2 or d < abs(r1-r2):
        return None
    
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = np.sqrt(r1**2 - a**2)
    
    x3 = x1 + a*(x2-x1)/d
    y3 = y1 + a*(y2-y1)/d
    
    x4 = x3 + h*(y2-y1)/d
    y4 = y3 - h*(x2-x1)/d
    
    x5 = x3 - h*(y2-y1)/d
    y5 = y3 + h*(x2-x1)/d
    
    return ((x4, y4), (x5, y5))

def calculate_polygon_properties(n, radius=1, inscribed=True):
    """计算正n边形的属性
    
    Args:
        n (int): 边数
        radius (float): 圆的半径
        inscribed (bool): True为内接，False为外切
        
    Returns:
        tuple: (vertices, perimeter, diagonal)
        vertices: 顶点坐标数组
        perimeter: 周长
        diagonal: 对角线长度（直径）
    """
    if inscribed:
        # 内接正n边形
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        vertices_x = radius * np.cos(angles)
        vertices_y = radius * np.sin(angles)
        
        # 一条边的长度
        side_length = 2 * radius * np.sin(np.pi/n)
        # 周长
        perimeter = n * side_length
        # 对角线长度（直径）
        diagonal = 2 * radius
        
    else:
        # 外切正n边形
        # 外切圆的半径需要调整，使得内切圆半径为指定值
        adjusted_radius = radius / np.cos(np.pi/n)
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        vertices_x = adjusted_radius * np.cos(angles)
        vertices_y = adjusted_radius * np.sin(angles)
        
        # 一条边的长度
        side_length = 2 * adjusted_radius * np.sin(np.pi/n)
        # 周长
        perimeter = n * side_length
        # 对角线长度（直径）
        diagonal = 2 * adjusted_radius
    
    vertices = np.column_stack((vertices_x, vertices_y))
    return vertices, perimeter, diagonal