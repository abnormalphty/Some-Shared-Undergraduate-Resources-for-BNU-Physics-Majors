from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


OUTPUT_NAME = "[学号已脱敏]学生.pptx"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

COLORS = {
    "navy": RGBColor(18, 34, 61),
    "blue": RGBColor(42, 103, 179),
    "cyan": RGBColor(52, 172, 193),
    "green": RGBColor(76, 150, 124),
    "orange": RGBColor(230, 148, 66),
    "light": RGBColor(244, 247, 251),
    "panel": RGBColor(255, 255, 255),
    "muted": RGBColor(94, 108, 132),
    "dark": RGBColor(28, 39, 52),
    "line": RGBColor(210, 219, 232),
}

FONT_CN = "Microsoft YaHei"
FONT_EN = "Aptos"


def set_text(run, size=24, bold=False, color=None, font=FONT_CN):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color or COLORS["dark"]


def set_fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.color.rgb = color


def add_background(slide):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLORS["light"]

    band = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, Inches(0.18)
    )
    set_fill(band, COLORS["blue"])


def add_page_title(slide, title, subtitle=None):
    title_box = slide.shapes.add_textbox(Inches(0.62), Inches(0.35), Inches(11.8), Inches(0.55))
    p = title_box.text_frame.paragraphs[0]
    p.text = title
    p.alignment = PP_ALIGN.LEFT
    set_text(p.runs[0], size=30, bold=True, color=COLORS["navy"])

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.64), Inches(0.94), Inches(11.4), Inches(0.35))
        p = sub_box.text_frame.paragraphs[0]
        p.text = subtitle
        set_text(p.runs[0], size=13, color=COLORS["muted"])


def add_footer(slide, page_no):
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.62), Inches(7.08), Inches(11.2), Inches(0.01)
    )
    set_fill(line, COLORS["line"])
    foot = slide.shapes.add_textbox(Inches(0.62), Inches(7.12), Inches(11.8), Inches(0.24))
    p = foot.text_frame.paragraphs[0]
    p.text = f"近代物理实验 | SLM 与无序系统光学模拟    {page_no}/6"
    set_text(p.runs[0], size=9, color=COLORS["muted"])
    p.alignment = PP_ALIGN.RIGHT


def add_panel(slide, x, y, w, h, title=None, accent=COLORS["blue"]):
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    panel.fill.solid()
    panel.fill.fore_color.rgb = COLORS["panel"]
    panel.line.color.rgb = COLORS["line"]
    panel.line.width = Pt(1)

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(0.08), h)
    set_fill(bar, accent)

    if title:
        title_box = slide.shapes.add_textbox(x + Inches(0.25), y + Inches(0.18), w - Inches(0.45), Inches(0.35))
        p = title_box.text_frame.paragraphs[0]
        p.text = title
        set_text(p.runs[0], size=17, bold=True, color=accent)
    return panel


def add_bullets(slide, x, y, w, h, bullets, font_size=20, color=COLORS["dark"]):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    for i, item in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        p.level = 0
        p.space_after = Pt(8)
        p.line_spacing = 1.15
        p.font.name = FONT_CN
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
    return box


def add_equation_chip(slide, x, y, w, text, accent=COLORS["cyan"]):
    chip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, Inches(0.52))
    chip.fill.solid()
    chip.fill.fore_color.rgb = RGBColor(234, 246, 249)
    chip.line.color.rgb = accent
    chip.line.width = Pt(1)
    tf = chip.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=15, bold=True, color=COLORS["navy"], font=FONT_EN)


def add_placeholder(slide, x, y, w, h, text, accent):
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    box.line.color.rgb = accent
    box.line.width = Pt(1.5)
    tf = box.text_frame
    tf.clear()
    tf.vertical_anchor = 1
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=18, bold=True, color=accent)
    return box


