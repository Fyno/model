import sys
sys.path.append(r"c:\users\汉乐府\appdata\local\programs\python\python39\lib\site-packages")
# import open3d
# print(open3d.__file__)

import open3d as o3d
# import open3d.core.geometry as o3d_geometry
import numpy as np

# 读取点云数据
pcd_file = "./data/velodyne/003224.bin"
points = np.fromfile(pcd_file, dtype=np.float32).reshape(-1, 4)
pcd = o3d.geometry.PointCloud()
# pcd = o3d_geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points[:, :3])

# 创建可视化窗口并设置参数
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.get_render_option().background_color = [0, 0, 0]
vis.get_view_control().set_zoom(0.5)

# 显示点云数据
vis.run()
vis.destroy_window()
