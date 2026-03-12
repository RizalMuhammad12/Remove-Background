from withoutbg import WithoutBG

img = WithoutBG.opensource()
result = img.remove_background("Jack.jpg")
result.save("hasil.png")