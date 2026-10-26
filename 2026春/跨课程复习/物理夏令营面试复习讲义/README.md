# 物理夏令营面试复习讲义

本项目是一份面向量子材料/凝聚态物理夏令营与研究生面试的中文系统讲义。全书按知识依赖划分为八个分部：复习导航与数学工具、理论力学、量子力学、热力学与统计物理、电动力学、固体物理、量子材料与计算、实验与面试训练。核心结论尽量从作用量、Hamiltonian、运动方程、态数或配分函数出发，保留变分、边界条件、近似理由和极限检查。

## 编译

推荐在项目根目录执行：

```bash
latexmk -xelatex -use-biber main.tex
```

也可以执行两遍：

```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

最终输出文件为 `summer_camp_physics_review_notes.pdf`。构建过程先生成 `main.pdf`，再将其复制为上述交付文件名。

若中文字体报错，优先使用最新版 TeX Live/MacTeX 的 XeLaTeX。项目固定使用 TeX Live 自带的 Fandol 字体，不依赖系统中文字体。若参考文献不显示，确认 `biber` 已安装并按上述四步编译。

## 推荐复习顺序

建议进行三轮复习：

1. **第一轮——按依赖建骨架：**数学工具 → 理论力学 → 量子力学 → 热统 → 电动力学 → 固体物理。目标是说清每个模型的起点、自由度和适用条件。
2. **第二轮——形成量材主线：**学习量子材料、计算和实验分部，把 Hubbard、Berry、BCS 与磁性、拓扑、超导及 ARPES/STM/散射数据连接起来。
3. **第三轮——面试输出：**使用高频题、工作册、黑板推导和跨学科例题，将核心题分别压缩为 30 秒、2 分钟和板书版。

不建议从公式速查表开始。速查表用于第三轮核对，不替代正文推导。

## 目录与构建产物

- `main.tex`：入口文件；
- `references.bib`：教材、官方课程与延伸阅读；
- `chapters/`：八个分部下的理论、量材、实验和训练章节；
- `chapters/mathematical_tools.tex`：全书统一使用的 Fourier、本征值、变分、量纲和张量工具；
- `chapters/*_derivations.tex`：各学科的核心计算章节，已在相应分部中紧邻概念骨架；
- `chapters/electrodynamics_action_radiation.tex`：从协变作用量到 Maxwell 方程、推迟势、能流和辐射；
- `chapters/core_worked_examples.tex`：跨学科综合例题和面试压缩训练；
- `chapters/quantum_angular_external_time.tex`：CG 系数、选择定则、外场效应、Rabi 与绝热演化；
- `chapters/quantum_identical_particles.tex`：交换对称性、两电子系统、Slater 行列式、氦交换劈裂与玻色增强；
- `chapters/quantum_scattering.tex`：本科层次 Born 近似、分波、光学定理和低能散射；
- `chapters/ensembles_quantum_gases.tex`：密度矩阵统一三大系综，并推导 Fermi 气、BEC、光子与声子；
- `chapters/waveguides_relativistic_gaussian.tex`：TE/TM/TEM 与 $c=1$ 的 Gaussian 几何制相对论电动力学；
- `figures/`：外部插图目录，主要示意图在 LaTeX 中用 TikZ/pgfplots 自绘；
- `summer_camp_physics_review_notes.pdf`：编译后的讲义。
