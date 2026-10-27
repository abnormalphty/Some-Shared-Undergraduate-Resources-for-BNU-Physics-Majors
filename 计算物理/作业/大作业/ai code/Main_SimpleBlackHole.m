% === 简单球对称黑洞光线追踪主程序 ===
clear; clc;

% 1. 参数设置
npix = 200;           % 像素分辨率 (想清楚点就设 500)
M = 1;                % 质量
Q = 0;              % 电荷 (Q=0 为 Schwarzschild; Q=0.9 为 RN)
fov = pi/6;           % 视场角
r_obs = 50 * M;       % 观测者距离
theta_obs = 85 * pi/180; % 观测者倾角 (接近赤道面才能看到盘)
pos_cam = [0, r_obs, theta_obs, 0]; 

% 视界半径 (用于判断黑洞阴影)
if M > abs(Q)
    r_horizon = M + sqrt(M^2 - Q^2);
else
    r_horizon = 0; % 裸奇点，哼，别作死去试这个
end

% 图像矩阵初始化
Image = zeros(npix, npix);

fprintf('开始光线追踪... 别眨眼，这可是广义相对论。\n');
fprintf('当前黑洞: M=%g, Q=%g (Horizon r = %.4f)\n', M, Q, r_horizon);

% 2. 开启并行池 (如果没有开启)
if isempty(gcp('nocreate')), parpool; end

tic; % 计时开始

parfor j = 1:npix      % 垂直像素循环
    row_data = zeros(1, npix);
    for i = 1:npix     % 水平像素循环
        
        % A. 获取初始条件
        y0 = init_photon_RN(i, j, npix, fov, pos_cam, M, Q);
        
        % B. 积分设置
        tspan = [0, 500]; % 积分长度
        options = odeset('RelTol', 1e-4, 'AbsTol', 1e-6, 'Events', @(t,y) event_func(t,y,r_horizon));
        
        % C. 执行 ODE 积分
        % 注意：parfor 中不能直接用嵌套函数，event_func 写在最后
        [~, Y, te, ye, ie] = ode45(@(t,y) ode_geodesic_RN(t,y,M,Q), tspan, y0, options);
        
        % D. 上色逻辑 (几何薄盘模型)
        % 默认颜色：黑色 (0)
        pixel_color = 0; 
        
        % 检查事件
        if ~isempty(ie)
            last_event = ie(end);
            if last_event == 1 % 落入视界
                pixel_color = 0; % 纯黑
            elseif last_event == 2 % 逃逸到无穷远 (天空)
                pixel_color = 0.1; % 深灰背景
            end
        end
        
        % 检查是否穿过吸积盘 (Theta = pi/2)
        % 遍历路径点，看 theta 是否跨过 pi/2
        theta_path = Y(:,3);
        % 寻找穿过赤道面的点 (符号改变)
        crossings = find(diff(sign(theta_path - pi/2)) ~= 0);
        
        if ~isempty(crossings)
            % 如果穿过赤道面
            idx = crossings(1); % 取第一次穿过的点
            r_hit = Y(idx, 2);
            
            % 简单的吸积盘纹理：根据半径 r 画环
            if r_hit > r_horizon + 0.5 % 盘必须在视界外
                 if mod(floor(r_hit), 2) == 0
                     pixel_color = 1; % 亮环
                 else
                     pixel_color = 0.6; % 暗环
                 end
            end
            % 如果已经被黑洞捕获，但之前穿过了盘，我们保留盘的颜色(前景)
            % 这里简化处理：只要碰盘就算盘的颜色
        end
        
        row_data(i) = pixel_color;
    end
    Image(j, :) = row_data;
end

toc; % 计时结束

% 3. 绘图
figure;
imagesc(Image);
colormap('hot'); % 用热力图看起来比较像黑洞
axis equal off;
title(sprintf('Black Hole Shadow (M=%g, Q=%g)', M, Q));

% === 辅助函数：事件检测 ===
function [value, isterminal, direction] = event_func(t, y, r_h)
    r = y(2);
    
    % 事件1: 落入视界 (r < 1.01 * r_horizon)
    val1 = r - 1.01 * r_h;
    
    % 事件2: 逃逸 (r > 100)
    val2 = r - 100;
    
    value = [val1; val2];
    isterminal = [1; 1]; % 发生任一事件即停止积分
    direction = [0; 0];
end