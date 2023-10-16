from django.shortcuts import render, redirect
from PIL import Image
from django.http import HttpResponse
from django import forms
from django.core.files import File
import numpy as np
import cv2 as cv
import sys
from .models import Photo

def success(request):
    searchWord = request.POST.get('search','')
    return render(request,'index.html')


class redFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(redFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def red(r,g,b):
            newr=r
            newg=0
            newb=0
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()
        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=red(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class blueFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(blueFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def blue(r,g,b):
            newr=0
            newg=0
            newb=b
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()

        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=blue(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class greenFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(greenFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        
        def green(r,g,b):
            newr=0
            newg=g
            newb=0
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()

        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=green(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class yellowFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(yellowFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def yellow(r,g,b):
            newr=r
            newg=g
            newb=0
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()

        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=yellow(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class purpleFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(purpleFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def purple(r,g,b):
            newr=r
            newg=0
            newb=b
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()

        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=purple(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class cyanFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(cyanFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def cyan(r,g,b):
            newr=0
            newg=g
            newb=b
            return(newr,newg,newb)
        
        width,height = img.size
        pixels= img.load()


        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=cyan(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class greyFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(greyFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def grey(r,g,b):
            newr=r+g+b//3
            newg=r+g+b//3
            newb=r+g+b//3
            return(newr,newg,newb)

        width,height = img.size
        pixels= img.load()

        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=grey(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class orangeFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(orangeFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        def orange(r,g,b):
            newr=r+r
            newg=g
            newb=0
            return(newr,newg,newb)

        width,height = img.size
        pixels= img.load()
        for py in range(height):
            for px in range(width):
                r,g,b=img.getpixel((px,py))
                pixels[px,py]=orange(r,g,b)
        
        width,height = img.size
        pixels= img.load()
        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 

class noneFilter(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"
    
    def save(self):
        photo = super(noneFilter, self).save()
        img = Image.open(photo.file)
        photos = Photo.objects.all()
        x=photo.description
        print(x)

        newsize = (300, 300) 
        img = img.resize(newsize)
        x=x+".jpg"
        outfile= img.save(x)
        outfile= img.save(photo.file.path) 
        
        return photo 



        
def redphoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = redFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = redFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def bluephoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = blueFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = blueFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def greenphoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = greenFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = greenFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def yellowphoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = yellowFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = yellowFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def purplephoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = purpleFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = purpleFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def greyphoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = greyFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = greyFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def orangephoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = orangeFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = orangeFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def cyanphoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = cyanFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = cyanFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

def nonephoto_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = noneFilter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('red')
    else:
        form = noneFilter()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})







class impaint(forms.ModelForm):
    # x = forms.FloatField(widget=forms.HiddenInput())
    # y = forms.FloatField(widget=forms.HiddenInput())
    # width = forms.FloatField(widget=forms.HiddenInput())
    # height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Photo
        fields = "__all__"
        

    def save(self):
        photo = super(impaint, self).save()

        res = Image.open(photo.file)


        imag = Image.open(photo.file)

        class Sketcher:
            def __init__(self,windowname,dests,colors_func):
                self.prev__pt=None
                self.windowname=windowname
                self.dests=dests
                self.colors_func=colors_func
                self.dirty= False
                self.show()
                cv.setMouseCallback(self.windowname,self.on_Mouse)




            def show(self):
                cv.imshow(self.windowname,self.dests[0])
                cv.imshow(self.windowname+"Masks",self.dests[1])


            def on_Mouse(self, event, x, y, flags, param):
                pt=( x, y)

                if event == cv.EVENT_LBUTTONDOWN:
                    self.prev__pt=pt

                elif event == cv.EVENT_LBUTTONUP:
                    self.prev__pt=None


                if self.prev__pt and flags & cv.EVENT_FLAG_LBUTTON:
                    for dst,color in zip(self.dests,self.colors_func()):
                        cv.line(dst,self.prev__pt,pt,color,5)
                        self.dirty=True
                        self.prev__pt=pt
                        self.show()
        
        def main():
            print ("Inpainting Python ")
            print ("Keys: ")
            print("t- inpainting using Fast Marching method")
            print ("n- Inpainting using NS technique")
            print ("r-reset the mask")
            print ("ESC-exit ")
            img=cv.imread(photo.file.path)
            
            if img is None:
                print ("Failed to import the Image".format(img))
                return

            img_mask=img.copy()
            inpaintMask=np.zeros(img.shape[:2],np.uint8)
            sketch =Sketcher('image',[img_mask,inpaintMask],lambda : ((255,255,255,),255))

            while True:
                ch=cv.waitKey(0)

                if ch==27:
                    break
                if ch==ord('t'):
                    res=cv.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=4,flags=cv.INPAINT_TELEA)
                    cv.imshow("Inpaint using Fast March Methodology", res)
                    

                if ch==ord('n'):
                    res=cv.inpaint(src=img_mask,inpaintMask=inpaintMask,inpaintRadius=4,flags=cv.INPAINT_NS)
                    cv.imshow("Inpaint using NS segmentation", res)
                

                if ch==ord('r'):
                    img_mask[ : ]=img
                    inpaintMask[ : ]=0
                    sketch.show()
            
            cv.imwrite("restor image.JPG",res)
            cv.destroyAllWindows()
            img = Image.open("restor image.JPG")
            newsize=(300,300)
            img=img.resize(newsize)
            outfile= img.save(photo.file.path) 
            
           
        main()
        return photo
    

def inpaint(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = impaint(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inpaint')
    else:
        form = impaint()
    return render(request, 'inpaint.html', {'form': form, 'photos': photos})

