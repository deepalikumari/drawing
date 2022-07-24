from sketchpy import canvas
obj = canvas.sketch_from_image('D:\image_drawer\img.jpg') #img path
obj.draw(threshold = 127)
#draw image of jpg file. 
#use threshold to draw more detailed img,its range 0-255,use btw 90-190