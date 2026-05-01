def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
               arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr

# Input jumlah data
n = int(input("Masukkan jumlah data: "))
data= []

# Input satu per satu
for i in range(n):
    angka =int(input(f"Masukkan angka ke-{i+1}: "))
    data.append(angka)
    
print("Data sebelum sorting: ", data)

# Proses
hasil = bubble_sort(data)

print("Data setelah sorting:", hasil)