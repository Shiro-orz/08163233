import tkinter as tk


class chess:
    def __init__(self):
        board = tk.Tk()
        board.title('chessboard')
        self.mark = 0
        self.board_canvas = tk.Canvas(board, bg='white', width=512, height=512)
        self.board_canvas.grid(row=0, column=0, columnspan=512, rowspan=512)
        self.board_set = tk.Button(
            board, text='设置边长', width=10, command=self.chessboard_set)
        self.set = tk.Button(
            board, text='设置特殊点', width=10, command=self.specialpoint_set)
        self.input_size = tk.Entry(board, width=10)
        self.input_x = tk.Entry(board, width=10)
        self.input_y = tk.Entry(board, width=10)
        self.process = tk.Button(
            board, text='演示', width=10, command=self.fill_color)
        self.la_1 = tk.Label(board, text='输入边长，为2^k并且小于512：')
        self.la_2 = tk.Label(board, text='输入特殊点坐标：')

        self.la_1.grid(row=200, column=520, columnspan=20)
        self.input_size.grid(row=201, column=520)
        self.board_set.grid(row=201, column=540)
        self.la_2.grid(row=202, column=520)
        self.input_x.grid(row=203, column=520)
        self.input_y.grid(row=203, column=530)
        self.set.grid(row=203, column=540)
        self.process.grid(row=204, column=540)
        board.mainloop()

    def chessboard_set(self):
        num = int(self.input_size.get())
        single_len = 512 // num
        for i in range(0, num):
            for j in range(0, num):
                self.board_canvas.create_rectangle(
                    j * single_len, i * single_len,
                    j * single_len + single_len, i * single_len + single_len)
        self.board_canvas.grid()

    def specialpoint_set(self):
        num = int(self.input_size.get())
        single_len = 512 // num
        point_x = int(self.input_x.get())
        point_y = int(self.input_y.get())
        s_point = self.board_canvas.create_rectangle(
            point_x * single_len, point_y * single_len,
            point_x * single_len + single_len,
            point_y * single_len + single_len)
        self.board_canvas.itemconfig(s_point, fill='black')
        self.board_canvas.grid()

    def fill_color(self):
        num = int(self.input_size.get())
        point_x = int(self.input_x.get())
        point_y = int(self.input_y.get())
        self.arrange(0, 0, point_x, point_y, num)

    def arrange(self, tx, ty, px, py, size):
        global mark
        self.mark += 1
        count = self.mark
        if size == 1:
            return
        half = size // 2

        if px < tx + half and py < ty + half:
            self.arrange(tx, ty, px, py, half)
        else:
            self.arrange(tx, ty, tx + half - 1, ty + half - 1, half)
            self.colored(tx + half - 1, ty + half - 1, count)

        if px < tx + half and py >= ty + half:
            self.arrange(tx, ty + half, px, py, half)
        else:
            self.arrange(tx, ty + half, tx + half - 1, ty + half, half)
            self.colored(tx + half - 1, ty + half, count)

        if px >= tx + half and py < ty + half:
            self.arrange(tx + half, ty, px, py, half)
        else:
            self.arrange(tx + half, ty, tx + half, ty + half - 1, half)
            self.colored(tx + half, ty + half - 1, count)

        if px >= tx + half and py >= ty + half:
            self.arrange(tx + half, ty + half, px, py, half)
        else:
            self.arrange(tx + half, ty + half, tx + half, ty + half, half)
            self.colored(tx + half, ty + half, count)

    def colored(self, px, py, count):
        colors = [
            '#FF9966',
            '#0066CC',
            '#FF9900',
            '#FFFFCC',
            '#FF6666',
            '#99CC33',
            '#33CC99',
            '#800080',
            '#FFB11B',
            '#D2B48C',
            '#87CEEB',
            '#A52A2A',
            '#A9A9A9',
            '#DC143C',
            '#98FB98',
        ]
        select = int(count % 15)
        num = int(self.input_size.get())
        single_len = 512 // num
        point = self.board_canvas.create_rectangle(
            px * single_len, py * single_len, px * single_len + single_len,
            py * single_len + single_len)
        self.board_canvas.itemconfig(point, fill=colors[select])
        self.board_canvas.grid()


chess_board = chess()
chess_board.__init__()