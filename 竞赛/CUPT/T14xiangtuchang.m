function saddle_point_phase_diagram
    % 定义系统初始参数
    alpha = 1;
    beta = 2;
    delta = 0;

    % 创建图形窗口
    fig = figure('Name', '2D Nonlinear System with Saddle Point', 'NumberTitle', 'off', 'Position', [100, 100, 1200, 600]);

    % 添加滑块用于调整参数 alpha, beta, delta
    uicontrol('Style', 'text', 'String', 'Alpha:', 'Position', [20, 550, 60, 20]);
    alpha_slider = uicontrol('Style', 'slider', 'Min', 0.1, 'Max', 10, 'Value', alpha, 'Position', [80, 550, 120, 20]);

    uicontrol('Style', 'text', 'String', 'Beta:', 'Position', [20, 520, 60, 20]);
    beta_slider = uicontrol('Style', 'slider', 'Min', 1.5, 'Max', 2.5, 'Value', beta, 'Position', [80, 520, 120, 20]);

    uicontrol('Style', 'text', 'String', 'Delta:', 'Position', [20, 490, 60, 20]);
    delta_slider = uicontrol('Style', 'slider', 'Min', -10, 'Max', 10, 'Value', delta, 'Position', [80, 490, 120, 20]);

    % 创建图形轴
    ax = axes('Parent', fig, 'Position', [0.1, 0.2, 0.8, 0.7]);
    xlabel(ax, 'x');
    ylabel(ax, 'y');
    title(ax, 'Saddle Point Phase Diagram with Vector Field');
    grid(ax, 'on');
    axis(ax, [0 2 -2 2]);

    % 设置滑块回调函数
    alpha_slider.Callback = @update_plot;
    beta_slider.Callback = @update_plot;
    delta_slider.Callback = @update_plot;

    % 初始化图形
    update_plot();

    function update_plot(~, ~)
        alpha = alpha_slider.Value;
        beta = beta_slider.Value;
        delta = delta_slider.Value;
        plot_vector_field_and_saddle(alpha, beta, delta);
    end

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
        x_vals = linspace(0, 2, 20);
        y_vals = linspace(-2, 2, 20);
        [X, Y] = meshgrid(x_vals, y_vals);
        U = Y;
        V = alpha * exp(beta * X) + delta;
        quiver(ax, X, Y, U, V, 'r', 'AutoScale', 'on', 'AutoScaleFactor', 1.5, 'LineWidth', 1);

        % 求解并绘制稳定线（从无穷远到鞍点）
        if ~isnan(x_saddle)
            % 从鞍点向左
            [x_stable_left, y_stable_left] = ode45(@(x, y) -(alpha * exp(beta * x) + delta), [x_saddle 0], 1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_left = y_stable_left >= -2 & y_stable_left <= 2;
            plot(ax, x_stable_left(idx_valid_left), y_stable_left(idx_valid_left), 'b', 'LineWidth', 2);
            
            % 从鞍点向右
            [x_stable_right, y_stable_right] = ode45(@(x, y) -(alpha * exp(beta * x) + delta), [x_saddle 2], -1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_right = y_stable_right >= -2 & y_stable_right <= 2;
            plot(ax, x_stable_right(idx_valid_right), y_stable_right(idx_valid_right), 'b', 'LineWidth', 2);
        end
        
        % 求解并绘制不稳定线（从鞍点到无穷远）
        if ~isnan(x_saddle)
            % 从鞍点向左
            [x_unstable_left, y_unstable_left] = ode45(@(x, y) alpha * exp(beta * x) + delta, [x_saddle 0], -1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_left = y_unstable_left >= -2 & y_unstable_left <= 2;
            plot(ax, x_unstable_left(idx_valid_left), y_unstable_left(idx_valid_left), 'b', 'LineWidth', 2);
            
            % 从鞍点向右
            [x_unstable_right, y_unstable_right] = ode45(@(x, y) alpha * exp(beta * x) + delta, [x_saddle 2], 1e-5, odeset('RelTol',1e-8,'AbsTol',1e-10));
            idx_valid_right = y_unstable_right >= -2 & y_unstable_right <= 2;
            plot(ax, x_unstable_right(idx_valid_right), y_unstable_right(idx_valid_right), 'b', 'LineWidth', 2);
        end
        
        % 绘制鞍点
        if ~isnan(x_saddle)
            plot(ax, x_saddle, y_saddle, 'ko', 'MarkerSize', 8, 'DisplayName', 'Saddle Point');
        end
        
        hold(ax, 'off');
    end
end
