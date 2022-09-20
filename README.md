# image-to-pdf

<p>convert images to pdf you select multiple if you want ;) </p>

#converting function
def img_pdf(filename,output):
    images = []
    for file in filename:
        im  = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
    images[0].save(output,save_all=True,append_images=images[1:])

    tk.messagebox.showinfo("Success","Your PDF has been created")
