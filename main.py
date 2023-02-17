import tkinter as tk
import requests

from function_helpers import Function

token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2JkYjAxMGE2LTFkMDUtNDk4Zi04MWI0LWJhNzgzNTY0M2RiNS8iLCJpYXQiOjE2NzY2NDM5NjcsIm5iZiI6MTY3NjY0Mzk2NywiZXhwIjoxNjc2NjQ4MzY4LCJhY3IiOiIxIiwiYWlvIjoiQVdRQW0vOFRBQUFBWlZwZFROVUFFb0hkTks2aTlHVVNoTXZpVmtQektEVlNpRjRBN3NGSnk0M2ppN2wrRXRZOXB2clpCTEYwNjJaMkt5dzZZbzhVL0F0RWwzWlRLOExVYVhhVmErS1dsSlRrVDNSb0ZuMHNrVjNjUFRwQjduWEllbHVLS09XdzB2WTkiLCJhbHRzZWNpZCI6IjU6OjEwMDMyMDAxRTcxOTUxQ0IiLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJhbnRvbi5zZXJiZXpvdkBhZGFzdHJhZ3JwLmNvbSIsImZhbWlseV9uYW1lIjoiU2VyYmV6b3YiLCJnaXZlbl9uYW1lIjoiQW50b24iLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kZDkyZjhlYy04M2ZjLTQ0YzQtYjI3Ny0xYzQxMjBmYWUyMWMvIiwiaXBhZGRyIjoiODUuMTg3LjIyNC4xOTciLCJuYW1lIjoiU2VyYmV6b3YsIEFudG9uIiwib2lkIjoiNWZlYmY3OWMtYjZiMS00NGJmLTk5YTEtYTA0ZjFhMmRiZTNkIiwicHVpZCI6IjEwMDMyMDAyMDgwNUU2OTYiLCJyaCI6IjAuQVRBQXBoQ3d2UVVkajBtQnRMcDROV1E5dFVaSWYza0F1dGRQdWtQYXdmajJNQk13QUljLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6InZXd1p5d0ZsNkhwTXphamtfdEg0RTN0Z0Y4N3F2aDF2dkpVUzhFelgyd0UiLCJ0aWQiOiJiZGIwMTBhNi0xZDA1LTQ5OGYtODFiNC1iYTc4MzU2NDNkYjUiLCJ1bmlxdWVfbmFtZSI6ImFudG9uLnNlcmJlem92QGFkYXN0cmFncnAuY29tIiwidXRpIjoiaVlfa0Q3Mk1xMFdRbHhpMU9EZzhBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiMTNiZDFjNzItNmY0YS00ZGNmLTk4NWYtMThkM2I4MGYyMDhhIl0sInhtc190Y2R0IjoxNTMyMzQ3MzUxfQ.OslyuF0j95xhZrVlcut9n9gg2w3EZUp1WdpFzqag43dtNSq8aMKrrtaDIKoKqhzQT6e4C-XKH1q626I1N6wS3Gt8fgviD7qpkiCBm74-UUtfI5M73yixIwWCVeY2zN2WiTx0tP0_8S0tGhsLn_iYLuWrFfF-Caddj4EBCDyEKzen5GJ8Ej3hyQvbqBdlQR0dGus37Wq0X_Eaxb9WCRr-fcJI8SXRNZX3c8Kfm6QNbObsLERoNVSAxmHuesPSbjK3IH94RCWcYlsCj3tUWiqXH6ZuS-ECFzarVnbkj4Nv1_G02hsIZBed5nrrxBIiixWAvn5l-W1ZSks1wcW8Sl_aRw'
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
