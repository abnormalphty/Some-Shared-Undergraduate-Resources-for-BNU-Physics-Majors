function phase_diagram_with_y0_slider
    % 定义系统初始参数
    alpha = 1;
    beta = 2; % 确保初始值在范围内
    delta = 0;
    y0_start = 0.1; % y_0 的起始值
    y0_end = 5; % y_0 的结束值
    y0_step = 0.01; % y_0 的步长

    % 创建图形窗口
    fig = figure('Name', '2D Nonlinear System Phase Diagram', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 添加文本框用于输入 alpha
    uicontrol('Style', 'text', 'String', 'Alpha:', 'Position', [20, 550, 60, 20]);
    alpha_edit = uicontrol('Style', 'edit', 'String', num2str(alpha), 'Position', [80, 550, 60, 20]);

    % 添加文本框用于输入 beta
    uicontrol('Style', 'text', 'String', 'Beta:', 'Position', [20, 520, 60, 20]);
    beta_edit = uicontrol('Style', 'edit', 'String', num2str(beta), 'Position', [80, 520, 60, 20]);

    % 添加文本框用于输入 delta
    uicontrol('Style', 'text', 'String', 'Delta:', 'Position', [20, 490, 60, 20]);
    delta_edit = uicontrol('Style', 'edit', 'String', num2str(delta), 'Position', [80, 490, 60, 20]);

    % 添加按钮用于更新绘图
    uicontrol('Style', 'pushbutton', 'String', 'Update', 'Position', [20, 460, 120, 30], 'Callback', @update_plot);

    % 创建子图用于显示 y_0 与 theta_max 的关系
    ax1 = subplot(1, 2, 1, 'Parent', fig);
    xlabel(ax1, 'y_0');
    ylabel(ax1, 'Theta_{max}');
    title(ax1, 'y_0 vs Theta_{max}');
    grid(ax1, 'on');
    hold(ax1, 'on');

    % 创建子图用于显示相图
    ax2 = subplot(1, 2, 2, 'Parent', fig);
    xlabel(ax2, 'x');
    ylabel(ax2, 'y');
    title(ax2, 'Phase Diagram');
    grid(ax2, 'on');
    hold(ax2, 'on');

    function update_plot(~, ~)
        % 获取用户输入的 alpha、beta 和 delta 值
        alpha = str2double(alpha_edit.String);
        beta = str2double(beta_edit.String);
        delta = str2double(delta_edit.String);

        % 初始化数据存储
        y0_values = y0_start:y0_step:y0_end;
        theta_max_values = zeros(size(y0_values));

        % 遍历 y_0 并计算 theta_max
        for i = 1:length(y0_values)
            y0 = y0_values(i);
            theta_max = compute_theta_max(alpha, beta, delta, y0, ax2);
            theta_max_values(i) = theta_max;

            % 如果 theta_max 不存在，停止循环
            if isnan(theta_max)
                break;
            end
        end

        % 清除旧图并绘制新图
        cla(ax1);
        plot(ax1, y0_values, theta_max_values, '-o', 'LineWidth', 2);
    end

    function theta_max = compute_theta_max(alpha_val, beta_val, delta_val, y0_val, ax)
        tspan = [0, 20];
        initial_conditions = [0, y0_val];
        
        % 清空之前的轨迹
        cla(ax);

        % 求解微分方程
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
            else
                theta_max = NaN;
            end
        else
            theta_max = NaN;
        end
    end

    function [value, isterminal, direction] = divergence_event(~, X)
        value = X(2) - 10; % 当 y > 10 时，value > 0
        isterminal = 1; % 终止积分
        direction = 0; % 无论 y 是增大还是减小，均触发事件
    end
end
