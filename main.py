import tkinter as tk
import requests

from function_helpers import Function

token = []
header = {'Authorization': token, 'Content-Type': 'application/json'}
subs = 'f103bbde-bf4d-44fd-817e-cde5ab222ece'

final = [{'resource_group_nane': 'api_call_tests', 'server_name': 'apicalltest', 'database_name': 'api_call_dwh_test',
          'status': 'Paused'},
         {'resource_group_nane': 'api_call_tests', 'server_name': 'apicalltest', 'database_name': 'this_second_dhw',
          'status': 'Paused'},
         {'resource_group_nane': 'second', 'server_name': 'seconderver', 'database_name': 'second_api_test',
          'status': 'Paused'}]


class Main:
    RESOURCE_GROUP_NAMES_AND_SERVERS = [
        {'Resource_group_name': 'api_call_tests', 'sql': ['secondservertest', 'apicalltest']},
        {'Resource_group_name': 'second', 'sql': ['seconderver']}]
    DATABASE_STATUS = [{'resource_group_name': 'api_call_tests', 'server_name': 'apicalltest', 'database_name': 'api_call_dwh_test', 'status': 'Paused'}, {'resource_group_name': 'api_call_tests', 'server_name': 'apicalltest', 'database_name': 'this_second_dhw', 'status': 'Paused'}, {'resource_group_name': 'second', 'server_name': 'seconderver', 'database_name': 'second_api_test', 'status': 'Paused'}]

    def __init__(self, token, subs):
        self.token = token
        self.subs = subs
        self.header = {'Authorization': token, 'Content-Type': 'application/json'}

    # working
    def main_logic(self):
        # this is working
        # result_res = Function.get_resource_groups(header, subs)
        # print(result_res)
        result_res = [{'Resource_group_name': 'api_call_tests'}, {'Resource_group_name': 'second'}]
        for resource_name in result_res:
            ready_dict = {'Resource_group_name': '', 'sql': []}
            resource_grp_name = resource_name['Resource_group_name']
            ready_dict['Resource_group_name'] = resource_grp_name
            result_res_ser = Function.get_servers(header, subs, resource_grp_name)
            ready_dict['sql'].extend(result_res_ser)
            self.RESOURCE_GROUP_NAMES_AND_SERVERS.append(ready_dict)

        return ''

    def get_database_status(self):
        for res in self.RESOURCE_GROUP_NAMES_AND_SERVERS:
            res_name = res['Resource_group_name']
            # print(res_name)
            sql_names = res['sql']
            # print(sql_names)
            res_ser = Function.get_database(header, subs, res_name, sql_names)
            self.DATABASE_STATUS.extend(res_ser)

        #print(self.DATABASE_STATUS)
        return ''


Main(token, subs)
#
# print(Main.main_logic(Main))
print(Main.get_database_status(Main))
