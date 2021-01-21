# 9128
# progressbar
# Paul Fratila

from TKmodule import ttk


def pr_bar(mod):
    """Alege mod hd,hi,vd,vi"""

    root = Tk()

    if mod == 'hd':
        pb_hd = ttk.Progressbar(root, orient='horizontal', mode='determinate', length = 200)
        pb_hd.pack(expand=True, fill=BOTH, side=TOP)        # Parametrii sunt optionali
        pb_hd.start()

    elif mod == 'hi':
        pb_hi = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length = 300)
        pb_hi.pack(expand=True, fill=BOTH, side=TOP)
        pb_hi.start()

    elif mod == 'vd':
        pb_vd = ttk.Progressbar(root, orient='vertical', mode='determinate', length = 400)
        pb_vd.pack(expand=True, fill=BOTH, side=LEFT)
        pb_vd.start()

    elif mod == 'vi':
        pb_vi = ttk.Progressbar(root, orient='vertical', mode='indeterminate', length = 500)
        pb_vi.pack(expand=True, fill=BOTH, side=LEFT)
        pb_vi.start()

    root.mainloop()

pr_bar('vi')
pr_bar('hi')
pr_bar('hd')
pr_bar('vd')

input('')
