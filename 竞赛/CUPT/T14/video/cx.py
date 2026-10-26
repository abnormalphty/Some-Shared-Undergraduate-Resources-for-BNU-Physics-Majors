import folium
import requests

# 高德地图 API 密钥
api_key = "YOUR_AMAP_KEY"

# 预先确定的无线电台位置（可以手动设置）
radio_stations = [
    {"name": "台站1", "address": "重庆市渝北区万科森林公园林璟", "radius": 500000},
    {"name": "台站2", "address": "重庆市开州区水利佳苑", "radius": 750000},
    {"name": "台站3", "address": "北京师范大学", "radius": 650000}
]

# 初始化地图对象
m = folium.Map(location=[35.8617, 104.1954], zoom_start=5)

def add_radio_station_to_map(station):
    """根据无线电台的地址，将其添加到地图上"""
    address = station["address"]
    radius = station["radius"]

    # 获取地址的经纬度
    url = f"https://restapi.amap.com/v3/geocode/geo?address={address}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["geocodes"]:
        location = data["geocodes"][0]["location"].split(",")
        lat = float(location[1])
        lng = float(location[0])

        # 在地图上添加标记
        folium.Marker(
            location=[lat, lng],
            popup=f"{station['name']} ({address})",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(m)

        # 在地图上添加信号覆盖范围
        folium.Circle(
            location=[lat, lng],
            radius=radius,
            color="blue",
            fill=True,
            fill_color="#30f",
            fill_opacity=0.3,
        ).add_to(m)
    else:
        print(f"未找到地址: {address}")

# 将预设的无线电台添加到地图上
for station in radio_stations:
    add_radio_station_to_map(station)

# 保存地图为 HTML 文件
m.save('radio_station_map.html')

# 提示信息
print("包含无线电台位置和信号覆盖范围的地图已生成并保存为 radio_station_map.html")
