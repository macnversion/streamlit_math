"""
Manim 动画组件示例
"""
import streamlit as st
from manim import *
import tempfile
import os

class ManimDemo:
    """Manim 演示类"""
    
    @staticmethod
    def create_temp_media_dir():
        """创建临时媒体目录"""
        temp_dir = tempfile.mkdtemp()
        return temp_dir

    def render_scene(self, scene_class, quality="medium_quality"):
        """渲染 Manim 场景

        Args:
            scene_class: Manim Scene 类
            quality: 渲染质量，可选 "low_quality", "medium_quality", "high_quality"
        """
        scene = scene_class()
        scene.render()
        # 使用 Manim 生成的实际视频路径
        video_path = f"media/videos/1080p60/{scene_class.__name__}.mp4"
        return video_path

    def show_function_animation(self, func_type="sin"):
        """显示函数动画

        Args:
            func_type: 函数类型，可选 "sin", "quadratic", "exponential"
        """
        class FunctionScene(Scene):
            def construct(self):
                # 创建坐标轴
                axes = Axes(
                    x_range=[-3, 3, 1],
                    y_range=[-2, 2, 1],
                    axis_config={"color": BLUE},
                )
                
                # 根据函数类型选择不同的函数
                if func_type == "sin":
                    graph = axes.plot(lambda x: np.sin(x), color=WHITE)
                    label = MathTex(r"f(x)=\sin(x)")
                elif func_type == "quadratic":
                    graph = axes.plot(lambda x: x**2, color=WHITE)
                    label = MathTex(r"f(x)=x^2")
                else:  # exponential
                    graph = axes.plot(lambda x: np.exp(x), color=WHITE)
                    label = MathTex(r"f(x)=e^x")
                
                # 设置标签位置
                label.to_corner(UR)
                
                # 创建动画
                self.play(Create(axes))
                self.play(Create(graph))
                self.play(Write(label))
                self.wait()

        # 渲染场景并显示
        video_path = self.render_scene(FunctionScene)
        st.video(video_path)

    def show_geometry_animation(self, shape_type="square"):
        """显示几何变换动画

        Args:
            shape_type: 形状类型，可选 "square", "circle", "triangle"
        """
        class GeometryScene(Scene):
            def construct(self):
                # 创建形状
                if shape_type == "square":
                    shape = Square(color=BLUE)
                elif shape_type == "circle":
                    shape = Circle(color=BLUE)
                else:  # triangle
                    shape = Triangle(color=BLUE)
                
                # 创建动画序列
                self.play(Create(shape))
                self.play(Rotate(shape, PI/2))
                self.play(shape.animate.scale(2))
                self.play(shape.animate.set_color(RED))
                self.wait()

        # 渲染场景并显示
        video_path = self.render_scene(GeometryScene)
        st.video(video_path)
