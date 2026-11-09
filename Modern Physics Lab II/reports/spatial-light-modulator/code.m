clear; clc; close all;

set(groot, 'defaultAxesFontName', 'Songti SC');
set(groot, 'defaultTextFontName', 'Songti SC');
set(groot, 'defaultLegendFontName', 'Songti SC');
set(groot, 'defaultAxesFontSize', 11);
set(groot, 'defaultLineLineWidth', 1.6);
set(groot, 'defaultAxesLineWidth', 0.9);

rootDir = fileparts(mfilename('fullpath'));
dataFile = fullfile(rootDir, 'data.xlsx');
figDir = fullfile(rootDir, 'tex', 'fig');
if ~exist(figDir, 'dir')
    mkdir(figDir);
end

T1 = readcell(dataFile, 'Sheet', 'Sheet1');
angle = cell2mat(T1(2:end, 2));
power0 = cell2mat(T1(2:end, 3));
power255 = cell2mat(T1(2:end, 7));
contrast = power255 ./ power0;

T2 = readcell(dataFile, 'Sheet', 'Sheet2');
gray = cell2mat(T2(2:end, 1));
power = cell2mat(T2(2:end, 2));

fig1 = figure('Color', 'w', 'Units', 'centimeters', 'Position', [3, 3, 15, 9]);
xfitAngle = linspace(0, 350, 600)';
X = [ones(size(angle)), cosd(4 * angle), sind(4 * angle)];
Xfit = [ones(size(xfitAngle)), cosd(4 * xfitAngle), sind(4 * xfitAngle)];
b0 = X \ power0;
b255 = X \ power255;
color0 = [0.0000, 0.4470, 0.7410];
color255 = [0.8500, 0.3250, 0.0980];
plot(xfitAngle, Xfit * b0, '-', 'Color', color0, 'LineWidth', 1.7); hold on;
plot(xfitAngle, Xfit * b255, '-', 'Color', color255, 'LineWidth', 1.7);
scatter(angle, power0, 24, 'o', 'MarkerEdgeColor', color0, 'MarkerFaceColor', 'w', 'LineWidth', 1.0);
scatter(angle, power255, 24, 's', 'MarkerEdgeColor', color255, 'MarkerFaceColor', 'w', 'LineWidth', 1.0);
grid on; box on;
set(gca, 'GridAlpha', 0.18, 'MinorGridAlpha', 0.10);
xlabel('半波片光轴角度 / (deg)');
ylabel('透过光功率 / \muW');
legend('灰度 0 拟合', '灰度 255 拟合', '灰度 0 实验点', '灰度 255 实验点', ...
    'Location', 'northoutside', 'NumColumns', 4, 'Box', 'off');
xlim([0, 350]);
ylim([0, 310]);
exportgraphics(fig1, fullfile(figDir, 'power_angle.png'), 'Resolution', 600);

[maxContrast, idx] = max(contrast);
bestAngle = angle(idx);
fig2 = figure('Color', 'w', 'Units', 'centimeters', 'Position', [3, 3, 15, 9]);
xfitAngle2 = linspace(0, 350, 1200)';
p0Fit = [ones(size(xfitAngle2)), cosd(4 * xfitAngle2), sind(4 * xfitAngle2)] * b0;
p255Fit = [ones(size(xfitAngle2)), cosd(4 * xfitAngle2), sind(4 * xfitAngle2)] * b255;
ratioFit = p255Fit ./ p0Fit;
ratioFit(p0Fit <= 10 | ratioFit > maxContrast * 1.05) = NaN;
plot(xfitAngle2, ratioFit, '-', 'Color', [0.3010, 0.7450, 0.9330], 'LineWidth', 1.6); hold on;
scatter(angle, contrast, 24, 'o', 'MarkerEdgeColor', [0.4940, 0.1840, 0.5560], ...
    'MarkerFaceColor', 'w', 'LineWidth', 1.0);
plot(bestAngle, maxContrast, 'p', 'MarkerSize', 9, 'MarkerFaceColor', [0.6350, 0.0780, 0.1840], ...
    'MarkerEdgeColor', [0.6350, 0.0780, 0.1840]);
grid on; box on;
set(gca, 'GridAlpha', 0.18, 'MinorGridAlpha', 0.10);
xlabel('半波片光轴角度 / (deg)');
ylabel('对比度 I_{255}/I_0');
ylim([0, maxContrast * 1.12]);
text(bestAngle - 95, maxContrast * 0.82, ...
    sprintf('最大值 %.1f\\n角度 %.0f^\\circ', maxContrast, bestAngle), 'FontSize', 10);
legend('由功率拟合得到的参考曲线', '实验点', '最大值', 'Location', 'northwest', 'Box', 'off');
xlim([0, 350]);
exportgraphics(fig2, fullfile(figDir, 'contrast_angle.png'), 'Resolution', 600);

p = polyfit(gray, power, 2);
xfit = linspace(min(gray), max(gray), 300);
yfit = polyval(p, xfit);
yhat = polyval(p, gray);
R2 = 1 - sum((power - yhat).^2) / sum((power - mean(power)).^2);

fig3 = figure('Color', 'w', 'Units', 'centimeters', 'Position', [3, 3, 15, 9]);
plot(xfit, yfit, '-', 'Color', [0.6350, 0.0780, 0.1840], 'LineWidth', 1.7); hold on;
scatter(gray, power, 28, 'o', 'MarkerEdgeColor', color0, 'MarkerFaceColor', 'w', 'LineWidth', 1.0);
grid on; box on;
set(gca, 'GridAlpha', 0.18, 'MinorGridAlpha', 0.10);
xlabel('输入图像灰度');
ylabel('输出光功率 / \muW');
legend(sprintf('二次拟合, R^2=%.4f', R2), '实验点', 'Location', 'northwest', 'Box', 'off');
xlim([0, 255]);
exportgraphics(fig3, fullfile(figDir, 'gray_response.png'), 'Resolution', 600);

fprintf('最大对比度角度: %.0f deg\n', bestAngle);
fprintf('最大对比度 I255/I0: %.6g\n', maxContrast);
fprintf('灰度响应二次拟合: P = %.8g g^2 + %.8g g + %.8g\n', p(1), p(2), p(3));
fprintf('灰度响应 R^2: %.6g\n', R2);
