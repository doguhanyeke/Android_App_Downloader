import os
from os import listdir
from os.path import isfile, join, isdir

path_phone = "/Users/doguhanyeke/PycharmProjects/app_statistics/wear_dataset2_phone"
path_watch = "/Users/doguhanyeke/PycharmProjects/app_statistics/wear_dataset2"
wearflow_apps_path = "/Users/doguhanyeke/PycharmProjects/app_statistics/wearflow_packagenames.txt"
wearflow_app_write = "/Users/doguhanyeke/PycharmProjects/app_statistics/wearflow_apps.txt"

def compare_watch_and_phone_datasets(folder_path_phone, folder_path_watch):
    dir_list_watch_set = set([f for f in listdir(folder_path_watch) if isdir(join(folder_path_watch, f))])
    dir_list_phone_set = set([f for f in listdir(folder_path_phone) if isdir(join(folder_path_phone, f))])

    common_apks = dir_list_watch_set.intersection(dir_list_phone_set)
    only_watch = dir_list_watch_set.difference(dir_list_phone_set)
    only_phone = dir_list_phone_set.difference(dir_list_watch_set)
    print("Common app size: ", len(common_apks))
    print("Only watch app set: ", only_watch)
    print("Only phone app set: ", only_phone)

    return (common_apks, only_phone, only_watch)

def get_wearflow_apks(file_path):
    app_list = []
    fd = open(file_path, "r")
    line = fd.readline()
    line = line.replace("\n", "")
    while line:
        if line != "":
            tmp_line = line[23:]
            app_list.append(tmp_line)
        line = fd.readline()
        line = line.replace("\n", "")
    print("Wearflow app size: ", len(app_list))
    return set(app_list)

def save_wearflow_apps(file_path):
    fd_write = open(wearflow_app_write, "w")
    fd = open(file_path, "r")
    line = fd.readline()
    line = line.replace("\n", "")
    while line:
        if line != "":
            tmp_line = line[23:]
            fd_write.write(tmp_line)
            fd_write.write("\n")
            fd_write.flush()
        line = fd.readline()
        line = line.replace("\n", "")

def write_to_file(apps, new_file_name):
    f_write = open(new_file_name, "w")
    for app in apps:
        f_write.write(app)
        f_write.write("\n")
        f_write.flush()



if __name__ == '__main__':
    (common_apps, phone_apps, watch_apps) = compare_watch_and_phone_datasets(path_phone, path_watch)
    wearflow_apps = get_wearflow_apks(wearflow_apps_path)
    common = common_apps.intersection(wearflow_apps)
    print(len(common_apps))
    print(common)
    wearflow_only = wearflow_apps.difference(common_apps)
    # write_to_file(list(common_apps), "wearapps_both_phone_and_watch.txt")
    # write_to_file(list(wearflow_only), "wearflow_only.txt")
    # print(len(wearflow_only))
    # save_wearflow_apps(wearflow_apps_path)
