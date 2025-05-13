#list
x = []

#dict
y = {"key": "value"}

#dict->list
z = {
    "nama" : [],
    "umur" : []
}

#index dimulai dari 0
buah = ["mangga", "apel", "duren"]
print(buah[0]) #mangga

#nambah list append dan prepend
buah.append("melon")

biodata = {
    "nama" : "Bintoro",
    "umur" : 25
}

print(biodata["umur"])

biodata2 = {
    "nama" : ["Bintoro","ucup"],
    "umur" : [25,50]
}

print(biodata2["nama"][0])

#input dinamin
namamu = []

for i in range(1,3):
    i_nama = input("masukkan nama kamu : ")
    namamu.append(i_nama)
    print(namamu)

bio = {
    "nim" : [],
    "gender" : []
}

for i in range(1,3):
    i_nim = input("masukkan nama kamu : ")
    bio["nim"].append(i_nim)
    print(bio["nim"])
    i_gender = input("masukkan gender kamu : ")
    bio["gender"].append(i_gender)
    print(bio["gender"])