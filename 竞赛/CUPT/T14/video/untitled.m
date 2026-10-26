% 导入视频
video = VideoReader('1.mp4');

% 获取视频信息
numFrames = video.NumFrames;
frameRate = video.FrameRate;

% 初始化变量
objectCentroid = zeros(numFrames, 2); % 存储弹性体的质心
objectOrientation = zeros(numFrames, 1); % 存储弹性体的方向
objectAxes = zeros(numFrames, 2); % 存储弹性体的长轴和短轴

% 手动设置阈值，可能需要根据实际情况调整
threshold = 100; % 例如，阈值为 100（范围为0到255）

% 创建图形窗口
figure;
axis off; % 隐藏坐标轴

% 定义卷积核（形态学结构元素）
se = ones(5, 5); % 5x5 的结构元素

for k = 1:numFrames
    % 读取当前帧
    frame = read(video, k);
    
    % 转换为灰度图像
    grayFrame = rgb2gray(frame);
    
    % 手动二值化
    binaryFrame = grayFrame > threshold;
    
    % 手动实现开运算
    erodedFrame = imerode(binaryFrame, se);
    openedFrame = imdilate(erodedFrame, se);
    
    % 手动实现闭运算
    dilatedFrame = imdilate(binaryFrame, se);
    closedFrame = imerode(dilatedFrame, se);
    
    % 手动实现连通分量检测
    label = 0;
    labels = zeros(size(closedFrame));
    [rows, cols] = size(closedFrame);
    
    % 遍历图像
    for i = 1:rows
        for j = 1:cols
            if closedFrame(i, j) == 1 && labels(i, j) == 0
                % 新的连通分量
                label = label + 1;
                queue = [i, j];
                labels(i, j) = label;
                
                % 广度优先搜索 (BFS) 标记连通分量
                while ~isempty(queue)
                    [x, y] = deal(queue(1, 1), queue(1, 2));
                    queue(1, :) = []; % 出队
                    
                    % 检查邻居像素
                    for dx = -1:1
                        for dy = -1:1
                            nx = x + dx;
                            ny = y + dy;
                            if nx > 0 && nx <= rows && ny > 0 && ny <= cols
                                if closedFrame(nx, ny) == 1 && labels(nx, ny) == 0
                                    labels(nx, ny) = label;
                                    queue = [queue; nx, ny]; % 入队
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    
    % 计算各个连通分量的面积
    numLabels = label;
    areas = zeros(numLabels, 1);
    for l = 1:numLabels
        areas(l) = sum(labels(:) == l);
    end
    
    if numLabels > 0
        [~, idx] = max(areas); % 找到面积最大的连通分量
        
        % 提取最大连通分量的质心、方向和形状特征
        [rowIdx, colIdx] = find(labels == idx);
        centroidX = mean(colIdx);
        centroidY = mean(rowIdx);
        
        % 使用最小二乘法拟合直线，得到弹性体的方向
        coeffs = polyfit(colIdx, rowIdx, 1);
        orientation = atan(coeffs(1)); % 计算直线的斜率
        
        % 计算主轴和次轴
        majorAxis = max(colIdx) - min(colIdx);
        minorAxis = max(rowIdx) - min(rowIdx);
        
        % 存储质心、方向和轴长
        objectCentroid(k, :) = [centroidX, centroidY];
        objectOrientation(k) = orientation * 180 / pi; % 转换为度数
        objectAxes(k, :) = [majorAxis, minorAxis];
        
        % 显示当前帧
        imshow(frame); % 显示图像
        hold on;
        
        % 在图像上标记质心
        plot(centroidX, centroidY, 'ro', 'MarkerSize', 10, 'LineWidth', 2);
        
        % 绘制弹性体的长轴方向
        quiver(centroidX, centroidY, majorAxis/2 * cosd(objectOrientation(k)), majorAxis/2 * sind(objectOrientation(k)), 'g', 'LineWidth', 2);
        quiver(centroidX, centroidY, -majorAxis/2 * cosd(objectOrientation(k)), -majorAxis/2 * sind(objectOrientation(k)), 'g', 'LineWidth', 2);
        
        hold off;
        
        % 暂停以控制播放速度
        pause(1 / frameRate);
    end
end

% 绘制质心、方向和形变随时间的变化
figure;
subplot(3, 1, 1);
plot(objectCentroid(:, 1), objectCentroid(:, 2), 'b');
xlabel('X Position');
ylabel('Y Position');
title('Elastic Body Centroid (Trajectory)');

subplot(3, 1, 2);
plot(objectOrientation, 'r');
xlabel('Frame');
ylabel('Orientation (degrees)');
title('Elastic Body Orientation');

subplot(3, 1, 3);
plot(objectAxes(:, 1), 'g');
hold on;
plot(objectAxes(:, 2), 'm');
xlabel('Frame');
ylabel('Axis Length');
legend('Major Axis', 'Minor Axis');
title('Elastic Body Shape Deformation');

% 自定义卷积函数，用于形态学操作
function output = imerode(input, se)
    [rows, cols] = size(input);
    [seRows, seCols] = size(se);
    padSize = [floor(seRows/2), floor(seCols/2)];
    paddedInput = zeros(rows + 2 * padSize(1), cols + 2 * padSize(2));
    paddedInput(padSize(1)+1:padSize(1)+rows, padSize(2)+1:padSize(2)+cols) = input;
    output = zeros(rows, cols);
    
    for r = 1:rows
        for c = 1:cols
            region = paddedInput(r:r+seRows-1, c:c+seCols-1);
            output(r, c) = min(region(se == 1));
        end
    end
end

function output = imdilate(input, se)
    [rows, cols] = size(input);
    [seRows, seCols] = size(se);
    padSize = [floor(seRows/2), floor(seCols/2)];
    paddedInput = zeros(rows + 2 * padSize(1), cols + 2 * padSize(2));
    paddedInput(padSize(1)+1:padSize(1)+rows, padSize(2)+1:padSize(2)+cols) = input;
    output = zeros(rows, cols);
    
    for r = 1:rows
        for c = 1:cols
            region = paddedInput(r:r+seRows-1, c:c+seCols-1);
            output(r, c) = max(region(se == 1));
        end
    end
end
