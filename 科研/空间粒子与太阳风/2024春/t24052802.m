% 读取 CDF 文件信息和数据
addpath 'matlab_plug-ins'
data = spdfcdfinfo('0404.cdf');
datan = spdfcdfread('0404.cdf');
time = datan{1,1};
eng = datan{1,19};
flx = datan{1,15};
flxt = log(flx');

% 处理原始数据中的 NaN 值：用邻近的值填补 NaN
flxt_filled = fillmissing(flxt, 'nearest', 2); % 沿列方向用邻近值填补 NaN
flxt_filled = fillmissing(flxt_filled, 'nearest', 1); % 沿行方向用邻近值填补 NaN

% 原始数据的网格坐标
[rows, cols] = size(flxt);
[x, y] = meshgrid(1:cols, 1:rows);

% 创建一个更密集的网格，但在原始数据范围内
[xq, yq] = meshgrid(linspace(1, cols, 200), linspace(1, rows, 200)); % 更高密度的网格

% 对数据进行线性插值
flxt_interp = interp2(x, y, flxt_filled, xq, yq, 'linear'); % 使用 'linear' 插值方法

% 处理插值结果中的 NaN 值：用邻近值填补 NaN
flxt_interp = fillmissing(flxt_interp, 'nearest'); % 用邻近值填补 NaN

% 绘制颜色图
colormap jet
s = pcolor(xq, yq, flxt_interp);
s.FaceColor = 'interp';
shading interp
clim([-2,3]);

% 设置图形属性
ylabel('Electron Energy / (keV)')
xlabel('Time')
c1 = colorbar;
set(get(c1,'ylabel'),'string','Log10 Efux','fontsize',10);

% 设置x轴刻度
set(gca, 'xtick', 0:3000:12000)
xlim([0,12000])
set(gca, 'XTickLabel',{'0:00:00','6:00:00','12:00:00','18:00:00','24:00:00'})

% 设置y轴刻度标签（原始 y 轴刻度）
y_ticks = [1, 2, 3, 4, 5, 6, 7, 8]; % 原始 y 轴刻度
y_labels = {'21.05', '23.94', '29.01', '37.69', '52.88', '79.64', '126.65', '206.94'}; % 替换后的实际物理量

set(gca, 'ytick', y_ticks)
set(gca, 'YTickLabel', y_labels)

% 设置 y 轴为对数尺度
set(gca, 'YScale', 'log');

% 在 y 轴上添加对数刻度标识
log_ticks = [1e2, 1e3, 1e4]; % 对数标识的值
log_labels = {'10^2', '10^3', '10^4'}; % 对应的对数标识标签

% 添加对数标识
for i = 1:length(log_ticks)
    y_value = log_ticks(i);
    if any(y_value == 10.^y_ticks) % 检查是否在 y 轴刻度位置
        text(0, y_value, log_labels{i}, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'left', 'Color', 'k', 'FontSize', 10, 'FontWeight', 'bold')
    end
end

% 设置次要刻度（如果需要）
set(gca, 'xminortick', 'on')
set(gca, 'yminortick', 'on')

% 其他图形设置
set(gca, 'tickdir', 'in')
set(gca, 'FontName', 'Times New Roman', 'FontSize', 10)
set(gca, 'Layer', 'top');
set(gca, 'LineWidth', 1)
