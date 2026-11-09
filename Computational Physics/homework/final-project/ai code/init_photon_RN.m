function y0 = init_photon_RN(i, j, npix, fov, pos, M, Q)
    % i, j: 像素坐标
    % npix: 总像素数
    % fov: 视场角
    % pos: 相机位置 [t, r, theta, phi]
    
    % 1. 屏幕坐标 (x, y) 归一化到 [-1, 1] 之间，再根据 fov 缩放
    % 假设相机看着黑洞中心 (r=0)
    screen_scale = 2 * tan(fov/2);
    alpha = screen_scale * (i - npix/2 - 0.5) / npix; % 水平方向
    beta  = screen_scale * (j - npix/2 - 0.5) / npix; % 垂直方向
    
    % 2. 局部动量 k (在相机参考系下)
    % k_r 指向黑洞 (负方向)，k_theta 和 k_phi 对应屏幕的 y 和 x
    % 注意：这里这是近似，对于远离黑洞的观测者适用
    k_r = -1;  
    k_th = -beta / pos(2); % 近似小角度
    k_phi = -alpha / (pos(2) * sin(pos(3))); 
    
    % 归一化光子动量，使得 k_t^2 = k_space^2 (零测地线)
    % g_tt * k_t^2 + g_rr * k_r^2 + ... = 0
    % 在无穷远近似下，我们直接构造初始四维动量
    % 更严谨的做法是用四脚标架，这里简化处理：
    
    [~, g_up] = gmetric_RN(pos(2), pos(3), M, Q);
    
    % 修正：我们要给出的初始条件是协变动量 p_mu (下指标)
    % 假设观测者主要感受到的是径向动量
    p_t = 1; % 能量归一化为 1
    p_th = beta * pos(2);  % 简单的几何投影
    p_phi = alpha * pos(2) * sin(pos(3));
    
    % 利用 H=0 计算 p_r
    % g^tt p_t^2 + g^rr p_r^2 + g^thth p_th^2 + g^phiphi p_phi^2 = 0
    % (-1/f) * 1^2 + f * p_r^2 + ... = 0
    % p_r^2 = (1/f) * [ (1/f) - g^thth p_th^2 - g^phiphi p_phi^2 ] 
    %       = (1/f^2) - (1/f)*(p_th^2/r^2 + ...)
    
    f = 1 - 2*M/pos(2) + Q^2/pos(2)^2;
    term_ang = p_th^2/pos(2)^2 + p_phi^2/(pos(2)^2*sin(pos(3))^2);
    
    % 求解 p_r (取负号，因为光线向内)
    p_r = -sqrt( (1/f^2) * 1^2 - (1/f)*term_ang );
    
    y0 = [pos(1); pos(2); pos(3); pos(4); p_t; p_r; p_th; p_phi];
end