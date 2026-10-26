% 读取 CDF 文件信息和数据
addpath 'matlab_plug-ins'
data = spdfcdfinfo('0404.cdf');
datan = spdfcdfread('0404.cdf');
time = datan{1,1};
eng = datan{1,19};
flx = datan{1,15};
flxt = log(flx');

% 绘制颜色图
colormap jet
s = pcolor(flxt);
s.FaceColor = 'interp';
shading interp
clim([0,1.25]);

% 设置图形属性
ylabel('Electron Energy / (keV)')
xlabel('Time')
c1 = colorbar;
set(get(c1,'ylabel'),'string','Log10 Efux','fontsize',10);

% 设置x轴刻度
set(gca, 'xtick', 0:3000:12000)
xlim([0,12000])
set(gca, 'XTickLabel',{'0:00:00','6:00:00','12:00:00','18:00:00','24:00:00'})

% 设置y轴刻度标签
y_ticks = [2, 4, 6, 8, 10, 12, 14, 16]; % 原始 y 轴刻度
y_labels = {'21.05', '23.94', '29.01', '37.69', '52.88', '79.64', '126.65', '206.94'}; % 替换后的实际物理量

set(gca, 'ytick', y_ticks)
set(gca, 'YTickLabel', y_labels)

% 在y轴上添加对数刻度标识
log_ticks = [1e2, 1e3, 1e4]; % 对数标识的值
log_labels = {'10^2', '10^3', '10^4'}; % 对应的对数标识标签

for i = 1:length(log_ticks)
    y_value = log_ticks(i);
    if any(y_value == y_ticks) % 只在 y 轴刻度位置添加对数标识
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
