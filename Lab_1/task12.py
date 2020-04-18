signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_frames(signal, size, overlap):
	size = size * overlap
	start = 0
	end = int(size)
	while end <= len(signal):
		frame = signal[start:end]
		yield frame
		start += int(size)
		end += int(size)


for frame in get_frames(signal, size=8, overlap=0.5):
	print(frame)