from PIL import Image
import random

hill = Image.open("hill.jpg")
babyPerson = Image.open("babyPerson.JPEG")
originalhill = Image.open("hill.jpg")

def greenscreen(background, im):
  (width, height) = background.size
  for x in range(width):
    for y in range(height):
      (red, green, blue) = im.getpixel((x,y))
      if red < (0b101000) and green > (0b10010110) and blue < (0b1010000):
        pass
      else:
        background.putpixel((x,y), (red, green, blue))

def grayscale(im):
  
  (width, height) = im.size

  for x in range(width):
    for y in range(height):
      (red, green, blue) = im.getpixel((x,y))
            
      lum = ((int) (0.21 * red) + (int) (0.72 *green) + (int)(0.07 * blue))

      im.putpixel((x, y), (lum, lum, lum))
        

grayscale(hill)
hill.save("result.jpg")


result = Image.open("result.jpg")

def randomFilter1(im, xx, yy):
  # (width, height) = im.size
  
  # startx = random.randint(20, 100)
  # starty = random.randint(20, 100)
  # endx = random.randint(startx + 200, 530 )
  # endy = random.randint(starty + 200, 323 )
           

  
  for x in range(340):
    for y in range(154):
      # if x > startx and x < endx and y > starty and y < endy:

      (red, green, blue) = originalhill.getpixel((xx+x,yy+y))

      red = (int) (red*.80)
      if red < 0:
        red = 0
      blue = blue + 30
      if blue > 255:
        blue = 255
      green = (int)(green*0.65)
      if green < 0:
        green = 0
        
      im.putpixel((xx+x,yy+y),(red, green, blue))

# randomFilter1(result)
# result.save("result.jpg")



def randomFilter2(im, xx, yy):
  # (width, height) = im.size
  
  for x in range(0b101010100):
    for y in range(0b10011010):

      (red, green, blue) = originalhill.getpixel((xx+x,yy+y))

      red = red + (0b1010)
      if red > (0b11111111):
        red = (0b11111111)
      blue = blue + (0b1010000)
      if blue > (0b11111111):
        blue = (0b11111111)
      green = green + (0b1010)
      if green > (0b11111111):
        green = (0b11111111)
      
      im.putpixel((xx+x,yy+y),(red, green, blue))

# randomFilter2(result)
# result.save("result.jpg")

def randomFilter3(im, xx, yy):
  
  # (width, height) = im.size

  # startx = random.randint(20, 100)
  # starty = random.randint(343, 423)
  # endx = random.randint(startx + 200, 530 )
  # endy = random.randint(starty + 200, 647 )
  for x in range(340):
    for y in range(154):
      # if x > startx and x < endx and y > starty and y < endy:
      (red, green, blue) = originalhill.getpixel((xx+x,yy+y))
            
      # red = (int)(red*0)
      # if red > 255:
      #   red = 255
      # blue = (int)(blue*1.7)
      # if blue > 255:
      #   blue = 255
      # green = (int)(green*1.7)
      # if green > 255:
      #   green = 255
      red = (int)(red*1.3)
      blue = (int)(blue*1.3)
      green = (int)(green*1.3)
      
      im.putpixel((xx+x,yy+y),(red, green, blue))

# randomFilter3(result)
# result.save("result.jpg")


def randomFilter4(im, xx, yy):
  
  # (width, height) = im.size
  # startx = random.randint(540, 620)
  # starty = random.randint(343, 423)
  # endx = random.randint(startx + 200, 1041 )
  # endy = random.randint(starty + 200, 647 )
  for x in range(340):
    for y in range(154):
      # if x > startx and x < endx and y > starty and y < endy:
      # print(str(xx+x)+", "+str(yy+y))
      (red, green, blue) = originalhill.getpixel((xx+x,yy+y))
            
      red = red + 60
      if red > 255:
        red = 255
      blue = blue + 80
      if blue > 255:
        blue = 255
      green = green + 10
      if green > 255:
        green = 255
      
      im.putpixel((xx+x,yy+y),(red, green, blue))

# randomFilter4(result)
# result.save("result.jpg")




def filterrect(im):
  (width, height) = im.size
  for j in range(11, width, 350):
    for k in range(11, height, 164):
      randomf = random.randint(1, 4)
      if randomf == 1:
        randomFilter1(result, j, k)
      elif randomf == 2:
        randomFilter2(result, j, k)
      elif randomf == 3:
        randomFilter3(result, j, k)
      elif randomf == 4:
      # print(str(j)+"; "+str(k))
        randomFilter4(result, j, k)

filterrect(result)
result.save("result.jpg")          
greenscreen(result, babyPerson)
result.save("result.jpg")


print("code complete")