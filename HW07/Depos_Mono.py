def skl_vidsotok(s_vkl, term, vids, dodsm):
    vids = round((vids * (1 - 0.18 - 0.015)), 3)
    vid_mis = (vids/12)/100
    s_vkl2 = s_vkl + (s_vkl * vid_mis)
    for m in range(1, term):
        s_vkl2 = s_vkl2 + dodsm
        s_vkl2 = s_vkl2 + (s_vkl2 * vid_mis)
    print('Ви отримаєте: ', round(s_vkl2, 2), ' грн')
    return s_vkl2

skl_vidsotok(int(input('Сума депозиту: ')), int(input('Термін міс: ')), int(input('Річний відсоток: ')), int(input('Сума щомісячного поповнення: ')))