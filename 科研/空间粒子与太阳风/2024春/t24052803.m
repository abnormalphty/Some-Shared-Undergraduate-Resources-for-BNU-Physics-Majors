% 文件列表
files = {'data1.cdf', 'data2.cdf', 'data3.cdf'}; % 替换为实际文件名

% 初始化空的变量
time_combined = [];
eng_combined = [];
flx_combined = [];

% 读取并合并数据
for i = 1:length(files)
    data = spdfcdfinfo(files{i});
    datan = spdfcdfread(files{i});
    time = datan{1,1};
    eng = datan{1,19};
    flx = datan{1,15};
    
    % 进行合并
    time_combined = [time_combined; time];
    eng_combined = [eng_combined; eng];
    flx_combined = [flx_combined; flx];
end

% 将合并后的数据转为对数值
flxt_combined = log(flx_combined);

% 将时间数据转换为 datetime 对象
time_combined_dt = datetime(time_combined, 'ConvertFrom', 'posixtime'); % 根据实际时间格式进行转换

% 对时间进行排序
[time_sorted, sort_idx] = sort(time_combined_dt);
eng_sorted = eng_combined(sort_idx);
flx_sorted = flx_combined(sort_idx);

% 转换 datetime 对象为数值格式
time_numeric = datenum(time_sorted);

% 创建插值网格
[xq, yq] = meshgrid(linspace(min(time_numeric), max(time_numeric), 400), linspace(min(eng_sorted), max(eng_sorted), 400));

% 对数据进行插值
flxt_interp = griddata(time_numeric, eng_sorted, flxt_combined(sort_idx), xq, yq, 'linear'); % 使用 'linear' 插值方法

% 处理插值结果中的 NaN 值：用邻近值填补 NaN
flxt_interp = fillmissing(flxt_interp, 'nearest'); % 用邻近值填补 NaN

% 绘制颜色图
figure;
colormap jet
s = pcolor(xq, yq, flxt_interp);
s.FaceColor = 'interp';
shading interp
clim([0, 1.25]);

% 设置图形属性
ylabel('Electron Energy / (keV)')
xlabel('Time')
c1 = colorbar;
set(get(c1, 'ylabel'), 'string', 'Log10 Efux', 'fontsize', 10);

% 设置x轴和y轴刻度
time_ticks = linspace(min(time_numeric), max(time_numeric), 5); % 根据实际时间范围设置刻度
set(gca, 'xtick', time_ticks)
set(gca, 'XTickLabel', datestr(time_ticks, 'HH:MM:SS'))

% 自定义 y 轴刻度标签
y_ticks = linspace(1, 8, 8); % 原始 y 轴刻度
y_labels = {'21.05', '23.94', '29.01', '37.69', '52.88', '79.64', '126.65', '206.94'}; % 替换后的实际物理量

set(gca, 'ytick', y_ticks)
set(gca, 'YTickLabel', y_labels)

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
