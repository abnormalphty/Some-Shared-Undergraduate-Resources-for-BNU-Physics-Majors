function p_time_evolution_plot()
    % 设置系统的初始参数
    alpha = 1;
    beta = 1.6;
    delta = -4; % 固定 delta 值
    
    % 创建图形窗口
    fig = figure('Name', 'p vs Time Plot', 'NumberTitle', 'off', 'Position', [100, 100, 800, 600]);

    % 创建图形轴用于显示 p 随时间演化
    ax_p_time = axes('Parent', fig, 'Position', [0.1, 0.1, 0.8, 0.8]);
    xlabel(ax_p_time, 'Time', 'FontSize', 14);
    ylabel(ax_p_time, 'p', 'FontSize', 14);
    title(ax_p_time, 'p vs. Time', 'FontSize', 16);
    grid(ax_p_time, 'on');
    hold(ax_p_time, 'on');

    % 计算并绘制 p 随时间演化的曲线
    [time, p_time] = compute_p_evolution(alpha, beta, delta);
    plot(ax_p_time, time, p_time, 'b-', 'LineWidth', 2);
    drawnow;
end

function [time, p_time] = compute_p_evolution(alpha, beta, delta)
    % 计算 p 随时间的演化，直到 \theta 回到 0
    tspan = [0, 100]; % 初始时间范围
    initial_conditions = [0; 1.8]; % 初始角度 \theta_0 和初始角速度为 1
    
    % 设置 ODE 解算器选项
    options = odeset('Events', @(t, X) stop_event(t, X, alpha, beta, delta), ...
                     'RelTol', 1e-8, 'AbsTol', 1e-10);
    
    % 计算 ODE 解
    [time, sol] = ode45(@(t, X) [X(2); alpha * exp(beta * X(1)) + delta], tspan, initial_conditions, options);
    
    % 计算 p 随时间的变化
    p_time = 100000*alpha * exp(beta * sol(:, 1)) + delta+10^6;
end

function [value, isterminal, direction] = stop_event(~, X, alpha, beta, delta)
    % 事件函数: 检测 \theta 是否回到 0
    theta = X(1);
    value = theta; % 目标值为 0
    isterminal = 1; % 事件发生时停止求解
    direction = 0; % 不管 \theta 方向
end
