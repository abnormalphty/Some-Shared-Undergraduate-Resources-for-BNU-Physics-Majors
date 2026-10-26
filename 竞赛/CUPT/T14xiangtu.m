function phase_diagram_with_y0_slider
    % 定义系统初始参数
    alpha = 1;
    beta = 2; % 确保初始值在范围内
    delta = 0;
    y0 = 1; % y_0 的初始值

    % 创建图形窗口
    fig = figure('Name', '2D Nonlinear System Phase Diagram with Sliders', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 添加滑块用于调整参数 alpha
    uicontrol('Style', 'text', 'String', 'Alpha:', 'Position', [20, 550, 60, 20]);
    alpha_slider = uicontrol('Style', 'slider', 'Min', 0, 'Max', 10, 'Value', alpha, 'Position', [80, 550, 120, 20]);

    % 添加文本标签用于显示 alpha 当前值
    alpha_text = uicontrol('Style', 'text', 'String', num2str(alpha), 'Position', [210, 550, 60, 20]);

    % 添加滑块用于调整参数 beta
    uicontrol('Style', 'text', 'String', 'Beta:', 'Position', [20, 520, 60, 20]);
    beta_slider = uicontrol('Style', 'slider', 'Min', 1.5, 'Max', 2.5, 'Value', beta, 'Position', [80, 520, 120, 20]);

    % 添加文本标签用于显示 beta 当前值
    beta_text = uicontrol('Style', 'text', 'String', num2str(beta), 'Position', [210, 520, 60, 20]);

    % 添加滑块用于调整参数 delta
    uicontrol('Style', 'text', 'String', 'Delta:', 'Position', [20, 490, 60, 20]);
    delta_slider = uicontrol('Style', 'slider', 'Min', -20, 'Max', 20, 'Value', delta, 'Position', [80, 490, 120, 20]);

    % 添加文本标签用于显示 delta 当前值
    delta_text = uicontrol('Style', 'text', 'String', num2str(delta), 'Position', [210, 490, 60, 20]);

    % 添加滑块用于调整 y_0
    uicontrol('Style', 'text', 'String', 'y_0:', 'Position', [20, 460, 60, 20]);
    y0_slider = uicontrol('Style', 'slider', 'Min', 0.1, 'Max', 5, 'Value', y0, 'Position', [80, 460, 120, 20]);

    % 添加文本标签用于显示 y_0 当前值
    y0_text = uicontrol('Style', 'text', 'String', num2str(y0), 'Position', [210, 460, 60, 20]);

    % 创建图形轴
    ax = axes('Parent', fig, 'Position', [0.1, 0.2, 0.8, 0.7]);
    xlabel(ax, 'x');
    ylabel(ax, 'y');
    title(ax, 'Phase Diagram with Dynamic Alpha, Beta, Delta, and y_0');
    grid(ax, 'on');

    % 设置滑块回调函数
    alpha_slider.Callback = @update_plot;
    beta_slider.Callback = @update_plot;
    delta_slider.Callback = @update_plot;
    y0_slider.Callback = @update_plot;

    % 初始化图形
    update_plot();

    function update_plot(~, ~)
        alpha = alpha_slider.Value;
        beta = beta_slider.Value;
        alpha_text.String = num2str(alpha);
        beta_text.String = num2str(beta);
        delta = delta_slider.Value;
        delta_text.String = num2str(delta);
        y0 = y0_slider.Value;
        y0_text.String = num2str(y0);
        update_trajectory(alpha, beta, delta, y0);
    end

    function update_vector_field(alpha_val, beta_val, delta_val)
        x_vals = linspace(0, 2, 20); % 确保 x 值从 0 开始
        y_vals = linspace(0, 2, 20);
        [X, Y] = meshgrid(x_vals, y_vals);
        U = zeros(size(X));
        V = zeros(size(Y));

        for i = 1:numel(X)
            dX = [Y(i); alpha_val * exp(beta_val * X(i)) + delta_val];
            U(i) = dX(1); % 保持原始矢量方向
            V(i) = dX(2); % 保持原始矢量方向
        end
        % 增大矢量场的范围，调整箭头长度
        quiver(ax, X, Y, U, V, 'r', 'AutoScale', 'on', 'AutoScaleFactor', 2, 'LineWidth', 1.5);
    end

    function update_trajectory(alpha_val, beta_val, delta_val, y0_val)
        tspan = [0, 20];
        initial_conditions = [0, y0_val];
        % 清空之前的轨迹
        cla(ax);
        hold(ax, 'on');
        update_vector_field(alpha_val, beta_val, delta_val);

        [t, sol, te, ye, ie] = ode45(@(t, X) [X(2); alpha_val * exp(beta_val * X(1)) + delta_val], tspan, initial_conditions, odeset('Events', @divergence_event));

        % 只绘制 x > 0 的轨迹
        valid_indices = sol(:, 1) > 0;
        if any(valid_indices)
            plot(ax, sol(valid_indices, 1), sol(valid_indices, 2), 'LineWidth', 2);
            
            % 使用插值找到与 x 轴的交点
            y_values = sol(valid_indices, 2);
            x_values = sol(valid_indices, 1);
            idx_cross = find(y_values .* circshift(y_values, -1) <= 0, 1); % 找到符号变化的点
            
            if ~isempty(idx_cross)
                % 使用线性插值计算交点
                x1 = x_values(idx_cross);
                x2 = x_values(idx_cross + 1);
                y1 = y_values(idx_cross);
                y2 = y_values(idx_cross + 1);
                theta_max = x1 - y1 * (x2 - x1) / (y2 - y1);
                
                % 输出 theta_max (与 x 轴交点的横坐标)
                fprintf('Theta_max = %.4f\n', theta_max);
            end
        end
        if ~isempty(te)
            plot(ax, ye(:, 1), ye(:, 2), 'ro'); % 绘制 y 超过 10 的点
        end
    end

    function [value, isterminal, direction] = divergence_event(t, X)
        value = X(2) - 10; % 当 y > 10 时，value > 0
        isterminal = 1; % 终止积分
        direction = 0; % 无论 y 是增大还是减小，均触发事件
    end
end
