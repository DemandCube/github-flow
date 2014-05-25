import click
import requests 
from tabulate import tabulate

class github:
    def __init__(self,ghf):
        self.ghf=ghf
        
    # def repos(self,org):
    #     if self.ghf.debug: click.echo("org:"+org+" token:"+self.ghf.token)
    #     url='https://api.github.com/orgs/'+org+'/repos'
    #     headers=self.get_auth_header()
    #     data=''
    #     r = requests.get(url, headers=headers, data=data)
    #     fields = ['full_name']
    #     if len(self.ghf.fields) > 0:
    #         fields = self.ghf.fields
    #     if self.ghf.profile:
    #         self.profile_keys(r.json())
    #     else:
    #         self.print_object_array_with_fields(r.json(),fields)
    
    def repos(self,org):
        url='https://api.github.com/orgs/'+org+'/repos'
        fields = ['full_name']
        headers=self.get_auth_header()
        self.make_github_get_request(fields,url,headers)

    
    def make_github_get_request(self,default_fields,url,headers,data=''):
        if self.ghf.debug: click.echo("url:"+url+" token:"+self.ghf.token+" fields:"+",".join(default_fields))
        r = requests.get(url, headers=headers, data=data)
        fields = default_fields
        if len(self.ghf.fields) > 0:
            fields = self.ghf.fields
        table = []
        if self.ghf.profile:
            (fields,table) = self.get_profile_table(r.json())
        else:
            table = self.get_table_from_object_array_with_fields(fields,r.json())
        self.print_table(fields,table)
    
    def print_table(self, field_names, table):
        if self.ghf.export_csv:
            separator = self.ghf.csv_separator
            if self.ghf.print_header_row:
                click.echo(separator.join(field_names))
            for entry in table:
                click.echo(separator.join(entry))
        else:
            if self.ghf.print_header_row:
                click.echo(tabulate(table, field_names, tablefmt="simple"))
            else:
                click.echo(tabulate(table, tablefmt="simple"))
    
    def test_post(self,url,headers,data):
        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 201:
            click.echo(r.json())
        elif r.status_code == 401:
            click.echo("Error:"+r.json()['message'])
        else:
            click.echo('status:'+str(r.status_code))
            click.echo(r.text)
    
    def test_get(self,url,headers,data):
        r = requests.get(url, headers=headers, data=data)
        if r.status_code == 201:
            click.echo(r.json())
        elif r.status_code == 401:
            click.echo("Error:"+r.json()['message'])
        else:
            click.echo('status:'+str(r.status_code))
            click.echo(r.text)
    
    
    def get_auth_header(self):
        headers={'Authorization' : 'token '+self.ghf.token}
        return headers
        
        
        
    def get_profile_table(self,json):
        outter_key_hash = {}
        inner_key_hash = {}
        if type(json) == type([]):
            for item in json:
                if type(item) == type(u''):
                    outter_key_hash[item] = 1 if item not in outter_key_hash else outter_key_hash[item] + 1
                if type(item) == type({}):
                    for inner_item in item:
                        if type(inner_item) == type(u''):
                            inner_key_hash[inner_item] = 1 if inner_item not in inner_key_hash else inner_key_hash[inner_item] + 1
        # elif type(json) == type({}):
#             None
        table = []
        for key, value in outter_key_hash.items():
            table.append(['level1',key,str(value)])
        for key, value in inner_key_hash.items():
            table.append(['level2',key,str(value)])
        field_names = ['level', 'name','count']
        table = sorted(table, key=lambda key: key[1])
        return (field_names,table)
#        click.echo(tabulate(table, field_names, tablefmt="simple"))
        
    def get_table_from_object_array_with_fields(self,fields,json):
        table = []
        if type(json) == type([]):
            for item in json:
                if type(item) == type({}):
                    row = []
                    for field in fields:
                        if field in item:
                            row.append(item[field])
                        else:
                            row.append('')
                    table.append(row)                                
        headers = fields
        return table
#        click.echo(tabulate(table, headers, tablefmt="simple"))
        
        
    # >>> js = ['name1', 'name2', {'iname1':11,'iname2':12}]
    # >>> for item in js:
    # ...     print type(item)
    # ... 
    # <type 'str'>
    # <type 'str'>
    # <type 'dict'>