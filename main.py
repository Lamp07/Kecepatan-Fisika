import os
import sys
import time

q = """
[1] Menghitung Jarak Tempuh
[2] Menghitung Kecepatan
[3] Menghitung Waktu
"""

class Rumus:

	def menghitung_jarak(kecepatan, waktu):
		diketahui = """
		Diketahui:
		Kecepatan: {0}km/jam
		Waktu: {1} jam
		""".format(kecepatan, waktu)
		return "{0}\nHasil: {1}km (kilometer)".format(diketahui, int(kecepatan) * int(waktu))

	def menghitung_kecepatan(jarak, waktu):
		diketahui = """
		Diketahui:
		Jarak: {0}m
		Waktu: {1}s
		""".format(jarak, waktu)
		return "{0}\nHasil: {1}m/s (meter/sekon)".format(diketahui, int(jarak) / int(waktu))

	def menghitung_waktu(kecepatan, jarak):
		diketahui = """
		Diketahui:
		Kecepatan: {0}m/s
		Jarak: {1}m
		""".format(kecepatan, jarak)
		return "{0}\nHasil: {1}s (sekon)".format(diketahui, int(jarak) / int(kecepatan))

print(q)
a = int(input("Pilih angka diatas> "))

if a == 1:
	kecepatan = input("Masukan kecepatan dalam satuan kilometer: ")
	waktu = input("Masukan waktu dalam satuan jam: ")

	hasil = Rumus.menghitung_jarak(kecepatan, waktu)
	print(hasil)
if a == 2:
	jarak = input("Masukan jarak tempuh dalam satuan meter: ")
	waktu = input("Masukan waktu dalam satuan sekon/detik: ")

	hasil = Rumus.menghitung_kecepatan(jarak, waktu)
	print(hasil)
if a == 3:
	kecepatan = input("Masukan kecepatan dalam satuan meter/sekon: ")
	jarak = input("Masukan jarak tempuh dalam satuan meter: ")

	hasil = Rumus.menghitung_waktu(kecepatan, jarak)
	print(hasil)
