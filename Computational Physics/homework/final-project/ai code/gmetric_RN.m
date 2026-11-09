function [g_down, g_up] = gmetric_RN(r, theta, M, Q)
    % Reissner-Nordstrom Metric (包含 Schwarzschild 当 Q=0 时)
    % M: 质量, Q: 电荷
    
    % 几何因子 f(r)
    f = 1 - 2*M/r + Q^2/r^2;
    
    % 下标度规 g_{mu,nu} (对角矩阵，很简单)
    % 坐标顺序: t, r, theta, phi
    g_down = diag([-f, 1/f, r^2, r^2*sin(theta)^2]);
    
    % 上标度规 g^{mu,nu} (也就是 g_down 的逆矩阵)
    g_up = diag([-1/f, f, 1/r^2, 1/(r^2*sin(theta)^2)]);
end