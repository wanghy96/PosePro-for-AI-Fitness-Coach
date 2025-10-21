# 1. 方法说明

## 1.1. get_coord【获取坐标】

### 1.1.1. 方法原型

```python
def get_coord(feature)
```

### 1.1.2. 参数


| 参数名  | 说明                                         |
| ------- | -------------------------------------------- |
| feature | 标识点名称。（见[身体标识点](#features)） |

### 1.1.4. 返回值

get_coord方法返回一个表示坐标的数值数组。数组的第0个元素表示x坐标，第1个元素表示y坐标。

### 1.1.5. 示例

```python
coord = frame_instance.get_coord('nose')
x = coord[0] # x坐标
y = coord[1] # y坐标
```

## 1.2. get_orientation【获取朝向】

### 1.2.1. 方法原型

```python
def get_orientation()
```

### 1.2.2. 参数

无

### 1.2.4. 返回值

get_orientation方法返回一个表示朝向的字符串。字符串的值可能是：front, left, right。

### 1.2.5. 备注

这个方法是通过检测鼻和两肩的夹角来计算的。夹角大于35度，识别为朝向镜头（或背向镜头）。小于35度，识别为朝向侧面，这种情况下会判断肩和脚的距离来识别左右。

### 1.2.6. 示例

```python
orientation = frame_instance.get_orientation()
```

## 1.3. get_angle【计算角度】

### 1.3.1. 方法原型

```python
def get_angle(point1, point2, point3)
```

### 1.3.2. 参数


| 参数名 | 说明                                                                                                        |
| ------ |-----------------------------------------------------------------------------------------------------------|
| point1 | 标识点名称1。（见[身体标识点](#features)）                                                                           |
| point2 | 标识点名称2。（见[身体标识点](#features)）                                                                           |
| point3 | 标识点名称3。取值：<br>标识点名称（见[身体标识点](#features)）；<br>'vertical'（point2的垂线上的点）；<br>'horizontal'（point2的水平线上的点）； |

### 1.3.4. 返回值

返回一个整数值，表示三点的夹角。

### 1.3.5. 示例

计算肩部、臀部、臀部垂直线上的角度：
![本地路径](img/get_angle2.jpg "肩部、臀部、臀部垂直线上的角度")
```python
angle = frame_instance.get_angle('shldr', 'hip', 'vertical')
```
## 1.4. get_angle_and_draw【计算角度并画点画线】

### 1.4.1. 方法原型
```python
def get_angle_and_draw(
        point1, 
        point2, 
        point3, 
        text_color='light_green', 
        line_color='light_blue', 
        point_color='yellow', 
        ellipse_color='white', 
        dotted_line_color='blue'
)
```
### 1.4.2. 参数
| 参数名               | 说明                                                                                                        | 默认值           |
|-------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| point1            | 标识点名称1。（见[身体标识点](#features)）                                                                              |               |
| point2            | 标识点名称2。（见[身体标识点](#features)）                                                                              |               |
| point3            | 标识点名称3。取值：<br/>标识点名称（见[身体标识点](#features)）；<br/>'vertical'（point2的垂线上的点）；<br/>'horizontal'（point2的水平线上的点）； |               |
| text_color        | 字符颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)                               | 'light_green' |
| line_color        | 连线颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)                               | 'light_blue'  |
| point_color       | 点的颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)                               | 'yellow'      |
| ellipse_color     | 角弧颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)                               | 'white'       |
| dotted_line_color | 垂直线或水平线颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)                          | 'blue'        |
### 1.4.4. 返回值
返回一个整数值，表示三点的夹角。
### 1.4.5. 示例

计算肩部、臀部、臀部垂直线上的角度，并画线画点：
![本地路径](img/get_angle2.jpg "肩部、臀部、臀部垂直线上的角度")
```python
angle = frame_instance.get_angle_and_draw('shldr', 'hip', 'vertical')
```

## 1.5. circle【画点】

### 1.5.1. 方法原型
```python
def circle(*args, radius=7, color='yellow')
```
### 1.5.2. 参数
| 参数名    | 说明                                                                          | 默认值      |
|--------|-----------------------------------------------------------------------------|----------|
| *args  | 标识点名称。（见[身体标识点](#features)）<br/>可以一次画多个点。                                   |          |
| radius | 点的半径                                                                        | 7        |
| color  | 点的颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255) | 'yellow' |

### 1.5.4. 返回值
无
### 1.5.5. 示例
画左肩、鼻、右肩的点：
```python
frame_instance.circle('left_shldr', 'nose', 'right_shldr')
```
## 1.6. line【画线】

### 1.6.1. 方法原型
```python
def line(pt1, pt2, color='light_blue', thickness=4)
```
### 1.6.2. 参数
| 参数名   | 说明                                                                          | 默认值      |
|-------|-----------------------------------------------------------------------------|----------|
| pt1   | 标识点名称1。（见[身体标识点](#features)）                                                |          |
| pt2   | 标识点名称2。（见[身体标识点](#features)）                                                | 7        |
| color | 线的颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255) | 'yellow' |

### 1.6.4. 返回值
无
### 1.6.5. 示例
画肩和肘的连线：
```python
frame_instance.line('shldr', 'elbow')
```
## 1.7. draw_text【显示文本（带线框）】

### 1.7.1. 方法原型
```python
def draw_text(
        text, 
        width=8, 
        font=cv2.FONT_HERSHEY_SIMPLEX, 
        pos=(0, 0), 
        font_scale=1.0, 
        font_thickness=2, 
        text_color=(0, 255, 0), 
        bg_color=(0, 0, 0), 
        box_offset=(20, 10)
)
```
### 1.7.2. 参数
| 参数名            | 说明                                                                           | 默认值                      |
|----------------|------------------------------------------------------------------------------|--------------------------|
| text           | 要显示的文本                                                                       |                          |
| width          | 边框圆角的宽度                                                                      | 8                        |
| font           | 字体                                                                           | cv2.FONT_HERSHEY_SIMPLEX |
| pos            | 文本框左上角坐标                                                                     | (0, 0)                   |
| font_scale     | 字体大小                                                                         | 1.0                      |
| font_thickness | 字体粗细                                                                         | 2                        |
| text_color     | 文本框颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255) | (0, 255, 0)              |
| bg_color       | 背景颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)  | (0, 0, 0)                |

### 1.7.4. 返回值
无
### 1.7.5. 示例
显示计数文本

![本地路径](img/draw_text.jpg "显示计数文本")
```python
frame_instance.draw_text(
        text="CORRECT: " + str(squat_count),
        pos=(int(frame_instance.get_frame_width() * 0.68), 30),
        text_color=(255, 255, 230),
        font_scale=0.7,
        bg_color=(18, 185, 0)
    )

frame_instance.draw_text(
        text="INCORRECT: " + str(improper_squat),
        pos=(int(frame_instance.get_frame_width() * 0.68), 80),
        text_color=(255, 255, 230),
        font_scale=0.7,
        bg_color=(221, 0, 0)
    )
```
## 1.8. show_feedback【显示反馈信息】
### 1.8.1. 方法原型
```python
def show_feedback(text, y, text_color, bg_color)
```

### 1.8.2. 参数
| 参数名        | 说明                                                                           | 默认值 |
|------------|------------------------------------------------------------------------------|-----|
| text       | 要显示的文本                                                                       |     |
| y          | 文本的Y坐标                                                                       |     |
| text_color | 文本框颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255) |     |
| bg_color   | 背景颜色。取值：<br/>预定义颜色（见[预定义颜色](#colors)）；<br/>颜色值，格式(R, G, B)，例如：(0, 127, 255)  |     |

### 1.8.4. 返回值
无
### 1.8.5. 示例
显示“LOWER YOUR HIPS”

![本地路径](img/show_feedback.jpg "显示“LOWER YOUR HIPS”")
```python
frame_instance.show_feedback(text='LOWER YOUR HIPS', y=80, text_color='black', bg_color='yellow')
```
### 1.8.6. 备注
反馈信息的X坐标统一为30

# 2. 身体标识点

<a id=features>身体标识点列表</a>


| 标识点        | 含义 | 备注                               |
| ------------- | ---- | ---------------------------------- |
| 'nose'        | 鼻子 |                                    |
| 'left_shldr'  | 左肩 |                                    |
| 'left_elbow'  | 左肘 |                                    |
| 'left_wrist'  | 左腕 |                                    |
| 'left_hip'    | 左臀 |                                    |
| 'left_knee'   | 左膝 |                                    |
| 'left_ankle'  | 左踝 |                                    |
| 'left_foot'   | 左脚 |                                    |
| 'right_shldr' | 右肩 |                                    |
| 'right_elbow' | 右肘 |                                    |
| 'right_wrist' | 右腕 |                                    |
| 'right_hip'   | 右臀 |                                    |
| 'right_knee'  | 右膝 |                                    |
| 'right_ankle' | 右踝 |                                    |
| 'right_foot'  | 右脚 |                                    |
| 'shldr'       | 肩   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'elbow'       | 肘   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'wrist'       | 腕   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'hip'         | 臀   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'knee'        | 膝   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'ankle'       | 踝   | 仅侧向时可用，代表靠近镜头一侧的点 |
| 'foot'        | 脚   | 仅侧向时可用，代表靠近镜头一侧的点 |

# 3. 预定义颜色
<a id=colors>预定义颜色</a>
```
    'black'         : (0, 0, 0),
    'blue'          : (0, 127, 255),
    'red'           : (255, 50, 50),
    'green'         : (0, 255, 127),
    'light_green'   : (100, 233, 127),
    'yellow'        : (255, 255, 0),
    'light_yellow'  : (255, 255, 230),
    'magenta'       : (255, 0, 255),
    'white'         : (255,255,255),
    'cyan'          : (0, 255, 255),
    'light_blue'    : (102, 204, 255)
```
