import svgwrite
import barcode
import xml.etree.ElementTree as ET

#wrapper function to generate svg xml string using pyBarcode module
def barcode_svg(barcode_string,format):
    try:
        barcode_svg = barcode.get(
                format,
                barcode_string).render(writer_options=None)
    except Exception as error:
        return {
                "error": 500,
                "message": str(error)
                }
    # print barcode_svg
    return barcode_svg

#function to convert millimetres to pixel
def mm2px(mm):
    px=mm*3.7795275591
    return  str(px)

#function to generate final barcode svg using given value,
#TODO make function parameter a an array that acceps a list of strings that the user wishes to appear with the barcode
def generate_barcode(a,value,format):
    final=''
    svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg", size = ("400px", "300px"))
    start_x = 50
    start_y = 50
    bar_size = ("1.2472440945px", "56.692913386px")
    x = 0.0
    brc=barcode_svg(value,format)
    root = ET.fromstring(brc)
    nsmap = {'n': 'http://www.w3.org/2000/svg'}
    i=0
    #using svg string output from barcode_svg to generate new svg that can include user input strings for future use
    for item in root.findall('n:rect', namespaces=nsmap):
        # if i==0:
        #     i+=1
        #     continue
        height = item.attrib['height']
        style=item.attrib['style']
        width=item.attrib['width']
        bar_size=(mm2px(float(width[:-2])*1.5),mm2px(float(height[:-2])*1.5))
        if style[-6:-1]=='black':
            svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(0,0,0)"))
        else:
            svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(255,255,255)"))
        x+=float(mm2px(float(width[:-2])))*1.5
    item=root.find('n:text',  namespaces=nsmap)
    svg_document.add(svg_document.text(item.text, insert = (start_x + 125, start_y + float(mm2px(float(height[:-2])))*1.5+20)))
    return svg_document.tostring()
