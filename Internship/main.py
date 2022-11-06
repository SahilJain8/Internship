from flask import Flask,request
import PyPDF2



app=Flask(__name__)

def PDFrotate(origFileName, newFileName,rotation,page_number):
  
    pdfFileObj = open(origFileName, 'rb')
      

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  

    pdfWriter = PyPDF2.PdfFileWriter()
      
 
    for page in range(pdfReader.numPages):
  
        pageObj = pdfReader.getPage(page)
        if page==2:
            pageObj.rotateClockwise(rotation)
  
     
        pdfWriter.addPage(pageObj)
  
   
    newFile = open(newFileName, 'wb')
      
    
    pdfWriter.write(newFile)
  
   
    pdfFileObj.close()
    
    newFile.close()

    

@app.route('/')
def home():
    return "hello world"


@app.route('/rotation', methods=['POST'])
def predict():

    origFileName= request.files['filename']
   
    rotation_angle=request.form['angle']
    page_no=request.form['no']
    if origFileName.filename != '':
        origFileName.save(origFileName.filename)
    
    newFileName =str(origFileName.filename)+"_rotated.pdf"
    PDFrotate(origFileName.filename, newFileName, int(rotation_angle),page_no)

    return "done"
      


if __name__=="__main__":
    app.run()