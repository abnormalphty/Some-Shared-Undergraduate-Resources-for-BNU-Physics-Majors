function phase_diagram_with_y0_animation
    % 定义系统初始参数
    alpha = 1;
    beta = 1.6; % 确保初始值在范围内
    delta = -4;

    % 创建图形窗口
    fig = figure('Name', 'y_0 vs \theta_{max} Animation', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 创建y_0和theta_max关系图的图形轴
    ax_plot = axes('Parent', fig, 'Position', [0.2, 0.2, 0.7, 0.7]);
    xlabel(ax_plot, '$y_0$', 'FontSize', 16, 'Interpreter', 'latex');
    ylabel(ax_plot, '$\theta_{max}$', 'FontSize', 16, 'Interpreter', 'latex');
    title(ax_plot, '$y_0 \,\, and \,\, \theta_{max}$', 'FontSize', 16, 'Interpreter', 'latex');
    grid(ax_plot, 'on');
    hold(ax_plot, 'on');

    % 初始化图形并开始动画
    animate_phase_diagram(alpha, beta, delta);

    function animate_phase_diagram(alpha_val, beta_val, delta_val)
        y0_vals = [];
        theta_max_vals = [];
        for y0_val = 0.1:0.05:5
            tspan = [0, 20];
            initial_conditions = [0, y0_val];
            
            [t, sol, te, ye, ie] = ode45(@(t, X) [X(2); alpha_val * exp(beta_val * X(1)) + delta_val], tspan, initial_conditions, odeset('Events', @divergence_event));

            % 只绘制 x > 0 的轨迹
            valid_indices = sol(:, 1) > 0;
            if any(valid_indices)
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

                    % 记录 y_0 和 theta_max
                    y0_vals = [y0_vals, y0_val];
                    theta_max_vals = [theta_max_vals, theta_max];
                else
                    break; % 如果找不到交点，停止增加 y_0
                end
            end
            
            % 更新 y_0 和 theta_max 的关系图
            cla(ax_plot);
            plot(ax_plot, y0_vals, theta_max_vals, '-o', 'LineWidth', 2);
            
            % 暂停以可视化动画效果
            pause(0.1);
        end
    end

    function [value, isterminal, direction] = divergence_event(~, X)
        value = X(2) - 10; % 当 y > 10 时，value > 0
        isterminal = 1; % 终止积分
        direction = 0; % 无论 y 是增大还是减小，均触发事件
    end
end
