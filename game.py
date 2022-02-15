import tkinter
import pygame
import time

gamestart = 0	# ゲームスタートの合図
count = 3

paddleon = 0	# パドルの表示非表示
px=400		# パドルの初期X座標
py=540		# パドルのY座標　※固定値

teki1on = 0		# 敵1の表示非表示
t1x=0		# 敵1の初期X座標
t1y=200		# 敵1の初期Y座標
x_houkou1 = 1	# 敵1の動く方向（左右）
y_houkou1 = 1	# 敵1の動く方向（上下）

teki2on = 0		# 敵2の表示非表示
t2x=500		# 敵1の初期X座標
t2y=0		# 敵1の初期Y座標
x_houkou2 = 1	# 敵2の動く方向（左右）
y_houkou2 = 1	# 敵2の動く方向（上下）

point = 0	# 点数
speed = 10	# 敵1の動くスピード

ojamaon = 0	# お邪魔の表示非表示
ox=400		# お邪魔の初期X座標
oy=300		# お邪魔の初期Y座標
x_houkou3 = 1	# お邪魔の動く方向（左右）
y_houkou3 = 1	# お邪魔の動く方向（上下）

size_x = 800	#敵の動く範囲（X）
size_y = 600	#敵の動く範囲（Y）
max = 0

def teki1move():	# 敵の動きを定義
	global teki1on, t1x, t1y, x_houkou1, y_houkou1, point, speed, size_x, size_y, max
	if gamestart == 1:
		if teki1on == 0:
			canvas.create_image(t1x, t1y, image=img1, tag="TEKI1")
			teki1on = 1
		if t1x-(img1.width()/2) <= 0:
			x_houkou1 =1
		elif t1x >= size_x -(img1.width()/2):
			x_houkou1 = -1

		if t1y-(img1.height()/2) <= max:
			y_houkou1 =1
		elif t1y >=  size_y -(img1.height()/2):
			music1.stop()
			gameover()
			return

		if t2y >= 600-(img1.height()/2):
			return

	if atari(t1x, t1y, img1, img2):
		if y_houkou1 == 1:
			y_houkou1 = -1
			point = point + 1
			lbl1.configure(text = "防いだ回数 "+ str(point))
			sound3.play()

	if teki1on == 1:
		t1x = t1x + 5 * x_houkou1
		t1y = t1y + 5 * y_houkou1

		canvas.coords("TEKI1", t1x, t1y)
		speedup()

	root.after(speed, teki1move)

def teki2move():
	global teki2on, t2x, t2y, x_houkou2, y_houkou2, point, size_x, size_y, max
	if teki2on == 1:
		canvas.delete("FOG")
		canvas.create_image(t2x, t2y, image=img1, tag="TEKI2")
		teki2on = 2
		canvas.create_image(ox, oy, image=img3, tag="FOG")

	if t2x-(img1.width()/2) <= 0:
		x_houkou2 =1
	elif t2x >= size_x -(img1.width()/2):
		x_houkou2 = -1

	if t2y-(img1.height()/2) <= max:
		y_houkou2 =1
	elif t2y >=  size_y -(img1.height()/2):
		music1.stop()
		gameover()
		return

	if t1y >= 600-(img1.height()/2):
		return

	if atari(t2x, t2y, img1, img2):
		if y_houkou2 == 1:
			y_houkou2 = -1
			point = point + 1
			lbl1.configure(text = "防いだ回数 "+ str(point))
			sound3.play()

	if teki2on == 2:
		t2x = t2x + 5 * x_houkou2
		t2y = t2y + 5 * y_houkou2

		canvas.coords("TEKI2", t2x, t2y)
	root.after(10, teki2move)

def speedup():		# 敵のスピードと移動範囲を定義
	global point, speed, size_x, size_y, teki2on, max
	if point < 10:
		speed = 10
	else:
		speed = 7

	if point == 30:
		if teki2on == 0:
			teki2on = 1

	if point >= 40:
		max = -300
		speed = 5

def padmove(event):	# パドルの動きを定義
	global gamestart,paddleon, px, py, t1y, t2y
	if gamestart == 1:
		if paddleon == 0:
			canvas.create_image(px, py, image=img2, tag="PAD")
			paddleon = 1

	if t1y >= 600-(img1.height()/2):
		return
	if t2y >= 600-(img1.height()/2):
		return
	px = event.x
	canvas.coords("PAD",px,py)

