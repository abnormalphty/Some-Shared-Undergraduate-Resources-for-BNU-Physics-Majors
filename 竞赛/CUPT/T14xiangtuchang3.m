function dynamic_saddle_point_plot()
    % 设置系统的初始参数
    alpha = 1;
    beta = 2;
    delta = -3; % 初始 delta 值
    delta_max = -0.1; % delta 最大值，保证 \delta < 0
    delta_step = 0.05; % delta 变化步长

    % 创建图形窗口
    fig = figure('Name', 'Dynamic Saddle Point Plot', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 创建图形轴
    ax = axes('Parent', fig, 'Position', [0.1, 0.2, 0.8, 0.7]);
    xlabel(ax, '\gamma', 'FontSize', 14);
    ylabel(ax, '\theta_0', 'FontSize', 14);
    %title(ax, '$Saddle Point and \grmma$', 'FontSize', 16, 'Interpreter', 'latex');
    grid(ax, 'on');
    hold(ax, 'on');
    
    % 动态更新图像
    gamma_values = [];
    theta_values = [];

    for delta = -3:delta_step:delta_max
        % 更新系统参数
        [chi, gamma] = compute_chi_gamma(alpha, beta, delta);
        [theta_0] = compute_saddle_point(alpha, beta, delta);

        % 保证 \theta_0 > 0 且 \gamma > 0
        if theta_0 > 0 && gamma > 0
            % 保存 \gamma 和 \theta_0 的值
            gamma_values(end+1) = gamma;
            theta_values(end+1) = theta_0;

            % 绘制 \gamma 和 \theta_0 的动态图像
            plot(ax, gamma_values, theta_values, 'b-', 'LineWidth', 2);
            drawnow;
        end
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
