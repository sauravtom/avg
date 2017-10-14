
import random
import requests
import shutil
import time

def download_image(url,output_path):
    if not output_path:
        output_path = 'temp/%s'%(url.split('/')[-1])
    
    print 'Downloading... %s to %s'%(url,output_path)

    response = requests.get(url, stream=True)
    with open(output_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def styletransfer(file_name,file_path,output_dir,temp_file_prefix,style_number):
    name=file_name.split('.')[0]

    r = requests.post('http://turbo.deepart.io/api/post/',
                      data={'style': style_number,
                            'return_url': 'http://my.return/' },
                      files={ 'input_image': ( file_name, open(file_path, 'rb'), 'image/jpeg' ) } )
    img=r.text
    link=("http://turbo.deepart.io/media/output/%s.jpg" % img)
    time.sleep(6)
    download_path='%s/%s%s_%s.jpg'%(output_dir,temp_file_prefix,name,style_number)
    download_image(url=link,output_path='%s'%(download_path))
    return download_path