def atari(X, Y, imgA, imgB):	# 当たり判定を定義
	global px, py
	cxl = X - imgA.width()/2
	cxr = X + imgA.width()/2
	cyt = Y - imgA.height()/2
	cyb = Y + imgA.height()/2

	pxl = px - imgB.width()/2
	pxr = px + imgB.width()/2
	pyt = py - imgB.height()/2
	pyb = py + imgB.height()/2

	if cxr>pxl:
		if cxl<pxr:
			if cyb>pyt:
				if cyt<pyb:
					return True
	return False

def ojamamove():	# お邪魔の動きを定義
	global t1y, t2y, point, ojamaon, ox, oy, x_houkou3, y_houkou3
	if point >= 20:
		if ojamaon == 0:
			canvas.create_image(ox, oy, image=img3, tag="FOG")
			ojamaon = 1
		if ox-(img3.width()/2) <= -300:
			x_houkou3 =1
		elif ox >= 1100-(img3.width()/2):
			x_houkou3 = -1

		if oy-(img3.height()/2) <= -300:
			y_houkou3 =1
		elif oy >= 900-(img3.height()/2):
			y_houkou3 = -1

		if t1y >= 600-(img1.height()/2):
			return
		if t2y >= 600-(img1.height()/2):
			return

	if ojamaon == 1:
		ox = ox + 5 * x_houkou3
		oy = oy + 5 * y_houkou3
		canvas.coords("FOG", ox, oy)

	root.after(20, ojamamove)

def op():
	music1.play(-1)
	canvas.create_image(400, 300, image=img0, tag="BG1")		# 背景表示
	btn1.place(anchor=tkinter.N, x=300, y=350)
	btn3.place(anchor=tkinter.N, x=500, y=350)

def btn1clk():
	pygame.mixer.music.stop()# music1を止める
	countdown()

def countdown():
	global count, gamestart, point
	if count == 3:
		canvas.create_image(400, 300, image=img01, tag="BG2")		# 背景表示
		canvas.delete("BG1")
		btn1.place_forget()
		btn3.place_forget()
		sound1.play()
		canvas.create_text(400, 300, text="3", font=("MS明朝", "50"), tag="CD", fill="#eaf4fc")
		count = 2
		root.after(1000, countdown)
	elif count == 2:
		sound1.play()
		canvas.delete("BG1")
		canvas.delete("CD")
		canvas.create_text(400, 300, text="2", font=("MS明朝", "50"), tag="CD", fill="#eaf4fc")
		count = 1
		root.after(1000, countdown)
	elif count == 1:
		sound1.play()
		canvas.delete("CD")
		canvas.create_text(400, 300, text="1", font=("MS明朝", "50"), tag="CD", fill="#eaf4fc")
		count = 0
		root.after(1000, countdown)
	elif count ==0:
		sound2.play()
		canvas.delete("CD")
		canvas.create_text(400, 300, text="開始", font=("MS明朝", "50"), tag="CD", fill="#eaf4fc")
		count =-1
		root.after(1000, countdown)
	else:
		canvas.delete("CD")
		music2 = pygame.mixer.music
		music2.load("game.ogg")
		music2.set_volume(0.5)
		music2.play(-1)
		lbl1.place(x=0, y=0)
		lbl1.configure(text = "防いだ回数 "+ str(point))

		teki1move()
		teki2move()
		ojamamove()
		canvas.bind('<Motion>', padmove)
		gamestart = 1

def gameover():
	global point
	lbl3.configure(text = point)
	lbl2.place(anchor=tkinter.N, x=400, y=100)
	lbl3.place(anchor=tkinter.N, x=400, y=200)
	btn2.place(anchor=tkinter.N, x=300, y=350)
	btn3.place(anchor=tkinter.N, x=500, y=350)

	if point<10:
		lbl4.configure(text = "まだまだ修行が足りないようだ…")
	elif point>=10 and point<20:
		lbl4.configure(text = "少しは時間が稼げたか…！")
	elif point>=20 and point<30:
		lbl4.configure(text = "そこそこ時間稼ぎができたぞ…！")
	elif point>=30 and point<40:
		lbl4.configure(text = "かなり時間が稼げた！")
	elif point>=40 and point<50:
		lbl4.configure(text = "民草は全員逃げ延びた！おめでとう！")
	else:
		lbl4.configure(text = "民草が遠くまで離れる時間も稼げた！そなたは最高の陰陽師だ！")

	lbl4.place(anchor=tkinter.N, x=400, y=300)
	lbl5.place(anchor=tkinter.N, x=400, y=500)

