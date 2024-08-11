from django.shortcuts import render
import openai
openai.api_key=''

def home(request):
    image_url=None

    if request.method=="POST":
        data=request.POST
        prompt=data['prompt']
        
        response = openai.Image.create(
                prompt=prompt,
                )
        image_url = response['data']
        imgurls=[]
        for i in image_url:
            imgurls.append(i['url'])

    return render(request,'home.html',{'files':image_url})