def build_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # Slide 1: Title Slide
    slide = prs.slides.add_slide(blank)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = COLORS["navy"]

    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(6.8), SLIDE_W, Inches(0.7))
    set_fill(accent, COLORS["cyan"])

    title = slide.shapes.add_textbox(Inches(0.82), Inches(1.62), Inches(11.4), Inches(1.35))
    p = title.text_frame.paragraphs[0]
    p.text = "空间光调制器原理及其在无序系统中的拓展模拟"
    p.alignment = PP_ALIGN.LEFT
    set_text(p.runs[0], size=36, bold=True, color=RGBColor(255, 255, 255))

    subtitle = slide.shapes.add_textbox(Inches(0.86), Inches(3.15), Inches(9.8), Inches(0.5))
    p = subtitle.text_frame.paragraphs[0]
    p.text = "近代物理实验期末汇报 | 汇报人：学生"
    set_text(p.runs[0], size=21, color=RGBColor(220, 233, 247))

    note = slide.shapes.add_textbox(Inches(0.88), Inches(4.48), Inches(10.8), Inches(0.7))
    p = note.text_frame.paragraphs[0]
    p.text = "从液晶相位调制出发，连接二维晶格、k 空间与安德森局域化的光学模拟"
    set_text(p.runs[0], size=17, color=RGBColor(194, 225, 232))

    # Slide 2: Bullet Slide
    slide = prs.slides.add_slide(blank)
    add_background(slide)
    add_page_title(slide, "实验基础与 SLM 调制机制")
    add_panel(slide, Inches(0.72), Inches(1.28), Inches(11.88), Inches(5.65), accent=COLORS["blue"])
    add_bullets(
        slide,
        Inches(1.12),
        Inches(1.62),
        Inches(10.92),
        Inches(3.25),
        [
            "向列型液晶分子具有介电各向异性：外加电场改变分子取向，从而改变有效折射率。",
            "入射偏振光在液晶层中积累相位延迟，延迟量由液晶层厚度、双折射与工作波长决定。",
            "灰度值经驱动电压映射到相位响应曲线，实现逐像素、可编程的相位调制。",
            "通过偏振器或复振幅编码，SLM 不只改变相位，也可等效实现振幅与相位联合控制。",
        ],
        font_size=19,
    )
    add_equation_chip(slide, Inches(1.45), Inches(5.05), Inches(5.1), "Gamma = 2*pi*d*Delta_n / lambda")
    emphasis = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(4.88), Inches(4.82), Inches(0.92))
    emphasis.fill.solid()
    emphasis.fill.fore_color.rgb = RGBColor(235, 242, 255)
    emphasis.line.color.rgb = COLORS["blue"]
    tf = emphasis.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.text = "SLM 提供了一个可通过计算机精确控制的二维复振幅调制场。"
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=16, bold=True, color=COLORS["navy"])
    add_footer(slide, 2)

    # Slide 3: Two Content Slide
    slide = prs.slides.add_slide(blank)
    add_background(slide)
    add_page_title(slide, "物理图像的跨学科同构", "像素网格与傅里叶光学把“光场”翻译成“晶格波函数”")
    add_panel(slide, Inches(0.72), Inches(1.45), Inches(5.82), Inches(4.8), "光学表述", COLORS["cyan"])
    add_panel(slide, Inches(6.80), Inches(1.45), Inches(5.82), Inches(4.8), "固体物理表述", COLORS["orange"])
    add_bullets(
        slide,
        Inches(1.06),
        Inches(2.05),
        Inches(5.08),
        Inches(2.95),
        [
            "SLM 像素间隙形成黑栅效应，天然引入周期采样结构。",
            "4f 系统后焦面对应输入光场的傅里叶面，可直接观察空间频率分布。",
            "空间滤波选择特定衍射级，相当于在动量空间裁剪与重构光场。",
        ],
        font_size=17,
    )
    add_bullets(
        slide,
        Inches(7.14),
        Inches(2.05),
        Inches(5.08),
        Inches(2.95),
        [
            "二维像素阵列可映射为二维晶格，灰度相位对应格点势场或跃迁相位。",
            "后焦面坐标映射到 k 空间（倒易空间），衍射峰对应晶格动量选择定则。",
            "周期结构的倒易格矢定义第一布里渊区，决定可观测的布拉格衍射图样。",
        ],
        font_size=17,
    )
    summary = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.38), Inches(6.32), Inches(10.55), Inches(0.52))
    summary.fill.solid()
    summary.fill.fore_color.rgb = RGBColor(232, 246, 241)
    summary.line.color.rgb = COLORS["green"]
    p = summary.text_frame.paragraphs[0]
    p.text = "这种同构使 SLM 成为天然的光学薛定谔方程模拟器。"
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=17, bold=True, color=COLORS["green"])
    add_footer(slide, 3)

    # Slide 4: Bullet Slide
    slide = prs.slides.add_slide(blank)
    add_background(slide)
    add_page_title(slide, "核心拓展方案：光学安德森局域化")
    add_panel(slide, Inches(0.72), Inches(1.28), Inches(11.88), Inches(5.65), accent=COLORS["green"])
    add_bullets(
        slide,
        Inches(1.12),
        Inches(1.55),
        Inches(10.95),
        Inches(3.35),
        [
            "势场模型：在周期相位光栅 V_periodic(x,y) 上叠加随机相噪矩阵 W*R(x,y)，模拟晶格缺陷与无序势。",
            "无序度 W 控制随机势强度：W 越大，晶格平移对称性破缺越明显，平均自由程缩短。",
            "传播过程可写作光学近似下的薛定谔方程：i*d psi/dz = [-1/(2k0)*nabla_perp^2 + V(x,y)]*psi。",
            "观测量从实空间强度 I(x,y) 与倒空间功率谱 |FFT{psi}|^2 两个维度同时提取。",
        ],
        font_size=18,
    )
    add_equation_chip(slide, Inches(1.35), Inches(5.13), Inches(5.85), "V(x,y) = V_periodic(x,y) + W*R(x,y)", COLORS["green"])
    obs = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.65), Inches(4.78), Inches(4.15), Inches(1.24))
    obs.fill.solid()
    obs.fill.fore_color.rgb = RGBColor(255, 246, 236)
    obs.line.color.rgb = COLORS["orange"]
    tf = obs.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.text = "预期现象"
    set_text(p.runs[0], size=15, bold=True, color=COLORS["orange"])
    p = tf.add_paragraph()
    p.text = "尖锐布拉格衍射峰（布洛赫扩展态）逐渐演化为随机散斑场（波函数局域化）。"
    p.font.name = FONT_CN
    p.font.size = Pt(13)
    p.font.color.rgb = COLORS["dark"]
    add_footer(slide, 4)

    # Slide 5: Two Content Slide
    slide = prs.slides.add_slide(blank)
    add_background(slide)
    add_page_title(slide, "MATLAB 预演与数据处理", "用仿真先验证无序度、采样周期与傅里叶谱之间的关系")
    add_placeholder(
        slide,
        Inches(0.82),
        Inches(1.48),
        Inches(5.8),
        Inches(4.55),
        "请在此处插入\n实空间无序相图",
        COLORS["green"],
    )
    add_placeholder(
        slide,
        Inches(6.72),
        Inches(1.48),
        Inches(5.8),
        Inches(4.55),
        "请在此处插入\n倒空间 FFT 散斑图",
        COLORS["blue"],
    )
    bottom = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.15), Inches(6.2), Inches(11.05), Inches(0.62))
    bottom.fill.solid()
    bottom.fill.fore_color.rgb = RGBColor(235, 242, 255)
    bottom.line.color.rgb = COLORS["line"]
    p = bottom.text_frame.paragraphs[0]
    p.text = "通过 2D FFT 计算空间功率谱，分析衍射斑的展宽与衰减。"
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=17, bold=True, color=COLORS["navy"])
    add_footer(slide, 5)

    # Slide 6: Centered Text
    slide = prs.slides.add_slide(blank)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(247, 249, 252)
    add_page_title(slide, "总结与致谢")
    box = slide.shapes.add_textbox(Inches(1.45), Inches(2.15), Inches(10.45), Inches(1.2))
    tf = box.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.text = "从基础图像处理升维到凝聚态拓扑现象的模拟"
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=28, bold=True, color=COLORS["navy"])

    thanks = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.45), Inches(4.25), Inches(6.45), Inches(0.82))
    thanks.fill.solid()
    thanks.fill.fore_color.rgb = COLORS["navy"]
    thanks.line.color.rgb = COLORS["navy"]
    p = thanks.text_frame.paragraphs[0]
    p.text = "感谢聆听，欢迎提问。"
    p.alignment = PP_ALIGN.CENTER
    set_text(p.runs[0], size=24, bold=True, color=RGBColor(255, 255, 255))

    add_footer(slide, 6)
    return prs


def main():
    output_path = Path(__file__).resolve().parent / OUTPUT_NAME
    prs = build_presentation()
    prs.save(output_path)
    print(f"PPT saved to: {output_path}")


if __name__ == "__main__":
    main()