def btn2clk():
	global gamestart, count, paddleon, px, py, teki1on, t1x, t1y, x_houkou1, y_houkou1, teki2on, t2x, t2y, x_houkou2, y_houkou2, point, speed, ojamaon, ox, oy, x_houkou3, y_houkou3, size_x, size_y, max
	gamestart = 0
	count = 3
	paddleon = 0
	px=400
	py=540
	teki1on = 0
	t1x=0
	t1y=200
	x_houkou1 = 1
	y_houkou1 = 1
	teki2on = 0
	t2x=500
	t2y=0
	x_houkou2 = 1
	y_houkou2 = 1
	point = 0
	speed = 10
	ojamaon = 0
	ox=400
	oy=300
	x_houkou3 = 1
	y_houkou3 = 1
	size_x = 800
	size_y = 600
	max = 0

	canvas.delete("TEKI1")
	canvas.delete("TEKI2")
	canvas.delete("FOG")
	canvas.delete("PAD")
	lbl1.place_forget()
	lbl2.place_forget()
	lbl3.place_forget()
	lbl4.place_forget()
	lbl5.place_forget()
	btn2.place_forget()
	btn3.place_forget()
	canvas.delete("BG2")

	music1.load("op.ogg")
	music1.set_volume(0.5)
	op()

def btn3clk():
	exit()


root = tkinter.Tk()					# メインのプログラム
root.title(u"陰陽師 -何故此の邪気は之程跳ねるのじゃ-")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

img0 = tkinter.PhotoImage(file = "background1.png")		# 画像の読み込み
img01 = tkinter.PhotoImage(file = "background2.png")
img1 = tkinter.PhotoImage(file = "jaki.png")
img1 = img1.subsample(8)
img2 = tkinter.PhotoImage(file = "ofuda.png")
img2 = img2.subsample(5)
img3 = tkinter.PhotoImage(file = "fog.png")
img3 = img3.subsample(2)

lbl1 = tkinter.Label(root, text="防いだ回数 "+ str(point), font=("MS明朝", "20"), fg="#eaf4fc", bg="#302833")	# 得点の生成
lbl2 = tkinter.Label(root, text="そなたの得点", font=("MS明朝", "50"), fg="#eaf4fc", bg="#302833")
lbl3 = tkinter.Label(root, text=point, font=("MS明朝", "50"), fg="#eaf4fc", bg="#302833")
lbl4 = tkinter.Label(root, text="結果", font=("MS明朝", "20"), fg="#eaf4fc", bg="#302833")
lbl5 = tkinter.Label(root, text="1424191268 村田りか\n画像・イラスト：unsplash 様、イラストAC 様、ぱくたそ 様\n音楽・効果音：おとわび 様、効果音ラボ 様、無料効果音で遊ぼう 様", font=("MS明朝", "10"), fg="#eaf4fc", bg="#302833")

btn1 = tkinter.Button(root, text="開始", font=("MS明朝", "20", "bold"), width=10, bg="#a0d8ef", command=btn1clk)
btn2 = tkinter.Button(root, text="再挑戦", font=("MS明朝", "20", "bold"), width=10, bg="#a0d8ef", command=btn2clk)
btn3 = tkinter.Button(root, text="終了", font=("MS明朝", "20", "bold"), width=10, bg="#a0d8ef", command=btn3clk)


pygame.init()						# 音のロードと再生
sound1 = pygame.mixer.Sound("ready.ogg")
sound2 = pygame.mixer.Sound("start.ogg")
sound3 = pygame.mixer.Sound("hit.ogg")

music1 = pygame.mixer.music
music1.load("op.ogg")
music1.set_volume(0.5)

op()


root.mainloop()
