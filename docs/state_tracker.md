# 1. 方法说明
## 1.1. set_state【设置状态】

### 1.1.1. 方法原型

```python
def set_state(state)
```

### 1.1.2. 参数
| 参数名   | 说明  |
|-------|-----|
| state | 新状态 |

### 1.1.4. 返回值
无
### 1.1.5. 示例
```python
state_tracker.set_state('s1')
```

## 1.2. get_state【获取当前】

### 1.2.1. 方法原型

```python
def get_state()
```

### 1.2.2. 参数
无

### 1.2.4. 返回值
返回当前状态。
### 1.2.5. 示例
```python
state_tracker.set_state('s1')
state = state_tracker.get_state() # state的值是's1'

state_tracker.set_state('s2')
state = state_tracker.get_state() # state的值是's2'
```
## 1.3. get_state_count【获取当前状态序列中，指定状态的数量】

### 1.3.1. 方法原型

```python
def get_state_count(state)
```

### 1.3.2. 参数
| 参数名   | 说明   |
|-------|------|
| state | 指定状态 |

### 1.3.4. 返回值
无
### 1.3.5. 示例
```python
# 假设现在状态已经完成动作的状态序列是['s1', 's2', 's3', 's2']
# 则get_state_count('s2')的返回值是2
cnt = state_tracker.get_state_count('s2')
```

## 1.4. reset_state【清空状态】

### 1.4.1. 方法原型

```python
def reset_state()
```

### 1.4.2. 参数
无
### 1.4.4. 返回值
无
### 1.4.5. 示例
```python
# 调用reset_state后，会重置当前状态为None，并且清空状态序列。
state_tracker.reset_state()
```

## 1.5. set_incorrect_posture【设置错误动作标志】

### 1.5.1. 方法原型

```python
def set_incorrect_posture()
```

### 1.5.2. 参数
无
### 1.5.4. 返回值
无
### 1.5.5. 示例
```python
# 调用set_incorrect_posture后，当前一组动作完成后，会被记到失败次数中。
state_tracker.set_incorrect_posture()
```