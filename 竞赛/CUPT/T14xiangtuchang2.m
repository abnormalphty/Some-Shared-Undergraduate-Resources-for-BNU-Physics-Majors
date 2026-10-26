function dynamic_saddle_point_plot()
    % 设置系统的初始参数
    alpha = 1;
    beta = 2;
    delta_min = -10; % delta 最小值，从 -10 开始
    delta_max = -0.1; % delta 最大值，保证 \delta < 0
    delta_step = 0.05; % delta 变化步长

    % 创建图形窗口
    fig = figure('Name', 'Dynamic Saddle Point Plot', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 创建显示 \chi 和 \gamma 的文本框
    chi_text = uicontrol('Style', 'text', 'String', '', 'Position', [300, 550, 120, 20]);
    gamma_text = uicontrol('Style', 'text', 'String', '', 'Position', [300, 520, 120, 20]);

    % 创建图形轴：用于 \theta_0 随 \delta 和 \gamma 的变化
    ax1 = axes('Parent', fig, 'Position', [0.1, 0.55, 0.8, 0.35]);
    xlabel(ax1, '\delta');
    ylabel(ax1, '\theta_0');
    title(ax1, '\theta_0 vs. \delta');
    grid(ax1, 'on');
    hold(ax1, 'on');

    % 创建图形轴：用于 \gamma 随 \delta 的变化
    ax2 = axes('Parent', fig, 'Position', [0.1, 0.1, 0.8, 0.35]);
    xlabel(ax2, '\delta');
    ylabel(ax2, '\gamma');
    title(ax2, '\gamma vs. \delta');
    grid(ax2, 'on');
    hold(ax2, 'on');

    % 动态更新图像
    gamma_values = [];
    theta_values = [];
    delta_values = [];

    for delta = delta_min:delta_step:delta_max
        % 更新系统参数
        [chi, gamma] = compute_chi_gamma(alpha, beta, delta);
        theta_0 = compute_saddle_point(alpha, beta, delta);

        % 保存 \gamma 和 \theta_0 的值
        gamma_values(end+1) = gamma;
        theta_values(end+1) = theta_0;
        delta_values(end+1) = delta;

        % 更新显示的 \chi 和 \gamma 的值
        set(chi_text, 'String', sprintf('\\chi = %.2f', chi));
        set(gamma_text, 'String', sprintf('\\gamma = %.2e', gamma));

        % 绘制 \theta_0 vs. \delta 的动态图像
        plot(ax1, delta_values, theta_values, 'b-', 'LineWidth', 2);
        % 绘制 \gamma vs. \delta 的动态图像
        plot(ax2, delta_values, gamma_values, 'r-', 'LineWidth', 2);

        drawnow;
    end
end

function [chi, gamma] = compute_chi_gamma(alpha, beta, delta)
    % 计算 \chi 和 \gamma
    A = beta;
    B = -delta * A;
    C = alpha * A;
    
    chi = A - 1;
    gamma = (B + 1) * C / (A * (B + 1) + B);
    
    % 扩大 \gamma 的范围，并确保 \gamma > 0
    gamma = abs(gamma) * 1e5;
end

function [theta_0] = compute_saddle_point(alpha, beta, delta)
    % 计算鞍点 \theta_0
    if delta < -alpha
        theta_0 = (1 / beta) * log(-delta / alpha);
    else
        theta_0 = NaN;
    end
end
