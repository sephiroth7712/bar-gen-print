from code128 import Code128
import svgwrite
import barcode

def barcode_svg(barcode_string):
    try:
        barcode_svg = barcode.get(
                'code39',
                barcode_string).render(writer_options=None)
    except Exception as error:
        return {
                "error": 500,
                "message": str(error)
                }
    # print barcode_svg
    return barcode_svg

def generate_barcode(a,value):
    # code = Code128()
    # binary = code.makeCode(barcode)
    # if binary:
    final=''
    svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg", size = ("400px", "300px"))
    start_x = 50
    start_y = 50
    bar_size = ("2px", "70px")
    x = 0
    print svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(0,0,0)")
    svg_document.add(svg_document.text(a,insert=(start_x+50,start_y)))
    final+=svg_document.tostring()
    final=final[:-6]
    print final
    final+="""<g transform="translate(100,100)">"""
    brc=barcode_svg(value)
    final+=brc+"</g></svg>"
    # for b in binary:
    #     if b == '1':
    #         svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(0,0,0)"))
    #     else:
    #         svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(255,255,255)"))
    #     x += 2
    return final
