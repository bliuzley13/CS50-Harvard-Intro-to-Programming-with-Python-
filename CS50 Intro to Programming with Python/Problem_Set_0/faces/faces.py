# def emt_t_emj(txt):
#     cnvrt_txt = emj.demojize(txt)
#     return cnvrt.txt

inpt = input(str("Input: "))
inpt = inpt.replace(':)', '🙂')
inpt = inpt.replace(':(', '🙁')

print(inpt)