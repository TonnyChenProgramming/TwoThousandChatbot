def filename_correction(input_filename):
    output_filename = ''
    illegal_characters = ['#','%','&','{','}','\\','<','?','*','?','/','$','!',':','+','|','=']
    for character in input_filename:
        if character in illegal_characters:
            output_filename+=''
        else:
            output_filename+=character
    return output_filename