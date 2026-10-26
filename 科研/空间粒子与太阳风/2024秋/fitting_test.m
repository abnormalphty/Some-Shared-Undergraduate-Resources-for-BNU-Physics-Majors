% 示例数据（替换为你的实际数据）
x_data = logspace(0.1, 2, 100); % 自变量
x_c = 20; % 转折点
y_data = [10 * x_data(x_data <= x_c).^(-1.5), 5 * x_data(x_data > x_c).^(-2)] + ...
         0.1 * randn(1, length(x_data)); % 模拟分段双幂律数据

% 定义分段函数的双幂律模型
double_power_law = @(p, x) (x <= p(5)) .* (p(1) * x.^(-p(2))) + ...
                           (x > p(5)) .* (p(3) * x.^(-p(4)));
% p(1): A1, p(2): alpha1, p(3): A2, p(4): alpha2, p(5): xc

% 初始参数猜测 [A1, alpha1, A2, alpha2, xc]
p0 = [10, 1.5, 5, 2, 15];

% 使用 lsqcurvefit 进行拟合
opts = optimset('Display', 'off'); % 控制输出选项
[p_fit, resnorm] = lsqcurvefit(double_power_law, p0, x_data, y_data, [], [], opts);

% 拟合结果
A1_fit = p_fit(1);
alpha1_fit = p_fit(2);
A2_fit = p_fit(3);
alpha2_fit = p_fit(4);
xc_fit = p_fit(5);

% 绘图
figure;
loglog(x_data, y_data, 'b.', 'DisplayName', '原始数据'); % 原始数据
hold on;
loglog(x_data, double_power_law(p_fit, x_data), 'r-', 'LineWidth', 2, 'DisplayName', '拟合曲线'); % 拟合曲线
legend;
xlabel('x');
ylabel('y');
title('双幂律谱拟合');
grid on;

% 显示拟合参数
fprintf('拟合参数:\n');
fprintf('A1 = %.3f\n', A1_fit);
fprintf('alpha1 = %.3f\n', alpha1_fit);
fprintf('A2 = %.3f\n', A2_fit);
fprintf('alpha2 = %.3f\n', alpha2_fit);
fprintf('xc = %.3f\n', xc_fit);
