import tkinter as tk
import requests

from function_helpers import Function

# working
def main_logic(header, subs):
    RESOURCE_GROUP_NAMES_AND_SERVERS = []
    # this is working
    result_res = Function.get_resource_groups(header, subs)
    #print(result_res)
    #result_res = [{'Resource_group_name': 'api_call_tests'}, {'Resource_group_name': 'second'}]
    for resource_name in result_res:
        ready_dict = {'Resource_group_name': '', 'sql': []}
        resource_grp_name = resource_name['Resource_group_name']
        ready_dict['Resource_group_name'] = resource_grp_name
        result_res_ser = Function.get_servers(header, subs, resource_grp_name)
        ready_dict['sql'].extend(result_res_ser)
        RESOURCE_GROUP_NAMES_AND_SERVERS.append(ready_dict)

    return RESOURCE_GROUP_NAMES_AND_SERVERS


def get_database_status(header, subs, RESOURCE_GROUP_NAMES_AND_SERVERS):
    DATABASE_STATUS = []
    for res in RESOURCE_GROUP_NAMES_AND_SERVERS:
        res_name = res['Resource_group_name']
        # print(res_name)
        sql_names = res['sql']
        # print(sql_names)
        res_ser = Function.get_database(header, subs, res_name, sql_names)
        DATABASE_STATUS.extend(res_ser)

    # print(self.DATABASE_STATUS)
    return DATABASE_STATUS


