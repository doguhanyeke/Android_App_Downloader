import os

import xml.etree.ElementTree as ET

# output: ( Success:1/Fail:0, File_Path/None)
def download_with_androzoo(apk_package_name):
    pass

# output: Success: 1 / Fail: 0
def decompile_with_jadx(input_file_path, output_folder_path):
    try:
        ret_val = os.system("jadx -d {} {}".format(output_folder_path, input_file_path) )
        print("Return value: ", ret_val)
        if ret_val == 0:
            return 1
        else:
            return 0
    except Exception as e:
        print("Error in decompile with jadx!")
        print(e)
        return 0

# output: (isWatchApp, isTightlyDependent)
def inspect_manifest(folder_path):
    manifest_file_path = folder_path + "/resources/AndroidManifest.xml"
    xmlTree = ET.parse(manifest_file_path)
    app_stats = {
        "watch": False,
        "tightCoupled": False
    }
    for elem in xmlTree.iter():
        if elem.tag == "uses-feature":
            if "android.hardware.type.watch" in elem.attrib.values():
                app_stats["watch"] = True
        elif "com.google.android.wearable.standalone" in elem.attrib.values() and "false" in elem.attrib.values():
            app_stats["tightCoupled"] = True
    return app_stats

def create_phoneapk_and_wearapk():
    
    pass


# output: (
# total_package_names,
# total_available_apks,
# total_downloadables_with_androzoo,
# total_decompilable_ones,
# total_manifest_chekable_ones,
# total_no_werables,
# total_no_tightly_coupled_ones
# )
def main(app_statistics_tuple):
    pass


# tests
if __name__ == '__main__':
    # jadx decompilation tests

    # ret_val = decompile_with_jadx(
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/apks/fr.thema.wear.watch.venom_22018_apps.evozi.com.apk",
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/output_folder")
    # if ret_val: print("Success")
    # else: print("Failed")
    #
    # ret_val = decompile_with_jadx(
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/apks/marine-commander-watch-face-for-wearos.apk",
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/output_folder2")
    # if ret_val: print("Success")
    # else: print("Failed")
    #
    # ret_val = decompile_with_jadx(
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/apks/wearoscom.mapmyrun.android2_22.4.1-22040100_minAPI24\(nodpi\)_apkmirror.com.apk",
    #     "/Users/doguhanyeke/PycharmProjects/app_statistics/output_folder3")
    # if ret_val:
    #     print("Success")
    # else:
    #     print("Failed")

    # inspect manifest check
    # return_dict = inspect_manifest("/Users/doguhanyeke/PycharmProjects/app_statistics/output_folder3")
    # print(return_dict)
    pass