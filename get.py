def get(conditional=None):
    #Gets Information from the fiddle-configurations file
    import os
    def read(conditionals=conditional):
        try:
            with open('fiddle-configurations.txt', 'r') as fiddle_configurations_raw:
                if conditionals == None:
                    fiddle_configurations = []
                    for i in fiddle_configurations_raw:
                        list_i = list(i)
                        del list_i[-1]
                        i = ""
                        for value in list_i:
                            i += value
                        fiddle_configurations.append(i)
                    del fiddle_configurations[0]
                    return fiddle_configurations
        except Exception as err:
            print(f"Could Not Gather Information from 'fiddle_configurations.txt'\nMore Information:\n" + str(err))
            return ""

    file = read()

    data = {"NAME":file[0], "VERSION":file[1], "VERSION (SHORT)":file[2], "BETA":file[3], "ALPHA":file[4], "PRE-ALPHA":file[5], "AUTHORS":file[6]}

    return data

def raw():
    #Gets Information from the fiddle-configurations file
    import os
    with open('fiddle-configurations.txt', 'r') as fiddle_configurations_raw:
            return fiddle_configurations_raw
