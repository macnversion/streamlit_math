# src/utils/page_config.py

from enum import Enum
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class PageInfo:
    """页面信息类"""
    display_name: str          # 显示名称（中文）
    file_path: str            # 文件路径
    handler: Optional[str]     # 处理函数名
    description: str          # 页面描述

class PageID(Enum):
    """页面ID枚举"""
    HOME = "home"
    GEOMETRY_POLYGON = "geometry_polygon"
    GEOMETRY_CIRCLE = "geometry_circle"
    GEOMETRY_ANGLE = "geometry_angle"
    GEOMETRY_TRIANGLE = "geometry_triangle"
    GEOMETRY_CUBOID = "geometry_cuboid"
    GEOMETRY_FRACTALS = "geometry_fractals"
    ALGEBRA = "algebra"
    ARITHMETIC = "arithmetic"

# 页面配置字典
PAGES = {
    PageID.HOME: PageInfo(
        display_name="首页",
        file_path="pages.home",
        handler="show_home_page",
        description="数学知识库首页"
    ),
    PageID.GEOMETRY_POLYGON: PageInfo(
        display_name="几何/多边形",
        file_path="pages.geometry.polygons",
        handler="show_polygons_page",
        description="多边形的性质与构造"
    ),
    PageID.GEOMETRY_CIRCLE: PageInfo(
        display_name="几何/圆",
        file_path="pages.geometry.circles",
        handler="show_circles_page",
        description="圆的性质与应用"
    ),
    PageID.GEOMETRY_ANGLE: PageInfo(
        display_name="几何/角",
        file_path="pages.geometry.angles",
        handler="show_angles_page",
        description="认识角的概念与度量"
    ),
    PageID.GEOMETRY_TRIANGLE: PageInfo(
        display_name="几何/三角形",
        file_path="pages.geometry.triangles",
        handler="show_triangles_page",
        description="三角形的性质与构造"
    ),
    PageID.GEOMETRY_CUBOID: PageInfo(
        display_name="几何/长方体",
        file_path="pages.geometry.cuboid",
        handler="show_cuboid_page",
        description="长方体的三维可视化"
    ),
    PageID.GEOMETRY_FRACTALS: PageInfo(
        display_name="几何/分形",
        file_path="pages.geometry.fractals",
        handler="show_fractals_page",
        description="分形图形的生成与性质"
    ),
    # ... 其他页面配置
}

def get_page_handler(page_id: PageID) -> Callable:
    """获取页面处理函数"""
    page_info = PAGES[page_id]
    module = __import__(f"src.{page_info.file_path}", fromlist=[page_info.handler])
    return getattr(module, page_info.handler)

def get_page_id_by_display_name(display_name: str) -> Optional[PageID]:
    """通过显示名称获取页面ID"""
    for page_id, info in PAGES.items():
        if info.display_name == display_name:
            return page_id
    return None

def get_all_display_names() -> list[str]:
    """获取所有页面的显示名称"""
    return [info.display_name for info in PAGES.values()]