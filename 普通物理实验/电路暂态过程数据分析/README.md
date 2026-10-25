# 电路暂态过程数据分析

本目录包含 RC、RL 与 RLC 电路暂态过程的拟合脚本，以及 RLC 波形的 FFT 分析脚本。

## 使用方式

- 依赖：Python 3、`numpy`、`matplotlib`、`scipy`、`openpyxl`。
- 将待分析的 Excel 文件放在脚本工作目录，并把每个脚本顶部的 `path` 改为本机路径。
- `拟合RC.py`、`拟合RL.py`、`拟合RLC.py` 分别读取 `RC2.xlsx`、`RL.xlsx`、`RLC.xlsx` 的 `Sheet1` 工作表：A 列为时间，B 列为电压。
- `FFT.py` 读取 `RLC.xlsx` 的同一数据格式，并绘制频谱。

原始实验数据不随仓库发布。脚本保留其课程作业时期的参数、坐标范围与拟合模型；复现实验时应根据自己的采样间隔、零点偏移和量程重新检查。
