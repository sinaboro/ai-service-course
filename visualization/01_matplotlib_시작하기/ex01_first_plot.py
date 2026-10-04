import matplotlib.pyplot as plt          # 관례적으로 plt 라는 별명

x = [1, 2, 3, 4, 5]
y = [3, 7, 4, 9, 6]

plt.plot(x, y)                            # x, y 로 선 그래프
plt.savefig("images/ex01_first_plot.png") # 이미지로 저장
plt.show()                                # 화면에 창으로 보여 주기
