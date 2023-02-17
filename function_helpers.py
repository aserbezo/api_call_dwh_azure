import requests


class Function:

    # method  take two parameters header abd subscription ID and returns a list of resource group names
    @staticmethod
    def get_resource_groups(header, subs):
        list_resources_group = []
        url = f'https://management.azure.com/subscriptions/{subs}/resourceGroups?api-version=2020-01-01'
        response = requests.get(url, headers=header)
        res = response.json()

        for resource_group_name in res['value']:
            ready = {'Resource_group_name': ''}
            ready['Resource_group_name'] = resource_group_name['name']
            list_resources_group.append(ready)
        return list_resources_group

    # method take three header , subscription id and resource group name and return  a list of server names
    @staticmethod
    def get_servers(header, subs, resource_name):
        servers_list = []

        url = f'https://management.azure.com/subscriptions/{subs}/resourceGroups/' \
              f'{resource_name}/providers/Microsoft.Sql/' \
              f'servers?api-version=2017-03-01-preview'
        response = requests.get(url, headers=header)

        res = response.json()
        for server in res['value']:
            server_name = server['name']
            servers_list.append(server_name)
        return servers_list

    # method which takes a three four params : header , subs id , resource group name and server and
    # return a list with dict {'resource_group_nane': '', 'server_name': '', 'database_name': ''}
    @staticmethod
    def get_database(header, subs, resource_name, server_names):
        list_database = []
        # print(resource_name)

        for server_name in server_names:
            url = f'https://management.azure.com/subscriptions/{subs}/resourcegroups/' \
                  f'{resource_name}/providers/Microsoft.Sql/servers/{server_name}' \
                  f'/databases?api-version=2020-08-01-preview'

            # print(ready_dict)
            response = requests.get(url, headers=header)
            res = response.json()

            for name in res['value']:
                database_name = name['name']
                if database_name == 'master':
                    pass
                # print(f'{resource_name}={server_name} = {database_name}')
                else:
                    ready_dict = {'resource_group_name': '', 'server_name': '', 'database_name': '', 'status': ''}
                    ready_dict['resource_group_name'] = resource_name
                    ready_dict['server_name'] = server_name
                    ready_dict['database_name'] = database_name
                    status = Function.get_status_database(header,subs,resource_name,server_name,database_name)
                    ready_dict['status'] = status
                    list_database.append(ready_dict)

        return list_database

    @staticmethod
    def get_status_database(header, subs, resource_name, serverName, database_name):
        status = []
        url = f'https://management.azure.com/subscriptions/{subs}' \
              f'/resourcegroups/{resource_name}/providers/Microsoft.Sql/servers/{serverName}' \
              f'/databases/{database_name}?api-version=2020-08-01-preview'
        response = requests.get(url, headers=header)
        res = response.json()
        # print(res)
        # database_name = res['name']
        status = res['properties']['status']

        return status
