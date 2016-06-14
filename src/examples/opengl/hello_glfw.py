#!/bin/env python

# file hello_glfw.py

from glfw_app import GlfwApp
from openvr_gl_renderer import OpenVrGlRenderer
from color_cube_actor import ColorCubeActor

"""
Minimal glfw programming example which colored OpenGL cube scene that can be closed by pressing ESCAPE.
"""


if __name__ == "__main__":
    actor = ColorCubeActor()
    renderer = OpenVrGlRenderer(actor)
    with GlfwApp(renderer, "glfw OpenVR color cube") as glfwApp:
        glfwApp.run_loop()