[x,y,ty,count] = textread('draw.out','%f %f %d,%d');
x = round(x,0);
y=round(3000-y,0);
ty = int16(ty);
image1 = zeros(3000,3000);
image2 = zeros(3000,3000);
image3 = zeros(3000,3000);
image4 = zeros(3000,3000);
image5 = zeros(3000,3000);
for i = 1:size(x)
    if x(i)<=0
        x(i)=1;
    end
    if y(i)<=0
        y(i) =1;
    end
    if ty(i)==1
        image1(y(i),x(i))=count(i);
    end
    if ty(i)==2
       image2(y(i),x(i))=count(i);
    end
    if ty(i)==3
        image3(y(i),x(i))=count(i);
    end
    if ty(i)==4
        image4(y(i),x(i))=count(i);
    end
    if ty(i)==5
        image5(y(i),x(i))=count(i);
    end

end
figure(1)
imshow(image1)
figure(2)
imshow(image2)
figure(3)
imshow(image3)
figure(4)
imshow(image4)
figure(5)
imshow(image5)
