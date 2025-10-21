from frame_instance import FrameInstance
from state_tracker import StateTracker
import simpleaudio as sa
import threading

# 全局变量，用于跟踪音频的播放状态
is_playing = False

def play_sound(sound_file):
    global is_playing
    wave_obj = sa.WaveObject.from_wave_file(f"{sound_file}.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    is_playing = False  # 音频播放完成，更新状态

# 完成一个动作的状态序列
COMPLETE_STATE_SEQUENCE = ['s1', 's2', 's3', 's2', 's1']

# 未活动监测的时长阈值，单位秒
INACTIVE_THRESH = 60.0

def trainer_process(frame_instance, state_tracker, frame_width, frame_height):
    global is_playing
    angle_shldr_nose = frame_instance.get_angle('left_shldr', 'nose', 'right_shldr')

    if angle_shldr_nose > 35:
        # 当前没有音频正在播放
        if not is_playing:
            is_playing = True  # 标记音频播放
            sound_thread = threading.Thread(target=play_sound, args=("reset_counters",))  # args中参数为播放音乐名，音乐为wav格式
            sound_thread.start()
        # 朝向正面，重置状态
        state_tracker.reset_state()
        # 画点
        frame_instance.circle('left_shldr', 'nose', 'right_shldr', radius=7, color='yellow')
        # ####################################### 如果朝向正面，提示角度错误 ####################################
        frame_instance.draw_text(
            text='请正对屏幕站立',
            pos=(40, frame_height - 90),
            text_color=(0, 255, 230),
            font_scale=0.65,
            bg_color=(255, 153, 0),
        )
        frame_instance.draw_text(
            text='当前偏斜角度: ' + str(angle_shldr_nose-35),
            pos=(40, frame_height - 40),
            text_color=(255, 255, 230),
            font_scale=0.65,
            bg_color=(255, 153, 0),
        )
    else:
        # 朝向侧面。可以进行深蹲监测

        # region 判断状态
        # 获取需要监测的角度
        # draw_and_get_angle_vertical(): 计算并画出两点与垂线的夹角
        knee_vertical_angle = frame_instance.get_angle_and_draw('hip', 'knee', 'vertical')
        knee_angle = int(knee_vertical_angle)
        # 判断当前状态
        if 0 <= knee_angle <= 32:
            # 臀膝角度在0~32之间是s1状态
            state_tracker.set_state('s1')
        elif 35 <= knee_angle <= 65:
            # 臀膝角度在35~65之间是s2状态
            state_tracker.set_state('s2')
        elif 70 <= knee_angle <= 95:
            # 臀膝角度在70~95之间是s3状态
            state_tracker.set_state('s3')
        # endregion

        # region 画点画线
        # line(): 画出两点之间的连线
        frame_instance.line('shldr', 'elbow', 'light_blue', 4)
        frame_instance.line('wrist', 'elbow', 'light_blue', 4)
        frame_instance.line('ankle', 'foot', 'light_blue', 4)
        # point()：画点
        frame_instance.circle('elbow', 'wrist', 'foot', radius=7, color='yellow')

        knee_vertical_angle = frame_instance.get_angle_and_draw('hip', 'knee', 'vertical')
        hip_vertical_angle = frame_instance.get_angle_and_draw('shldr', 'hip', 'vertical')
        ankle_vertical_angle = frame_instance.get_angle_and_draw('knee', 'ankle', 'vertical')

        # ####################################### 判断前倾或后仰，并提示 #######################################
        if hip_vertical_angle > 50:
            frame_instance.show_feedback(text='身体向后仰', y=215, text_color='light_yellow', bg_color='blue')
        elif hip_vertical_angle < 10 and state_tracker.get_state_count('s2') == 1:
            frame_instance.show_feedback(text='身体向前倾', y=215, text_color='light_yellow', bg_color='blue')

        # ####################################### 下蹲深度提示 ###############################################
        if 50 < knee_vertical_angle < 70 and state_tracker.get_state_count('s2') == 1:
            # 提示蹲的深度不够
            frame_instance.show_feedback(text='请继续下蹲', y=80, text_color='black', bg_color='yellow')
        elif knee_vertical_angle > 95:
            # 提示蹲的过深
            frame_instance.show_feedback(text='蹲的太深了', y=125, text_color='light_yellow', bg_color='red')
            # 标记“不正确的姿势”
            state_tracker.set_incorrect_posture()

        # ####################################### 膝盖位置提示 #################################################
        if ankle_vertical_angle > 45:
            # 提示膝盖过脚尖
            frame_instance.show_feedback(text='膝盖超过了脚尖', y=170, text_color='light_yellow', bg_color='yellow')
            # 标记“不正确的姿势”
            state_tracker.set_incorrect_posture()

        # endregion

