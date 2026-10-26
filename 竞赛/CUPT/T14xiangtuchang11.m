function saddle_point_phase_diagram
    % 定义系统初始参数
    alpha = 1;
    beta = 1.6;
    delta = -4;

    % 创建图形窗口
    fig = figure('Name', '2D Nonlinear System with Saddle Point', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 创建图形轴
    ax = axes('Parent', fig, 'Position', [0.1, 0.2, 0.8, 0.7]);
    xlabel(ax, '$\theta$', 'Interpreter', 'latex', 'FontSize', 16);  % 将横坐标标注为 \theta
    ylabel(ax, '$\dot{\theta}$', 'Interpreter', 'latex', 'FontSize', 16);  % 将纵坐标标注为 \dot{\theta}
    title(ax, 'Saddle Point Phase Diagram with Vector Field', 'FontSize', 16);  % 设置标题字号
    grid(ax, 'on');
    axis(ax, [0 1.8 -2 3]);  % 修改x轴范围为[0, 1.8]，y轴范围为[-2, 3]
    set(ax, 'FontSize', 14);  % 调整坐标轴刻度字号

    % 计算并绘制矢量场、鞍点和相轨迹
    plot_vector_field_and_saddle(alpha, beta, delta);

    function plot_vector_field_and_saddle(alpha, beta, delta)
        % 清空之前的图形
        cla(ax);
        hold(ax, 'on');
        
        % 计算鞍点
        if delta / alpha < 0
            x_saddle = (1 / beta) * log(-delta / alpha);
            y_saddle = 0;
        else
            x_saddle = NaN;  % 没有实际鞍点
            y_saddle = NaN;
        end

        % 绘制矢量场
        x_vals = linspace(0, 1.8, 20);  % 修改x轴范围为[0, 1.8]
        y_vals = linspace(-2, 3, 20);   % 修改y轴范围为[-2, 3]
        [X, Y] = meshgrid(x_vals, y_vals);
        U = Y;
        V = alpha * exp(beta * X) + delta;
        quiver(ax, X, Y, U, V, 'r', 'AutoScale', 'on', 'AutoScaleFactor', 1.5, 'LineWidth', 1);

        % 求解并绘制稳定线（从无穷远到鞍点）
        if ~isnan(x_saddle)
            % 从鞍点向左
            [x_stable_left, y_stable_left] = ode45(@(x, y) -(alpha * exp(beta * x) + delta), [x_saddle 0], 1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_left = y_stable_left >= -2 & y_stable_left <= 3;  % 修改y轴范围为[-2, 3]
            plot(ax, x_stable_left(idx_valid_left), y_stable_left(idx_valid_left), 'b', 'LineWidth', 2);
            
            % 从鞍点向右
            [x_stable_right, y_stable_right] = ode45(@(x, y) -(alpha * exp(beta * x) + delta), [x_saddle 1.8], -1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_right = y_stable_right >= -2 & y_stable_right <= 3;  % 修改y轴范围为[-2, 3]
            plot(ax, x_stable_right(idx_valid_right), y_stable_right(idx_valid_right), 'b', 'LineWidth', 2);
        end
        
        % 求解并绘制不稳定线（从鞍点到无穷远）
        if ~isnan(x_saddle)
            % 从鞍点向左
            [x_unstable_left, y_unstable_left] = ode45(@(x, y) alpha * exp(beta * x) + delta, [x_saddle 0], -1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_left = y_unstable_left >= -2 & y_unstable_left <= 3;  % 修改y轴范围为[-2, 3]
            plot(ax, x_unstable_left(idx_valid_left), y_unstable_left(idx_valid_left), 'b', 'LineWidth', 2);
            
            % 从鞍点向右
            [x_unstable_right, y_unstable_right] = ode45(@(x, y) alpha * exp(beta * x) + delta, [x_saddle 1.8], 1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_right = y_unstable_right >= -2 & y_unstable_right <= 3;  % 修改y轴范围为[-2, 3]
            plot(ax, x_unstable_right(idx_valid_right), y_unstable_right(idx_valid_right), 'b', 'LineWidth', 2);
        end
        
        % 绘制鞍点
        if ~isnan(x_saddle)
            plot(ax, x_saddle, y_saddle, 'ko', 'MarkerSize', 8, 'DisplayName', 'Saddle Point');
        end
        
        % 绘制不同初值条件的相轨迹
        initial_conditions = [0, 0.51; 0, 1.01; 0, 1.41; 0, 2.61;0,2.91];  % 调整初值条件的速度，以避免与稳定线和不稳定线相交
        for i = 1:size(initial_conditions, 1)
            [t, sol] = ode45(@(t, z) [z(2); alpha * exp(beta * z(1)) + delta], [0 10], initial_conditions(i, :));
            plot(ax, sol(:, 1), sol(:, 2), 'g', 'LineWidth', 1.5);
        end
        
        hold(ax, 'off');
    end
end
