"""多语言支持配置"""

TRANSLATIONS = {
    "zh": {
        # 通用
        "language": "语言",
        "chinese": "中文",
        "english": "英文",
        "start_side": "起始边",
        "end_side": "终止边",
        
        # 主页
        "home_title": "数学可视化学习",
        "home_welcome": "欢迎来到数学可视化学习平台！",
        "home_description": """
        这是一个互动式的数学学习平台，通过可视化和交互来帮助你理解数学概念。
        
        选择左侧的导航菜单来探索不同的数学主题：
        - 几何：探索角度、多边形、圆等几何概念
        - 代数：理解方程、函数和图形
        - 统计：学习数据分析和概率
        """,
        
        # 几何页面通用
        "geometry_title": "几何探索",
        "visualization": "可视化",
        "properties": "属性",
        "description": "描述",
        "interactive_controls": "交互控制",
        
        # 角度页面
        "angles_title": "认识角",
        "angles_intro": """
        角是几何中的基本概念之一。它由一个定点（称为角的顶点）和从该点出发的两条射线（称为角的边）所组成。
        
        在这个页面中，你可以：
        1. 通过交互式工具探索不同大小的角
        2. 认识一些常见的特殊角
        3. 了解角度的基本概念和性质
        """,
        
        # 多边形页面
        "polygons_title": "多边形探索 🔷",
        "polygons_intro": "多边形是由有限个线段首尾相连构成的封闭平面图形。",
        "what_is_polygon": "什么是多边形？",
        "polygon_definition": "多边形是由**有限个线段**首尾相连构成的**封闭**平面图形。这些线段称为多边形的**边**，线段的端点称为多边形的**顶点**。",
        
        "basic_elements": "基本要素",
        "vertices": "顶点",
        "vertices_description": "多边形的角的位置",
        "sides": "边",
        "sides_description": "连接顶点的线段",
        "interior_angles": "内角",
        "interior_angles_description": "多边形内部的角",
        "exterior_angles": "外角",
        "exterior_angles_description": "边的延长线与相邻边形成的角",
        
        "polygon_classification": "多边形分类",
        "by_sides": "按边的数量分类",
        "triangle": "三角形",
        "quadrilateral": "四边形",
        "pentagon": "五边形",
        "hexagon": "六边形",
        
        "by_shape": "按形状特征分类",
        "convex_polygon": "凸多边形",
        "convex_description": "任意两个顶点的连线都在多边形内部",
        "concave_polygon": "凹多边形",
        "concave_description": "存在两个顶点的连线不完全在多边形内部",
        "regular_polygon": "正多边形",
        "regular_description": "所有边长相等且所有内角相等",
        "irregular_polygon": "不规则多边形",
        "irregular_description": "边长或角度不全相等",
        
        "important_properties": "重要性质",
        "sum_of_interior_angles": "内角和",
        "interior_angles_formula": "n边形的内角和 = (n-2) × 180°",
        "sum_of_exterior_angles": "外角和",
        "exterior_angles_property": "任何多边形的外角和都等于360°，这是一个非常神奇的性质！",
        "number_of_diagonals": "对角线的数量",
        "diagonals_formula": "n边形的对角线数量 = n(n-3) ÷ 2",
        
        "examples": "例如",
        "area": "面积",
        "area_calculator": "面积计算器",
        "regular_area_formula": "面积 = 周长 × 半径 ÷ 2",
        "irregular_area_description": "可以通过三角剖分法计算",
        
        "number_of_sides": "边数",
        "side_length": "边长",
        "equal_sides": "所有边长相等",
        "angles": "角的性质",
        "equal_interior_angles": "所有内角相等",
        "equal_exterior_angles": "所有外角相等",
        "interior_angle": "每个内角",
        "exterior_angle": "每个外角",
        
        "symmetry": "对称性",
        "symmetry_axes": "对称轴数量",
        "rotational_symmetry": "旋转对称性：旋转后与原图形重合",
        
        "circle_relationships": "与圆的关系",
        "inscribed_circle": "可以内接于圆",
        "circumscribed_circle": "可以外切于圆",
        "equal_radius": "所有顶点到中心的距离相等",
        
        "fun_facts": "趣味知识",
        "bee_nest_secret": "蜂巢的奥秘",
        "bee_nest_description": "蜜蜂建造的蜂巢为什么是六边形的？这是因为正六边形是所有正多边形中最接近圆形，且能够完全铺满平面的形状，这样既节省材料又保证强度。",
        "gauss_and_17_gon": "高斯与17边形",
        "gauss_description": """19岁的高斯证明了正17边形可以用尺规作图构造，这个发现让他决定终身献身于数学研究。
        实际上，可以用尺规作图的正多边形的边数必须是以下形式：
        - 2的幂（4, 8, 16, ...）
        - 费马素数（3, 5, 17, 257, ...）
        - 以上两种数的乘积""",
        "polygons_in_nature": "自然界中的多边形",
        "polygons_in_nature_description": """
        - 雪花呈现六边形结构
        - 玄武岩柱多呈六边形
        - 石榴石晶体呈现十二面体
        - 蜂巢呈现规则六边形""",
        "polygons_in_life": "生活中的多边形",
        "polygons_in_life_description": """
        - 交通标志：八边形（停车标志）、三角形（警告）
        - 建筑设计：五角大楼（五边形）
        - 运动场：足球（五边形和六边形的组合）""",
        
        # 圆形页面
        "circles_title": "圆与圆周率",
        "circles_intro": """
        圆是平面上到定点（圆心）距离相等的所有点的集合。
        在这个页面中，你可以：
        1. 探索圆的基本性质
        2. 理解圆周率π的含义
        3. 学习圆的周长和面积计算
        """,
        "radius": "半径",
        "diameter": "直径",
        "circumference": "周长",
        "circle_area": "面积",
        "pi_approximation": "π的近似值",
        "inscribed_polygon": "内接多边形",
        "circumscribed_polygon": "外接多边形",
        
        # 分形页面
        "fractals_title": "分形几何",
        "fractals_intro": """
        分形是具有自相似性的几何图形，在任何尺度下都呈现出相似的形状。
        在这里，你可以：
        1. 探索各种分形图案
        2. 了解分形的生成规则
        3. 观察分形的自相似性
        """,
        "iteration_depth": "迭代深度",
        "fractal_type": "分形类型",
        "koch_snowflake": "科赫雪花",
        "sierpinski_triangle": "谢尔宾斯基三角形",
        "dragon_curve": "龙形曲线",
        
        # 立方体页面
        "cuboid_title": "立方体与长方体",
        "cuboid_intro": """
        立方体和长方体是最基本的立体图形。
        在这个页面中，你可以：
        1. 观察立方体的三维投影
        2. 计算体积和表面积
        3. 探索不同视角下的形状
        """,
        "length": "长",
        "width": "宽",
        "height": "高",
        "volume": "体积",
        "surface_area": "表面积",
        "rotation_angle": "旋转角度",
        
        # 角度探索器
        "angle_explorer": "角度探索器",
        "angle": "角度",
        "angle_slider_help": "拖动滑块改变角度大小（正值为逆时针，负值为顺时针）",
        "current_angle": "当前角度",
        "characteristics": "特点",
        "acute_angle": "锐角",
        "right_angle": "直角",
        "obtuse_angle": "钝角",
        "straight_angle": "平角",
        "reflex_angle": "优角",
        "zero_angle": "零角",
        "counterclockwise": "逆时针",
        "clockwise": "顺时针",
        "angle_visualization": "角度可视化",
        
        # 特殊角度
        "special_angles": "特殊角度",
        "select_special_angle": "选择特殊角度",
        "special_angle_30": "30°角：等边三角形的一半，常见于正六边形的内角",
        "special_angle_45": "45°角：等腰直角三角形的一半，表示完全对角的方向",
        "special_angle_60": "60°角：等边三角形的内角，正六边形中心角",
        "special_angle_90": "90°角：直角，垂直线之间的角度",
        "special_angle_120": "120°角：正六边形的内角",
        "special_angle_180": "180°角：平角，两点之间的直线角度",
    },
    
    "en": {
        # General
        "language": "Language",
        "chinese": "Chinese",
        "english": "English",
        "start_side": "Start Side",
        "end_side": "End Side",
        
        # Home Page
        "home_title": "Math Visualization Learning",
        "home_welcome": "Welcome to Math Visualization Learning Platform!",
        "home_description": """
        This is an interactive math learning platform that helps you understand mathematical concepts through visualization and interaction.
        
        Choose from the navigation menu on the left to explore different math topics:
        - Geometry: Explore angles, polygons, circles, and more
        - Algebra: Understand equations, functions, and graphs
        - Statistics: Learn about data analysis and probability
        """,
        
        # Geometry Common
        "geometry_title": "Geometry Exploration",
        "visualization": "Visualization",
        "properties": "Properties",
        "description": "Description",
        "interactive_controls": "Interactive Controls",
        
        # Angles Page
        "angles_title": "Understanding Angles",
        "angles_intro": """
        An angle is one of the fundamental concepts in geometry. It consists of a fixed point (called the vertex) and two rays extending from that point (called the sides).
        
        On this page, you can:
        1. Explore different angles using interactive tools
        2. Learn about common special angles
        3. Understand basic angle concepts and properties
        """,
        
        # Polygons Page
        "polygons_title": "Exploring Polygons 🔷",
        "polygons_intro": "A polygon is a plane figure bounded by line segments connected end to end.",
        "what_is_polygon": "What is a Polygon?",
        "polygon_definition": "A polygon is a **closed** plane figure bounded by a **finite number of line segments**. These line segments are called **sides**, and their endpoints are called **vertices**.",
        
        "basic_elements": "Basic Elements",
        "vertices": "Vertices",
        "vertices_description": "The points where sides meet",
        "sides": "Sides",
        "sides_description": "Line segments connecting vertices",
        "interior_angles": "Interior Angles",
        "interior_angles_description": "Angles inside the polygon",
        "exterior_angles": "Exterior Angles",
        "exterior_angles_description": "Angles formed by a side and the extension of an adjacent side",
        
        "polygon_classification": "Polygon Classification",
        "by_sides": "By Number of Sides",
        "triangle": "Triangle",
        "quadrilateral": "Quadrilateral",
        "pentagon": "Pentagon",
        "hexagon": "Hexagon",
        
        "by_shape": "By Shape Characteristics",
        "convex_polygon": "Convex Polygon",
        "convex_description": "All line segments between any two points lie inside the polygon",
        "concave_polygon": "Concave Polygon",
        "concave_description": "Some line segments between points lie outside the polygon",
        "regular_polygon": "Regular Polygon",
        "regular_description": "All sides equal and all angles equal",
        "irregular_polygon": "Irregular Polygon",
        "irregular_description": "Sides or angles are not all equal",
        
        "important_properties": "Important Properties",
        "sum_of_interior_angles": "Sum of Interior Angles",
        "interior_angles_formula": "Sum of interior angles of an n-sided polygon = (n-2) × 180°",
        "sum_of_exterior_angles": "Sum of Exterior Angles",
        "exterior_angles_property": "The sum of exterior angles of any polygon is 360°, a remarkable property!",
        "number_of_diagonals": "Number of Diagonals",
        "diagonals_formula": "Number of diagonals in an n-sided polygon = n(n-3) ÷ 2",
        
        "examples": "Examples",
        "area": "Area",
        "area_calculator": "Area Calculator",
        "regular_area_formula": "Area = Perimeter × Radius ÷ 2",
        "irregular_area_description": "Can be calculated using triangulation method",
        
        "number_of_sides": "Number of Sides",
        "side_length": "Side Length",
        "equal_sides": "All sides are equal",
        "angles": "Angle Properties",
        "equal_interior_angles": "All interior angles are equal",
        "equal_exterior_angles": "All exterior angles are equal",
        "interior_angle": "Each Interior Angle",
        "exterior_angle": "Each Exterior Angle",
        
        "symmetry": "Symmetry",
        "symmetry_axes": "Number of Symmetry Axes",
        "rotational_symmetry": "Rotational Symmetry: Coincides with original after rotation",
        
        "circle_relationships": "Circle Relationships",
        "inscribed_circle": "Can be inscribed in a circle",
        "circumscribed_circle": "Can be circumscribed about a circle",
        "equal_radius": "All vertices are equidistant from center",
        
        "fun_facts": "Fun Facts",
        "bee_nest_secret": "The Mystery of Honeycomb",
        "bee_nest_description": "Why do bees build hexagonal honeycombs? Because regular hexagons are the most circle-like polygons that can completely tile a plane, maximizing efficiency and strength while minimizing material usage.",
        "gauss_and_17_gon": "Gauss and the 17-gon",
        "gauss_description": """At age 19, Gauss proved that a regular 17-sided polygon could be constructed using only compass and straightedge. This discovery led him to dedicate his life to mathematics.
        In fact, regular polygons that can be constructed with compass and straightedge must have the number of sides in the form of:
        - Powers of 2 (4, 8, 16, ...)
        - Fermat primes (3, 5, 17, 257, ...)
        - Products of the above""",
        "polygons_in_nature": "Polygons in Nature",
        "polygons_in_nature_description": """
        - Snowflakes exhibit hexagonal structure
        - Basalt columns often form hexagons
        - Garnet crystals form dodecahedrons
        - Honeycombs form regular hexagons""",
        "polygons_in_life": "Polygons in Daily Life",
        "polygons_in_life_description": """
        - Traffic signs: Octagon (Stop), Triangle (Warning)
        - Architecture: Pentagon (Pentagon Building)
        - Sports: Soccer ball (Pentagons and Hexagons)""",
    }
}
