function dydt = ode_geodesic_RN(t, y, M, Q)
    % y = [t, r, theta, phi, pt, pr, ptheta, pphi]'
    % 这是一个一阶微分方程组，用于 ode45
    
    % 提取坐标和动量
    r = y(2); theta = y(3);
    pt = y(5); pr = y(6); pth = y(7); pphi = y(8);
    
    % 几何因子及其导数
    f = 1 - 2*M/r + Q^2/r^2;
    df_dr = 2*M/r^2 - 2*Q^2/r^3;
    
    % --- 哈密顿方程 ---
    % 1. dx/dlambda = dH/dp (速度)
    dt_dlam = -pt / f;       % g^tt = -1/f
    dr_dlam = pr * f;        % g^rr = f
    dth_dlam = pth / r^2;    % g^thth = 1/r^2
    dphi_dlam = pphi / (r^2 * sin(theta)^2); % g^phiphi
    
    % 2. dp/dlambda = -dH/dx (力/曲率)
    % dpt_dlam = 0; (因为度规不含 t，能量守恒)
    dpt_dlam = 0;
    
    % dpr_dlam = -dH/dr
    % H = -0.5*pt^2/f + 0.5*pr^2*f + ...
    term1 = 0.5 * pt^2 * (df_dr / f^2); % d(-1/f)/dr = 1/f^2 * f'
    term2 = -0.5 * pr^2 * df_dr;
    term3 = pth^2 / r^3;                % d(1/2r^2)/dr = -1/r^3
    term4 = pphi^2 / (r^3 * sin(theta)^2);
    dpr_dlam = term1 + term2 + term3 + term4;
    
    % dpth_dlam = -dH/dtheta
    % 只与最后一项有关: 0.5 * pphi^2 / (r^2 * sin(theta)^2)
    % d(1/sin^2)/dth = -2*cos/sin^3
    dpth_dlam = pphi^2 * cos(theta) / (r^2 * sin(theta)^3);
    
    % dpphi_dlam = 0; (轴对称，角动量守恒)
    dpphi_dlam = 0;
    
    % 输出
    dydt = [dt_dlam; dr_dlam; dth_dlam; dphi_dlam; ...
            dpt_dlam; dpr_dlam; dpth_dlam; dpphi_dlam];
end