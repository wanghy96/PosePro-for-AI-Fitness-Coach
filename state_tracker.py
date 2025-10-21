import time

class StateTracker:
    def __init__(self, complete_state_sequence, inactive_thresh):
        self.complete_state_sequence = complete_state_sequence
        self.begin_state = complete_state_sequence[0]
        self.end_state = complete_state_sequence[len(complete_state_sequence) - 1]
        self.end_state_thresh = complete_state_sequence.count(self.end_state)
        self.state_trans_pairs = []
        temp_pair = []
        for state in complete_state_sequence:
            temp_pair.append(state)
            if len(temp_pair) == 2:
                self.state_trans_pairs.append(temp_pair)
                temp_pair = [state]

        self.inactive_thresh = inactive_thresh

        self.state_seq = []
        self.curr_state = None
        self.prev_state = None

        self.start_inactive_time = time.perf_counter()
        self.inactive_long = 0.0 # INACTIVE_TIME

        self.incorrect_posture = False

        self.squat_count = 0 # SQUAT_COUNT
        self.improper_squat = 0 # IMPROPER_SQUAT

    def set_state(self, state):
        self.curr_state = state
        if self.curr_state == self.prev_state:
            return

        idx = len(self.state_seq)
        if idx >= len(self.complete_state_sequence):
            return

        if idx == 0 and state != self.begin_state:
            return

        # for pair in self.state_trans_pairs:
        #     if pair[0] == self.prev_state and pair[1] == self.curr_state:
        #         self.state_seq.append(state)
        #         break
        self.state_seq.append(state)
        self.__reset_inactive_tracker__()
        # print(">>state seq: ", self.state_seq)

    def get_state(self):
        return self.curr_state

    def get_state_count(self, state):
        return self.state_seq.count(state)

    def reset_state(self):
        self.state_seq = []
        self.curr_state = None
        self.prev_state = None
        self.incorrect_posture = False

    def set_incorrect_posture(self):
        self.incorrect_posture = True

    def before_process(self):
        if self.curr_state is not None:
            self.prev_state = self.curr_state
        self.curr_state = None

    def after_process(self, frame_instance):
        display_inactivity = False
        end_time = 0.0

        if self.curr_state is None or self.curr_state == self.prev_state:
            end_time = time.perf_counter()
            self.inactive_long += end_time - self.start_inactive_time
            self.start_inactive_time = end_time
            if self.inactive_long >= self.inactive_thresh:
                self.squat_count = 0
                self.improper_squat = 0
                frame_instance.put_text(
                    text='Resetting SQUAT_COUNT due to inactivity!!!',
                    pos=(10, frame_instance.get_frame_height() - 25),
                    font_scale=0.7,
                    color='blue',
                    thickness=2)
                display_inactivity = True
        else:
            isfull = len(self.state_seq) == len(self.complete_state_sequence)
            end_state_cnt = self.state_seq.count(self.end_state)
            checked_end_state = self.curr_state == self.end_state and end_state_cnt >= self.end_state_thresh
            if self.complete_state_sequence == self.state_seq:
                if self.incorrect_posture:
                    self.improper_squat += 1
                else:
                    self.squat_count += 1
                self.reset_state()
            elif isfull:
                if self.curr_state == self.end_state:
                    self.improper_squat += 1
                self.reset_state()
            elif checked_end_state:
                self.improper_squat += 1
                self.reset_state()

        frame_instance.draw_text(
                text="正确: " + str(self.squat_count),
                pos=(int(frame_instance.get_frame_width() * 0.82), 30),
                text_color=(255, 255, 230),
                font_scale=0.7,
                bg_color=(18, 185, 0)
            )

        frame_instance.draw_text(
                text="错误: " + str(self.improper_squat),
                pos=(int(frame_instance.get_frame_width() * 0.82), 80),
                text_color=(255, 255, 230),
                font_scale=0.7,
                bg_color=(221, 0, 0)
            )

        if display_inactivity:
            self.__reset_inactive_tracker__()

    def reset(self):
        self.state_seq = []
        self.curr_state = None
        self.prev_state = None

        self.start_inactive_time = time.perf_counter()
        self.inactive_long = 0.0 # INACTIVE_TIME

        self.incorrect_posture = False

        self.squat_count = 0 # SQUAT_COUNT
        self.improper_squat = 0 # IMPROPER_SQUAT

    def __reset_inactive_tracker__(self):
        self.start_inactive_time = time.perf_counter()
        self.inactive_long = 0.0
